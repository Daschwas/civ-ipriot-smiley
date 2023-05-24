from smiley import Smiley
import time


class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()
        self.draw_eyebrows()

    def draw_mouth(self):
        """
        Method that draws the mouth on the standard faceless smiley.
        """
        mouth = [42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        eyes = [18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def draw_eyebrows(self):
        """
        Method that draws the eyebrows on the standard smiley.
        """
        eyes = [9, 10, 11, 12, 13, 14]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK

    def blink(self):
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(0.25)
        self.draw_eyes(wide_open=True)
        self.show()
