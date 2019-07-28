import pygame

from src.colours import *

class hud:

    def __init__(self):
        self.score = 1

    def draw(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render(f"Score: {self.score}", False, RED)
        screen.blit(text,(520,580))

    def set_score(self, score):
        self.score = score