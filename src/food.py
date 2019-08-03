from pygame import draw, image

from random import randint
from src.colours import *
from src.directory import *


food_image = image.load(os.path.join(IMAGE_DIR,"leaf.png"))


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
        w = self.location[0]-40
        h = self.location[1]-40
        screen.blit(food_image, (w,h))
        return


