import os.path
from googleapiclient.http import MediaFileUpload
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import mimetypes
from tqdm import tqdm
from google.oauth2 import service_account

# Define Create_Service function (replace with your implementation)
def Create_Service(client_secret_file, api_name, api_version, *scopes):
    credentials = service_account.Credentials.from_service_account_file( #This is what was missing, needed a credentials variable to allow permissions.
        client_secret_file, scopes=scopes[0]
    )
    service = build(api_name, api_version, credentials=credentials)
    print(f'Successfully created {api_name} service')
    return service

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.file"]
SERVICE_ACCOUNT_FILE = "./newCreds.json"
API_NAME = 'drive'
API_VERSION = "v3"

# Replace with the correct implementation of Create_Service
service = Create_Service(SERVICE_ACCOUNT_FILE, API_NAME, API_VERSION, SCOPES)
print('Service created successfully')
folder_id = "1cE5w3LSzAjiMLLmndtJ3P7pOTokhLuHH"
image_folder_id = "1rZi3zOw4dzlcqOyHE2dAI37SSuEhfVge"
misc_folder_id="1S9agy36W-ziHFrcaguZMFHphqjGVO8v8"

file_names = [] #list to hold files from the files.
counter =0

path = "/Users/aidanbongiorno/Desktop/images_stuff"

for (root, dirs, file) in os.walk(path):
    for f in file:
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.pdf')):
            file_names.append(f)

for file_name in tqdm(file_names, desc="Uploading files"):
    file_path = os.path.join(path, file_name)
    mime_type, _ = mimetypes.guess_type(file_path) #dynamically gets the mime type, which previously caused only the pngs to upload
    file_extension = os.path.splitext(file_name)[1]
      
    if file_name.endswith((".png", "JPEG", "jpg", "HEIC", "pdf")):
        file_metadata={
        "name": file_name,
        "parents": [image_folder_id]
      }
    else:
        file_metadata = {
            "name": file_name,
            "parents": [misc_folder_id]
        }
        os.remove(file_name)

    media = MediaFileUpload(file_path, mimetype=mime_type)

    try:
      service.files().create(
          body=file_metadata,
          media_body=media,
          fields="id"
      ).execute()        
      print(f'Successfully uploaded {file_name} to Google Drive')
      if file_name.endswith((".gcode", ".prt")):
          parent_folder = misc_folder_id
          print(f'{file_name} Went to misc folder')
          
      elif file_name.endswith((".png", ".jpg", "JPEG", ".pdf")):
          parent_folder = image_folder_id
          print(f'{file_name} Went to image folder')
          
      elif file_name.endswith((".jpeg", ".heic")):
          parent_folder = image_folder_id
          print(f'{file_name} Went to image folder')
          
      else:
          print(f'Unsupported file type for {file_name}')
          continue
            
    except Exception as e:
      continue


print('Script execution completed successfully')

