# bird.py
import pygame
from settings import GRAVITY, JUMP_STRENGTH

class Bird:
    def __init__(self):
        self.x = 60
        self.y = 300
        self.velocity = 0

        # Load and scale bird
        # Ensuring bird visual size matches its hitbox reasonably well
        self.original_image = pygame.image.load("bird.png")
        self.original_image = pygame.transform.scale(self.original_image, (60, 45))
        self.image = self.original_image

        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.angle = 0

    def jump(self):
        # Consistent jump velocity
        self.velocity = JUMP_STRENGTH

    def update(self):
        # Apply physics
        self.velocity += GRAVITY
        self.y += self.velocity

        # Smooth Rotation Logic
        # Calculate target angle based on velocity
        # Cap rotation to -25 (up) and 25 (down) for subtle effect
        target_angle = max(-25, min(25, -self.velocity * 3))
        
        # Linear interpolation (Lerp) for smooth transition
        # 0.15 factor makes the rotation lag slightly behind movement, feeling more organic
        self.angle += (target_angle - self.angle) * 0.15
        
        # Apply rotation
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, int(self.y)))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect
