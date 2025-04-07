import pygame
import os
import math
from thrust import Thrust

class Player:
    def __init__(self, x, y):
        # load the ship image
        image_path = os.path.join("assets", "images", "ships", "player_ship.png")
        original = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(original, (100,100)) # scale if needed
        self.image = self.original_image # current image used for drawing
        # get the rectangular area for positioning
        self.rect = self.image.get_rect()
        self.rect.center = (x, y) 
        # initial direction
        self.direction = "UP"
        # initial rotation
        self.rotate()
        # movement
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.5
        self.friction = 0.1
        self.max_speed = 8

        self.thrust = Thrust(
        direction_ref=lambda: self.direction,
        get_position_func=self.get_thrust_position
)


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
    
    def get_thrust_position(self, direction):
        # position of the thrust effect based on the direction
        offset_map = {
            "UP": (0, 25),
            "DOWN": (0, -25),
            "LEFT": (25, 0),
            "RIGHT": (-25, 0),
            "UPRIGHT": (-18, 18),
            "UPLEFT": (18, 18),
            "DOWNRIGHT": (-18, -18),
            "DOWNLEFT": (18, -18)
        }

        offset = offset_map.get(direction, (0, 50))
        return (self.rect.centerx + offset[0], self.rect.centery + offset[1])


    # move the player based on key inputs
    def move(self, keys, screen_width, screen_height):
        dx, dy = 0, 0

        # check for input and move the player accordingly
        if keys[pygame.K_w]:
            dy = -1

        if keys[pygame.K_s]:
            dy = 1

        if keys[pygame.K_a]:
            dx = -1

        if keys[pygame.K_d]:
            dx = 1

        self.is_thrusting = (dx != 0 or dy != 0)

        # update direction based on input
        if dx != 0 or dy != 0:
            self.direction = self.get_direction_from_vector(dx, dy)
            self.rotate()

            # normalize the direction vector
            length = math.hypot(dx, dy)
            dx /= length
            dy /= length

            self.velocity_x += dx * self.acceleration
            self.velocity_y += dy * self.acceleration
        else:
            # apply friction if no movement
            if self.velocity_x > 0:
                self.velocity_x = max(0, self.velocity_x - self.friction)
            elif self.velocity_x < 0:
                self.velocity_x = min(0, self.velocity_x + self.friction)

            if self.velocity_y > 0:
                self.velocity_y = max(0, self.velocity_y - self.friction)
            elif self.velocity_y < 0:
                self.velocity_y = min(0, self.velocity_y + self.friction) 
        
        # limit speed
        speed = math.hypot(self.velocity_x, self.velocity_y)
        if speed > self.max_speed:
            scale = self.max_speed / speed
            self.velocity_x *= scale
            self.velocity_y *= scale

        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # keep player within screen bounds
        self.rect.clamp_ip(pygame.Rect(0, 0, screen_width, screen_height))

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

    def draw(self, screen):
        self.thrust.draw(screen)
        screen.blit(self.image, self.rect)