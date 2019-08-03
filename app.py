import pygame

from src.snake import Snake
from src.food import Food
from src.hud import hud
from src.colours import *

pygame.init()
pygame.font.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")

DIFFICULTY = 10

# Loop until the user clicks the close button.
done = False

clock = pygame.time.Clock()

snake = Snake()
food = Food()
HUD = hud()
 

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not snake.turned:
                snake.left()
            elif event.key == pygame.K_RIGHT and not snake.turned:
                snake.right()
            elif event.key == pygame.K_UP and not snake.turned:
                snake.up()
            elif event.key == pygame.K_DOWN and not snake.turned:
                snake.down()
            elif event.key == pygame.K_q:
                """Restart Game"""
                del snake
                snake = Snake()
                HUD.reset_score()

    screen.fill(WHITE)
    # --- Game logic
    if snake.alive:
        snake.simulate()
        if snake.head_location == food.location:
            snake.eat()
            food.consumed()
            HUD.add_score(DIFFICULTY)
    # --- Drawing
    if snake.alive:
        snake.draw(screen)
        food.draw(screen)
        HUD.draw(screen)
    else:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f"Snake Dead. Score: {HUD.score}", False, RED)
        screen.blit(text,(10,10))
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(DIFFICULTY)

pygame.quit()

