import pygame

from src.colours import *

class hud:

    def __init__(self):
        self.score = 0

    def draw(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 18)
        text = font.render(f"Score: {self.score}", True, RED)
        screen.blit(text,(500,580))

    def reset_score(self):
        self.score = 0

    def add_score(self, score):
        self.score += score