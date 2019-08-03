import os

from pygame import draw, image, font
from random import randint
from src.colours import *
from src.directory import *

spider_image = image.load(os.path.join(IMAGE_DIR,"spider.png"))
font.init()

class Spider:

    def __init__(self, difficulty):
        i = randint(1,14) * 40
        j = randint(1,14) * 40
        self.location = [i,j]
        self.alive = False
        self.time = 0
        self.just_consumed = 0
        self.last_score = 0
        self.difficulty = difficulty
        return

    def __generate(self):
        if randint(1,100) > 97:
            self.alive = True
            i = randint(1,14) * 40
            j = randint(1,14) * 40
            self.location = [i,j]
            self.time = randint(50,100)

    def simulate(self):
        if self.alive:
            if self.time == 1:
                self.time = 0
                self.alive = False
            else: 
                self.time -= 1
        else:
            self.__generate()

    def __draw_consumed_popup(self, screen):
        w = self.location[0]-40
        h = self.location[1]-40


    def consumed(self):
        self.alive = False
        self.last_score = self.score()
        self.time = 0
        self.just_consumed = 3

    def draw(self, screen):
        w = self.location[0]-40
        h = self.location[1]-40
        if self.alive:
            screen.blit(spider_image, (w,h))
        else:
            if self.just_consumed > 0 and self.last_score > 0:
                f = font.Font('freesansbold.ttf', 40)
                text = f.render(f"+{self.last_score}", True, GREEN)
                screen.blit(text,(w-20,h))
                self.just_consumed -= 1

    def reset(self):
        self.alive = False
        self.just_consumed = 0
        self.time = 0
        self.last_score = 0

    def score(self):
        score = self.time * self.difficulty / 10
        return(int(score))
