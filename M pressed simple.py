import keyboard
from playsound import playsound

SOUND_PATH = r"E:\epic games\youtube XL\alt-J - Tessellate [OFFICIAL VIDEO] - alt-J.mp3"

def play_sound():
    print("M pressed 😭")
    playsound(SOUND_PATH)

keyboard.add_hotkey("m", play_sound)

print("Press M to play sound. Press ESC to exit.")
keyboard.wait("esc")