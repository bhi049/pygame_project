import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Window")

# clock and FPS
clock = pygame.time.Clock()
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_pos = [100, 100]
player_size = 50
player_speed = 5

# Main loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos[0] -= player_speed
    if keys[pygame.K_d]:
        player_pos[0] += player_speed
    if keys[pygame.K_w]:
        player_pos[1] -= player_speed
    if keys[pygame.K_s]:
        player_pos[1] += player_speed

    # draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (*player_pos, player_size, player_size))
    pygame.display.flip()

# qiut
pygame.quit()
sys.exit()