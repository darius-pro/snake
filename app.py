import pygame

from src.snake import Snake
from src.food import Food
from src.hud import hud
from src.spider import Spider
from src.colours import *

pygame.init()
pygame.font.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")

DIFFICULTY = 7

# Loop until the user clicks the close button.
done = False

clock = pygame.time.Clock()

snake = Snake()
food = Food()
HUD = hud()
spider = Spider(DIFFICULTY)

session_high_score = 0 

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
                spider.reset()

    screen.fill(WHITE)
    # --- Game logic
    if snake.alive:
        snake.simulate()
        spider.simulate()
        if snake.head_location == food.location:
            snake.eat()
            food.consumed()
            HUD.add_score(DIFFICULTY)
        if snake.head_location == spider.location:
            HUD.add_score(spider.score())
            snake.eat()
            spider.consumed()
            
    # --- Drawing
    if snake.alive:
        food.draw(screen)
        snake.draw(screen)
        spider.draw(screen)
        HUD.draw(screen)      
    else:
        session_high_score = HUD.score if HUD.score > session_high_score else session_high_score
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f"Snake Dead. Score: {HUD.score}", True, RED)
        text2 = font.render(f"Best Score: {session_high_score}", True, RED)
        screen.blit(text,(10,10))
        screen.blit(text2,(10,60))
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(DIFFICULTY)

pygame.quit()

