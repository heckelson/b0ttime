# soundboard.py
from pynput import keyboard

from sound import Sound

class Soundboard:
    
    so = Sound()

    def __init__(self):    
        with keyboard.GlobalHotKeys({
            '<ctrl>+f': self.play_sound
            }) as k:
            k.join()

    def play_sound(self):
        self.so.play("sounds/{}.mp3".format("alert"))

    
if __name__ == "__main__":
    s = Soundboard()
