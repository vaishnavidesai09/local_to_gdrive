from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Step 1: Authenticate
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # creates 'clients_secrets.json' on first run

drive = GoogleDrive(gauth)

# Step 2: Set local folder and Google Drive folder ID
local_folder = r'C:/Users/PC/OneDrive/Documents/docparsing' # give your local systems folder path
drive_folder_id = '12x_DeXTucG7vDXRpmeg-TkpndkHf80no'  # make a folder in google drive and paste its folfer id in this

# Step 3: Upload each file in the local folder
for filename in os.listdir(local_folder):
    file_path = os.path.join(local_folder, filename)

    if os.path.isfile(file_path):  # Only upload files
        gfile = drive.CreateFile({'title': filename, 'parents': [{'id': drive_folder_id}]})
        gfile.SetContentFile(file_path)
        gfile.Upload()
        print(f"Uploaded: {filename}")
