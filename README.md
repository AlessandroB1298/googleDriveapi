# googleDriveapi


![1_9M_6hUyuPYc7-J3eM6kNwQ](https://github.com/AlessandroB1298/googleDriveapi/assets/98426727/8c82f9de-a6be-422c-ab70-f95dccfc15c1)


## This program is a desktop cleaner which uses the google drive api to store extra files that are removed form your desktop, it can run automatically when you set up a crontsb job



---------------------------------------------------------------------------------------------------------------------------------------------
## Probelms/Solutions

### Instrucitons linked [Here](https://developers.google.com/drive/api/quickstart/python)

### These lines below are very important to the routing of where these files are going to go.

```ruby
# Replace with the correct implementation of Create_Service
service = Create_Service(SERVICE_ACCOUNT_FILE, API_NAME, API_VERSION, SCOPES)
print('Service created successfully')
folder_id = "**************************"
image_folder_id = "***********************"
misc_folder_id="***************************"
```
#### The folder_id, image_folder_id, and misc_folder_id all relate to the endpoints for each of the selected folders.
#### You can find them by going to your google drive, then your selected folder, then look at the last backslash and use that.

---------------------------------------------------------------------------------------------------------------------------------------------


