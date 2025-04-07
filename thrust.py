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

        # map diretions to thrust frames
        self.angle_map = {
            "UP": 0,
            "DOWN": 180,
            "RIGHT": -90,
            "LEFT": 90,
            "UPRIGHT": -45,
            "UPLEFT": 45,
            "DOWNRIGHT": -135,
            "DOWNLEFT": 135
        }

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

        # Rotate the frame based on the ships direction
        direction = self.direction_ref()
        angle = self.angle_map.get(direction, 0)
        rotated_frame = pygame.transform.rotate(frame, angle)

        # Draw the thrust effect on the screen
        screen.blit(rotated_frame, rotated_frame.get_rect(center=position))