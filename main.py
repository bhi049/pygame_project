import pygame
import sys
from player import Player # import custom Player class
from bullet import Bullet # import custom Bullet class
from enemy import Enemy # import custom Enemy class

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
# create the enemy object
enemy = Enemy(100, 100)
enemies = [enemy] # list to store enemies

# create a list to store bullets
bullets = []

def direction_to_player(enemy_rect, player_rect):
    dx = player_rect.centerx -enemy_rect.centerx
    dy = player_rect.centery - enemy_rect.centery

    # determine direction based on dx and dy
    dir_x = -1 if dx < -10 else 1 if dx > 10 else 0
    dir_y = -1 if dy < -10 else 1 if dy > 10 else 0

    direction_map = {
        "UP": (0, -1),
        "DOWN": (0, 1),
        "LEFT": (-1, 0),
        "RIGHT": (1, 0),
        "UPRIGHT": (1, -1),
        "UPLEFT": (-1, -1),
        "DOWNRIGHT": (1, 1),
        "DOWNLEFT": (-1, 1)
    }

    return direction_map.get((dir_x, dir_y), "UP")

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
                bullet = Bullet(player.rect.centerx, player.rect.centery, player.direction, owner="player")
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
            continue

        # check for collision with enemies
        for enemy in enemies:
            if bullet.owner == "player" and enemy.is_alive and bullet.rect.colliderect(enemy.rect):
                enemy.take_damage(1)
                bullets.remove(bullet)
                break

        # check for collision with player
        if bullet.owner == "enemy" and player.is_alive and bullet.rect.colliderect(player.rect):
            player.take_damage(1)
            bullets.remove(bullet)

    for enemy in enemies:
        if not enemy.is_alive:
            continue
        # move enemy towards player
        enemy.move_towards_player(player.rect)
        # update enemy shoot timer
        enemy.update_shoot_timer(dt)
        # draw enemy
        enemy.draw(screen)
        # check if enemy can shoot
        if enemy.can_shoot():
            bullet = Bullet(enemy.rect.centerx, enemy.rect.centery, enemy.direction, owner="enemy")
            bullets.append(bullet)
            enemy.reset_shoot_timer()

    pygame.display.flip() # update the display

# quit the game
pygame.quit()
sys.exit()