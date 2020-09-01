from pynput.keyboard import Key, Listener, Controller

class Soundboard:

    ctrl_held = False
    shift_held = False

    def __init__(self):    
        with Listener(on_press=self._on_press, on_release=self._on_release) as listener:
            listener.join()

    def _on_press(self, key):
        print("{0} pressed".format(key))

        if key == Key.ctrl:
            self.ctrl_held = True
        if key == Key.shift:
            self.shift_held = True


    def _on_release(self, key):
        print("{0} released".format(key))
        
        if key == Key.ctrl:
            self.ctrl_held = False
        if key == Key.shift:
            self.shift_held = False


        if key == Key.esc and self.shift_held: 
            return False # stop the listener

if __name__ == "__main__":
    s = Soundboard()
