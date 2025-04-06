import pygame
import sys
from player import Player # import custom Player class
from bullet import Bullet # import custom Bullet class

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

# create a list to store bullets
bullets = []

# main game loop
running = True
while running:
    clock.tick(FPS) # limit the loop to FPS

    # handle events (like quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                bullet = Bullet(player.rect.centerx, player.rect.centery, player.direction)
                bullets.append(bullet)

    # handle key presses
    keys = pygame.key.get_pressed()
    player.move(keys, WIDTH, HEIGHT) # move the player based on key input

    dt = clock.get_time() # delta time for animation
    player.thrust.update(dt, player.is_thrusting) # update thrust animation

    # clear the screen and draw everything
    screen.fill(WHITE)
    player.draw(screen)

    # update and draw bullets
    for bullet in bullets[:]:
        bullet.move()
        bullet.draw(screen)
        # check if bullet is off screen and remove it if so
        if bullet.is_off_screen(WIDTH, HEIGHT):
            bullets.remove(bullet)

    pygame.display.flip() # update the display

# quit the game
pygame.quit()
sys.exit()