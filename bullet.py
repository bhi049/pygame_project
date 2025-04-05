import pygame
import os

class Bullet:
    def __init__(self, x, y, direction):
        image_path = os.path.join("assets", "images", "bullets", "bullet_red.png")
        original_image = pygame.image.load(image_path).convert_alpha()
        original_image = pygame.transform.scale(original_image, (20, 20))

        self.direction = direction
        self.image = self.rotate_image(original_image, direction)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 15

    def move(self):
        if self.direction == "UP":
            self.rect.y -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed
        elif self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "RIGHT":
            self.rect.x += self.speed

    def rotate_image(self, image, direction):
        angle_map = {
            "UP": 0,
            "RIGHT": -90,
            "DOWN": 180,
            "LEFT": 90
        }
        angle = angle_map[direction]
        return pygame.transform.rotate(image, angle)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self, width, height):
        return (self.rect.right < 0 or self.rect.left > width or
                self.rect.bottom < 0 or self.rect.top > height)