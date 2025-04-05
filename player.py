import pygame
import os

class Player:
    def __init__(self, x, y):
        # load the ship image
        image_path = os.path.join("assets", "images", "ship.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100)) # scale if needed
        # get the rectangular area for positioning
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # movement speed
        self.speed = 5

    # draw the player image on the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # move the player based on key inputs
    def move(self, keys, screen_width):
        # check for key presses and move the player accordingly
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < screen_width:
            self.rect.y += self.speed