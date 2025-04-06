import pygame
import os

class Player:
    def __init__(self, x, y):
        # load the ship image
        image_path = os.path.join("assets", "images", "ships", "ship.png")
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

    def get_direction_from_vector(self, dx, dy):
        if dx == 0 and dy == -1:
            return "UP"
        if dx == 0 and dy == 1:
            return "DOWN"
        if dx == -1 and dy == 0:
            return "LEFT"
        if dx == 1 and dy == 0:
            return "RIGHT"
        if dx == -1 and dy == -1:
            return "UPLEFT"
        if dx == 1 and dy == -1:
            return "UPRIGHT"
        if dx == -1 and dy == 1:
            return "DOWNLEFT"
        if dx == 1 and dy == 1:
            return "DOWNRIGHT"
        
        return self.direction

    # move the player based on key inputs
    def move(self, keys, screen_width, screen_height):
        dx, dy = 0, 0

        # check for key presses and move the player accordingly
        if keys[pygame.K_w]:
            dy = -1

        if keys[pygame.K_s]:
            dy = 1

        if keys[pygame.K_a]:
            dx = -1

        if keys[pygame.K_d]:
            dx = 1

        if dx != 0 or dy != 0:
            self.direction = self.get_direction_from_vector(dx, dy)
            self.rotate()

            new_x = self.rect.x + (dx * self.speed)
            new_y = self.rect.y + (dy * self.speed)
            
            if 0 < new_x < screen_width - self.rect.width:
                self.rect.x = new_x
            if 0 < new_y < screen_height - self.rect.height:
                self.rect.y = new_y 

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