import os
import requests
import time

# --- CONFIGURATION ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1474075400840810599/B4trxVfxrZPYXm9VTdBfG1uyA3vGNBK2EVtApymHgg9ryZoap8kQ3YZSsLXVTp9sWyS9"
FOLDER_PATH = r"E:\epic games\youtube XL\fast Nigeria"
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}

def upload_images():
    if not os.path.exists(FOLDER_PATH):
        print(f"Error: The folder '{FOLDER_PATH}' does not exist.")
        return

    # Loop through files in the folder
    for filename in os.listdir(FOLDER_PATH):
        ext = os.path.splitext(filename)[1].lower()
        
        if ext in ALLOWED_EXTENSIONS:
            file_path = os.path.join(FOLDER_PATH, filename)
            
            with open(file_path, 'rb') as f:
                payload = {'content': f"Uploaded: {filename}"}
                files = {'file': f}
                
                response = requests.post(WEBHOOK_URL, data=payload, files=files)
                
                if response.status_code == 200 or response.status_code == 204:
                    print(f"Successfully uploaded: {filename}")
                else:
                    print(f"Failed to upload {filename}. Status: {response.status_code}")

            # Sleep for a second to avoid hitting rate limits
            time.sleep(1.5)

if __name__ == "__main__":
    upload_images()