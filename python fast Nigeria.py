import requests
import time
import os
import sys
from datetime import datetime

# Configuration
URL = "https://picsum.photos/1920/1080"
SAVE_PATH = r"E:\epic games\youtube XL\fast Nigeria"
INTERVAL = 40  # seconds

def download_image():
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"image_{timestamp}.jpg"
        full_file_path = os.path.join(SAVE_PATH, filename)

        with open(full_file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Success! Saved to {filename}")

    except Exception as e:
        print(f"\n[!] Error occurred: {e}")

if __name__ == "__main__":
    print(f"--- Downloader Started ---")
    print(f"Target: {SAVE_PATH}\n")
    
    try:
        while True:
            download_image()
            
            # Countdown Logic
            for i in range(INTERVAL, 0, -1):
                # \r moves the cursor back to the start of the line
                sys.stdout.write(f"\rNext download in: {i}s  ")
                sys.stdout.flush()
                time.sleep(1)
                
    except KeyboardInterrupt:
        print("\n\nScript stopped. Happy editing!")