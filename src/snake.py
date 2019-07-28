import pygame

from src.colours import *


def location_start():
    """Return start matrix"""
    matrix = []
    for i in range(15):
        matrix.append([0 for x in range(15)])
    matrix[7][7] = 1
    return matrix


class Snake:

    def __init__(self):
        self.alive = True
        self.direction = "left"
        self.length = 1
        self.head_location = [280,280]
        self.snake_matrix = location_start()

    def draw(self ,screen):
        surf = pygame.Surface((40, 40))
        surf.fill(BLACK)
        rect = surf.get_rect()
        for i, val in enumerate(self.snake_matrix):
            for j, val2 in enumerate(self.snake_matrix[i]):
                if self.snake_matrix[i][j] > 0:
                    w = i * 40
                    h = j * 40
                    screen.blit(surf, (w, h))

    # Change snake direction
    def right(self):
        self.direction = "right"

    def left(self):
        self.direction = "left"

    def up(self):
        self.direction = "up"

    def down(self):
        self.direction = "down"

    # Simulate snake process
    def __move_head(self):
        """Add direction to the matrix"""
        if self.direction == "left":
            self.head_location[0]-=40
        elif self.direction == "right":
            self.head_location[0]+=40
        elif self.direction == "up":
            self.head_location[1]-=40
        elif self.direction == "down":
            self.head_location[1]+=40
        i : int = self.head_location[0]/40 - 1
        j : int = self.head_location[1]/40 - 1
        if (0 <= i < 15) and (0 <= j < 15):
            self.snake_matrix[int(i)][int(j)] += self.length
        else:
            self.alive = False

    def __move_body(self):
        for i, val in enumerate(self.snake_matrix):
            for j, val2 in enumerate(self.snake_matrix[i]):
                if self.snake_matrix[i][j] > 0:
                    self.snake_matrix[i][j] -= 1 


    def simulate(self):

        self.__move_body()
        self.__move_head()
        

    def eat(self):
        self.length += 1
