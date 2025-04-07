import pygame
import os
import math

class Bullet:
    def __init__(self, x, y, direction, owner):
        image_path = os.path.join("assets", "images", "bullets", "bullet_red.png")
        original_image = pygame.image.load(image_path).convert_alpha()
        original_image = pygame.transform.scale(original_image, (20, 20))

        self.direction = direction
        self.image = self.rotate_image(original_image, direction)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 15
        self.dx, self.dy = self.get_normalized_direction(direction)

        self.owner = owner  # reference to the owner (player or enemy)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def rotate_image(self, image, direction):
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
        angle = angle_map[direction]
        return pygame.transform.rotate(image, angle)
    
    def get_normalized_direction(self, direction):
        dir_map = {
            "UP": (0, -1),
            "RIGHT": (1, 0),
            "DOWN": (0, 1),
            "LEFT": (-1, 0),
            "UPRIGHT": (1, -1),
            "UPLEFT": (-1, -1),
            "DOWNRIGHT": (1, 1),
            "DOWNLEFT": (-1, 1)
        }

        dx, dy = dir_map.get(direction, (0, -1))
        lenght = math.hypot(dx, dy)
        if lenght != 0:
            dx = (dx / lenght) * self.speed
            dy = (dy / lenght) * self.speed
        return dx, dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self, width, height):
        return (self.rect.right < 0 or self.rect.left > width or
                self.rect.bottom < 0 or self.rect.top > height)