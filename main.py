import pygame
import sys
from player import Player # import custom Player class

# initialize Pygame
pygame.init()

# set up the display window size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Window")

# set up clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# create the player object
player = Player(WIDTH // 2, HEIGHT - 60)

# main game loop
running = True
while running:
    clock.tick(FPS) # limit the loop to FPS

    # handle events (like quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # handle key presses
    keys = pygame.key.get_pressed()
    player.move(keys, WIDTH, HEIGHT) # move the player based on key input

    # clear the screen and draw everything
    screen.fill(WHITE)
    player.draw(screen)
    pygame.display.flip() # update the display

# quit the game
pygame.quit()
sys.exit()