# pipes.py
import pygame
import random
from settings import (
    WIDTH, HEIGHT,
    PIPE_GAP, PIPE_WIDTH,
    PIPE_SPEED_START, PIPE_SPEED_MAX,
    GREEN
)

class Pipes:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(150, 400)
        self.passed = False
        self.speed = PIPE_SPEED_START

    def update_speed(self, score, is_slow_motion=False):
        # Calculate base speed based on score (Level progression)
        # Increase speed more gradually (every 10 points instead of 8?)
        # Keeping it fair: score // 10
        progression = score // 10
        
        base_speed = min(
            PIPE_SPEED_START + progression,
            PIPE_SPEED_MAX
        )

        # Apply slow motion factor if active
        if is_slow_motion:
            self.speed = base_speed * 0.6 # Run at 60% speed during slow motion
        else:
            self.speed = base_speed

    def move(self):
        self.x -= self.speed
        
        # Reset pipe when it goes off screen
        if self.x < -PIPE_WIDTH:
            self.x = WIDTH
            self.height = random.randint(150, 400)
            self.passed = False

    def draw(self, screen):
        # Top Pipe
        top_pipe = pygame.Rect(
            self.x,
            0,
            PIPE_WIDTH,
            self.height - PIPE_GAP
        )

        # Bottom Pipe
        bottom_pipe = pygame.Rect(
            self.x,
            self.height,
            PIPE_WIDTH,
            HEIGHT
        )

        # Draw pipes
        pygame.draw.rect(screen, GREEN, top_pipe)
        pygame.draw.rect(screen, GREEN, bottom_pipe)
        
        # Draw border for better visuals (optional, keeps it clean)
        pygame.draw.rect(screen, (0, 100, 0), top_pipe, 2)
        pygame.draw.rect(screen, (0, 100, 0), bottom_pipe, 2)

        return top_pipe, bottom_pipe
