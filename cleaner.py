import os 
from time import sleep
from tqdm import tqdm
import shutil



def cleaner():
    counter_image = 0
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    destination = '/Users/aidanbongiorno/Desktop/images_stuff'

    desktop_files = os.listdir(desktop)

    for filename in desktop_files:
        if filename.endswith("png") or filename.endswith("pdf") or filename.endswith("prt")or filename.endswith("jpeg")or filename.endswith("jpg"):
            counter_image+= 1
            src_path = os.path.join(desktop, filename)
            dst_path= os.path.join(destination, filename)
            
            if os.path.exists(src_path):
                shutil.move(src_path, dst_path)
                sleep(0.5)
            
                
        for i in tqdm (range (counter_image), desc="Loading...",):
            pass
            print("Filename: ", filename)
    print(f"{counter_image} files with the extension 'png' have been moved.")



def main():

    cleaner()

main()
