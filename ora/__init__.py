import time
from itertools import cycle
import threading
from ora.spinners import Spinner
from colorama import Fore

__all__ = ['Ora', "Spinner"]


class Ora:
    def __init__(self, spinner: Spinner) -> None:
        self.frames = cycle(spinner.value.symbols)
        self.interval = 0.001 * spinner.value.interval  # ms to second
        self._screen_lock = threading.Lock()

        self._text = "loading"
        self._color = Fore.WHITE
        self._spinning = False

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, txt):
        self._text = txt

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, clr):
        self._color = clr

    def isSpinning(self):
        return self._spinning

    def spin(self):
        self._spinning = True
        time.sleep(self.interval)
        self._screen_lock.acquire()
        self._stop_flag = False

        def inner(ora: Ora):
            while ora._stop_flag is False:
                print(
                    f"\r{ora.color}{next(ora.frames)}{Fore.WHITE} {ora.text}", end="")
                time.sleep(ora.interval)

            ora._screen_lock.release()
            ora._spinning = False

        thread = threading.Thread(
            target=inner, args=(self,), daemon=True)
        thread.start()

    def stop(self):
        self._stop_flag = True
        print("\r", end="")
