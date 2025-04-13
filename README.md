project-folder/
├── credentials.json
├── token.json         # (auto-created after login)
├── my_script.py       # (your Python code)
├── MyUploads/         # (your local folder with files)
│   ├── file1.jpg
│   ├── file2.pdf

create virtual env by writing  python -m venv venv command in terminal 
activate this by .\venv\Scripts\Activate
and then write pip install -r requirements.txt

## Upload Local Files to Google Drive with PyDrive

This script uploads all files from a local folder to a specific Google Drive folder using the [PyDrive](https://pythonhosted.org/PyDrive/) library.

---

### Features

- Authenticates with your Google Drive account via OAuth2
- Uploads **all files** from a **specified local folder** to a **target Google Drive folder**
- Saves your OAuth credentials in a `credentials.json` file

---

## Requirements

- Python 3.x
- PyDrive
- Google account with access to Google Cloud Console

---

## Google Cloud Setup Instructions (OAuth Setup)

### Step 1: Create a Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **Select a project** → **New Project**
3. Enter a name (e.g., `DriveUploader`) and click **Create**

---

### Step 2: Enable Google Drive API
1. In your project dashboard, go to `APIs & Services` → `Library`
2. Search for **Google Drive API**
3. Click **Enable**

---

### Step 3: Configure OAuth Consent Screen
1. Go to `APIs & Services` → `OAuth consent screen`
2. Choose **External**
3. Fill in:
   - **App name**
   - **User support email**
   - **Developer contact info**
4. In the **Scopes** section, add:
   - `../auth/drive.file` *(For uploading only to files created by your app)*
   - OR `../auth/drive` *(Full access to Google Drive — use with caution)*

---

### Step 4: Add Test Users
1. Still on the **OAuth Consent Screen**, scroll to **Audience**
2. In **Test Users**, click **Add Users**
3. Add your Gmail (e.g., `vaishnavidesai957@gmail.com`)
4. Save

> You will not be able to sign in with accounts **not** added as test users until the app is verified by Google.

---

### Step 5: Create OAuth Client ID
1. Go to `Credentials` → **Create Credentials** → `OAuth client ID`
2. Choose **Desktop app** (or Web if you're deploying online)
3. Click **Create**, and download the `client_secrets.json`

---

###  Step 6: Set Up Your Python Script

1. Save `client_secrets.json` in the same directory as your Python script.
2. Install PyDrive:

```bash
pip install PyDrive
```

3. Run your script:


python my_scripts.py


4. A browser window will open — log in using the **test user account** you added.

---

## 📁 Folder Setup

Replace the following in your script:
- `local_folder`: Set your local folder path.
- `drive_folder_id`: Find your Google Drive folder ID by opening it in a browser and copying the ID from the URL.

---

## Output

Each file from the local folder will be uploaded to the selected Drive folder, and you'll see:

```bash
Uploaded: file1.pdf
Uploaded: file2.docx
...
```

---


- The first time you run the script, it will create a `credentials.json` for you.
- This method uses **user-based OAuth**, so only authorized users can run it unless the app is verified.

