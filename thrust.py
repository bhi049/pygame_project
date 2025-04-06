import pygame
import os

class Thrust:
    def __init__(self, direction_ref, get_position_func):
        self.frames = []
    
        image_path = os.path.join("assets", "images", "effects", "thrust", "thrust_1.png")
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, (40, 60)) # scale if needed
        self.frames.append(image)

        self.thrust_frame_index = 0
        self.thrust_animation_timer = 0
        self.thrust_animation_speed = 100 # ms per frame adjust if needed
        self.is_active = False
        self.direction_ref = direction_ref # reference to the direction of the player
        self.get_position_func = get_position_func # function to get the position of the player

    def update(self, dt, is_thrusting):
        self.is_active = is_thrusting
        if not self.is_active:
            self.frame_index = 0
            self.animation_timer = 0
            return
                
        self.animation_timer += dt
        if self.animation_timer >= self.animation_timer:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
    
    def draw(self, screen):
        if not self.is_active:
            return

        # Get the current frame and position
        frame = self.frames[self.thrust_frame_index]
        position = self.get_position_func(self.direction_ref())

        # Draw the thrust effect on the screen
        screen.blit(frame, frame.get_rect(center=position))