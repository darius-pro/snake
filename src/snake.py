from pygame import Surface, draw

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
        self.turned = False

    def __draw_body(self ,screen):
        surf = Surface((40, 40))
        surf.fill(BLACK)
        rect = surf.get_rect()
        for i, val in enumerate(self.snake_matrix):
            for j, val2 in enumerate(self.snake_matrix[i]):
                if self.snake_matrix[i][j] > 0:
                    w = i * 40
                    h = j * 40
                    screen.blit(surf, (w, h))

    def __draw_eyes(self, screen):
        eye_colour = WHITE
        eye_radius = 4
        if self.direction in ["left", "right"]:
            center1 = (self.head_location[0]-20,self.head_location[1]+15-40)
            center2 = (self.head_location[0]-20, self.head_location[1]+25-40)
            draw.circle(screen, eye_colour, center1, eye_radius)
            draw.circle(screen, eye_colour, center2, eye_radius)
        if self.direction in ["up", "down"]:
            center1 = (self.head_location[0]-40+15,self.head_location[1]-20)
            center2 = (self.head_location[0]-40+25, self.head_location[1]-20)
            draw.circle(screen, eye_colour, center1, eye_radius)
            draw.circle(screen, eye_colour, center2, eye_radius)

    def draw(self, screen):
        self.__draw_body(screen)
        self.__draw_eyes(screen)

    # Change snake direction
    def right(self):
        if not self.direction == "left" and not self.turned:
            self.direction = "right"
            self.turned = True

    def left(self):
        if not self.direction == "right" and not self.turned:
            self.direction = "left"
            self.turned = True

    def up(self):
        if not self.direction == "down" and not self.turned:
            self.direction = "up"
            self.turned = True

    def down(self):
        if not self.direction == "up" and not self.turned:
            self.direction = "down"
            self.turned = True

    # Simulate snake process
    def __collision_check(self):
        for i, val in enumerate(self.snake_matrix):
            for j, val2 in enumerate(self.snake_matrix[i]):
                if self.head_location == [(i+1)*40, (j+1)*40] and (0 < self.snake_matrix[i][j] < self.length):
                    return True
        return False

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
        i = self.head_location[0]/40 - 1
        j = self.head_location[1]/40 - 1

        # Check for collisions
        if self.__collision_check():
            self.alive = False

        # Check within box
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
        self.turned = False

    def eat(self):
        self.length += 1



