import pygame

from random import randint
from src.colours import *

class Food:

    def __init__(self, size = 1):
        self.size = size
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
        pygame.draw.circle(screen, BROWN, (w, h), 20)
        return


