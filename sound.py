# sound.py
import time
import logging
import contextlib, io

from pydub import AudioSegment
from pydub.playback import play as pydub_play

logging.basicConfig(level=logging.INFO)

class Sound:
    cooldown = -1 # cooldown is off (-1)
    volume = 7
    last_played = 0

    def play(self, path):
        if time.time() > (self.last_played + self.cooldown):
            logging.info(f"Sound {path} was played")
            self._playsound(path)
            self.last_played = time.time()
        else:
            logging.warn(f"Sound {path} was not played")

    def _playsound(self, filename):
        if filename.endswith(".mp3"):
            sound = AudioSegment.from_mp3(filename) + self.volume
        elif filename.endswith(".wav"):
            sound = AudioSegment.from_file(filename) + self.volume
        else:
            logger.warning("Sound file format not supported.")
            return

        pydub_play(sound)

    def is_on_cooldown(self):
        return time.time() <= (self.last_played + self.cooldown)


if __name__ == "__main__":
    s = Sound()
    s.play("sounds/oof.mp3")
