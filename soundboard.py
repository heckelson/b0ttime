# soundboard.py
from sound import Sound

from pynput.keyboard import Key, Listener, Controller

class Soundboard:

    ctrl_held  = False
    shift_held = False
    alt_held   = False

    sound = Sound()

    def __init__(self):    
        with Listener(on_press=self._on_press, on_release=self._on_release) as listener:
            listener.join()
            

    def _on_press(self, key):
        print("{} pressed".format(key))

        if key == Key.ctrl:
            self.ctrl_held = True
        if key == Key.shift:
            self.shift_held = True
        if key == Key.alt:
            self.alt_held = True

    def _on_release(self, key):
        print("{} released".format(key))
        
        if key == Key.ctrl:
            self.ctrl_held = False
        if key == Key.shift:
            self.shift_held = False
        if key == Key.alt:
            self.alt_held = False

        # if something:       
        #     self.sound.play("sounds/alert.mp3")



        if key == Key.esc and self.shift_held: 
            return False # stop the listener

if __name__ == "__main__":
    s = Soundboard()

