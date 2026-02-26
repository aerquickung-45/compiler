import keyboard
from playsound import playsound
import time
import threading

SOUND_PATH = r"E:\epic games\youtube XL\alt-J - Tessellate [OFFICIAL VIDEO] - alt-J.mp3"

start_time = time.time()
running = True

def play_sound():
    print("M pressed 😭")
    playsound(SOUND_PATH)

def show_uptime():
    while running:
        uptime = int(time.time() - start_time)
        hours = uptime // 3600
        minutes = (uptime % 3600) // 60
        seconds = uptime % 60
        print(f"\rUptime: {hours:02}:{minutes:02}:{seconds:02}", end="")
        time.sleep(1)

keyboard.add_hotkey("m", play_sound)

print("Press M to play sound. Press ESC to exit.")

# Start uptime thread
thread = threading.Thread(target=show_uptime)
thread.start()

# Wait for ESC to stop
keyboard.wait("esc")
running = False