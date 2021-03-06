# sound.py
import time

from pydub import AudioSegment
from pydub.playback import play


class Sound:
    cooldown = -1 # cooldown is off (-1)
    volume = 7
    last_played = 0

    def play(self, path):
        if time.time() > (self.last_played + self.cooldown):
            print(f"Sound {path} was played")
            self._playsound(path)
            self.last_played = time.time()
        else:
            print(f"Sound {path} was not played")

    def _playsound(self, filename):
        if filename.endswith(".mp3"):
            sound = AudioSegment.from_mp3(filename) + self.volume
        elif filename.endswith(".wav"):
            sound = AudioSegment.from_file(filename) + self.volume
        else:
            return
        play(sound)


if __name__ == "__main__":
    s = Sound()

    s.play("sounds/oof.mp3")
