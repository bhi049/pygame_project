import pygame
import os
import math

class Enemy:
    def __init__(self, x, y):
        image_path = os.path.join("assets", "images", "ships", "enemy_1.png" )
        original = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(original, (100, 100)) # scale if needed
        self.image = self.original_image # original image
        self.rect = self.image.get_rect(center=(x, y))
        
        self.speed = 2
        self.shoot_cooldown = 1000  # shot delay (ms)
        self.since_last_shot = 0
        self.direction = "UP"

    def move_towards_player(self, player_rect):
        # calculate the direction vector towards the player
        dx = player_rect.centerx - self.rect.centerx
        dy = player_rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)

        if distance != 0:
            dx /= distance
            dy /= distance

            # move enemy towards the player
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

            # update the direction based on the movement
            self.direction = self.get_direction_from_vector(dx, dy)
            self.rotate()

    def get_direction_from_vector(self, dx, dy):
        dir_x = -1 if dx < -0.5 else 1 if dx > 0.5 else 0
        dir_y = -1 if dy < -0.5 else 1 if dy > 0.5 else 0

        direction_map = {
            (0, -1): "UP",
            (0, 1): "DOWN",
            (-1, 0): "LEFT",
            (1, 0): "RIGHT",
            (1, -1): "UPRIGHT",
            (-1, -1): "UPLEFT",
            (1, 1): "DOWNRIGHT",
            (-1, 1): "DOWNLEFT"
        }

        return direction_map.get((dir_x, dir_y), self.direction)

    
    def rotate(self):
        # Rotate the image based on the direction
        angle_map = {
            "UP": 0,
            "DOWN": 180,
            "RIGHT": -90,
            "LEFT": 90,
            "UPRIGHT": -45,
            "UPLEFT": 45,
            "DOWNRIGHT": -135,
            "DOWNLEFT": 135
        }
        angle = angle_map.get(self.direction, 0)
        # Rotate the original image
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update_shoot_timer(self, dt):
        self.since_last_shot += dt
    
    def can_shoot(self):
        return self.since_last_shot >= self.shoot_cooldown
    
    def reset_shoot_timer(self):
        self.since_last_shot = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)