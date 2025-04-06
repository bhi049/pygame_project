import pygame
import os

class Player:
    def __init__(self, x, y):
        # load the ship image
        image_path = os.path.join("assets", "images", "ship.png")
        original = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(original, (100,100)) # scale if needed
        self.image = self.original_image # current image used for drawing
        # get the rectangular area for positioning
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # movement speed
        self.speed = 5
        # initial direction
        self.direction = "UP"
        # initial rotation
        self.rotate()

    # draw the player image on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # move the player based on key inputs
    def move(self, keys, screen_width, screen_height):
        moved = False

        # check for key presses and move the player accordingly
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
            self.direction = "UP"
            moved = True

        if keys[pygame.K_s] and self.rect.bottom < screen_height:
            self.rect.y += self.speed
            self.direction = "DOWN"
            moved = True

        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = "LEFT"
            moved = True

        if keys[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = "RIGHT"
            moved = True

        # check for diagonal movement
        if keys[pygame.K_w] and keys[pygame.K_d]:
            self.rect.x += self.speed
            self.rect.y -= self.speed
            self.direction = "UPRIGHT"
            moved = True

        if keys[pygame.K_w] and keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
            self.direction = "UPLEFT"
            moved = True

        if keys[pygame.K_s] and keys[pygame.K_d]:
            self.rect.x += self.speed
            self.rect.y += self.speed
            self.direction = "DOWNRIGHT"
            moved = True

        if keys[pygame.K_s] and keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.rect.y += self.speed
            self.direction = "DOWNLEFT"
            moved = True

        if moved:
            self.rotate()

    def rotate(self):
        # determine angle based on direction
        angle_map = {
            "UP": 0,
            "RIGHT": -90,
            "DOWN": 180,
            "LEFT": 90,
            "UPRIGHT": -45,
            "UPLEFT": 45,
            "DOWNRIGHT": -135,
            "DOWNLEFT": 135
        }

        # rotate the image
        angle = angle_map[self.direction]
        # rotate the original image
        self.image = pygame.transform.rotate(self.original_image, angle)
        # keep position centered
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)