import pygame
import os
import math

class Enemy:
    def __init__(self, x, y):
        image_path = os.path.join("assets", "images", "ships", "enemy_1.png" )
        original = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(original, (100, 100)) # scale if needed
        self.rect = self.image.get_rect(center=(x, y))
        
        self.speed = 2
        self.shoot_cooldown = 1000  # shot delay (ms)
        self.since_last_shot = 0

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
    
    def update_shoot_timer(self, dt):
        self.since_last_shot += dt
    
    def can_shoot(self):
        return self.since_last_shot >= self.shoot_cooldown
    
    def reset_shoot_timer(self):
        self.since_last_shot = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)