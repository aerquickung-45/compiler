import subprocess
import time

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
url = "https://www.pexels.com"

max_tabs = 13

print("Opening 13 tabs... chaos calibrated 😈")

for i in range(max_tabs):
    subprocess.Popen([edge_path, "--new-tab", url])
    print(f"Opened tab {i+1}/13 💀")
    time.sleep(5)

print("Mission complete. No more tabs.")