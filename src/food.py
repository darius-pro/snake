from pygame import draw

from random import randint
from src.colours import *

class Food:

    def __init__(self):
        i = randint(1,14) * 40
        j = randint(1,14) * 40
        self.location = [i,j]
        return

    def consumed(self):
        i = randint(1,14) * 40
        j = randint(1,14) * 40
        self.location = [i,j]
        return

    def draw(self, screen):
        w = self.location[0] - 20
        h = self.location[1] - 20
        draw.circle(screen, BROWN, (w, h), 20)
        return


