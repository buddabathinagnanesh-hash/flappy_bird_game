# main.py
import pygame
import sys
import time

from settings import (
    WIDTH, HEIGHT, FPS,
    SKY_BLUE, WHITE, BLACK, YELLOW, PIPE_WIDTH,
    SLOW_MOTION_DURATION
)
from bird import Bird
from pipes import Pipes

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird - Advanced Edition")

clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("arial", 24, bold=True)       
big_font = pygame.font.SysFont("arial", 50, bold=True)   
popup_font = pygame.font.SysFont("arial", 40, bold=True) 
stats_font = pygame.font.SysFont("arial", 30, bold=True) 

def draw_text(text, font, color, x, y, shadow=True, center=True):
    if shadow:
        shadow_surface = font.render(text, True, BLACK)
        if center:
            shadow_rect = shadow_surface.get_rect(center=(x + 2, y + 2))
        else:
            shadow_rect = shadow_surface.get_rect(topleft=(x + 2, y + 2))
        screen.blit(shadow_surface, shadow_rect)
    
    surface = font.render(text, True, color)
    if center:
        rect = surface.get_rect(center=(x, y))
    else:
        rect = surface.get_rect(topleft=(x, y))
    screen.blit(surface, rect)

def get_level(score):
    if score < 5:
        return 1
    elif score < 15:
        return 2
    else:
        return 3

def reset_game():
    return Bird(), Pipes(), 0

# -------- GAME STATES --------
START = "start"
PLAYING = "playing"
GAME_OVER = "game_over"

game_state = START
paused = False

bird, pipes, score = reset_game()

current_level = 1
show_level_popup = False
popup_start_time = 0

high_score = 0 
start_time = 0 

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            # GLOBAL PAUSE
            if event.key == pygame.K_p and game_state == PLAYING:
                paused = not paused

            # START SCREEN
            elif game_state == START and event.key == pygame.K_SPACE:
                bird, pipes, score = reset_game()
                current_level = 1
                game_state = PLAYING
                paused = False
                start_time = time.time()

            # PLAYING
            elif game_state == PLAYING and not paused:
                if event.key == pygame.K_SPACE:
                    bird.jump()

            # GAME OVER
            elif game_state == GAME_OVER:
                if event.key == pygame.K_r:
                    bird, pipes, score = reset_game()
                    current_level = 1
                    game_state = PLAYING
                    paused = False
                    start_time = time.time()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    # -------- GAME LOGIC --------
    if game_state == PLAYING and not paused:
        elapsed = time.time() - start_time
        is_slow_motion = elapsed < SLOW_MOTION_DURATION
        
        bird.update()
        
        pipes.update_speed(score, is_slow_motion)
        pipes.move()

        if pipes.x + PIPE_WIDTH < bird.x and not pipes.passed:
            score += 1
            pipes.passed = True

        new_level = get_level(score)
        if new_level != current_level:
            current_level = new_level
            show_level_popup = True
            popup_start_time = time.time()

        # Check collisions (Logic only!)
        # Pass a temporary surface or dummy check if draw() is required for hitboxes.
        # But 'pipes.draw' actually RETURNS the rects we need. 
        # This is a bit of a coupling issue in the original code structure, 
        # but we can fix it by calling draw logically but not blitting, or just allowing the blit 
        # since we will overwrite the screen in the DRAW phase anyway? 
        # NO. We must separate Logic and Draw.
        # However, to be safe and simple: We will do the logic check here.
        # We will allow it to draw to screen here (wastefully) because we clear screen immediately below.
        top_pipe, bottom_pipe = pipes.draw(screen) 
        
        # NOTE: The above draw calls happens BEFORE screen.fill in the loop? 
        # Wait, the structure is:
        # while running:
        #   events...
        #   logic...
        #   screen.fill...
        #   draw...
        #
        # If I call pipes.draw(screen) in Logic, it draws to the buffer.
        # Then screen.fill(SKY_BLUE) happens in Drawing Phase, wiping it out.
        # So it effectively does NOT show up. This works for Logic-Draw separation!

        if (
            bird.get_rect().colliderect(top_pipe)
            or bird.get_rect().colliderect(bottom_pipe)
            or bird.y <= 0
            or bird.y >= HEIGHT
        ):
            game_state = GAME_OVER
            if score > high_score:
                high_score = score

    # -------- DRAWING PHASE --------
    # 1. Background (Always draw first to clear previous frame)
    screen.fill(SKY_BLUE)

    # 2. State-Specific Drawing
    if game_state == START:
        # Optional: could draw bird/pipes for aesthetics, but user wants clean.
        # We'll just keep it text based or maybe just bird. 
        # Let's keep it simple as per request.
        draw_text("FLAPPY BIRD", big_font, WHITE, WIDTH // 2, HEIGHT // 2 - 60)
        draw_text("Press SPACE to Start", font, WHITE, WIDTH // 2, HEIGHT // 2 + 10)
        draw_text(f"High Score: {high_score}", font, WHITE, WIDTH // 2, HEIGHT // 2 + 60)
        draw_text("v2.2 Clean Render", popup_font, YELLOW, WIDTH // 2, HEIGHT - 50)

    elif game_state == PLAYING:
        # Draw World
        pipes.draw(screen)
        bird.draw(screen)
        
        # HUD
        draw_text(f"Score: {score}", font, WHITE, WIDTH // 2, 30)
        draw_text(f"Level: {current_level}", font, WHITE, WIDTH // 2, 60)

        # Effects
        if not paused and (time.time() - start_time < SLOW_MOTION_DURATION):
             draw_text("SLOW MOTION START!", font, YELLOW, WIDTH // 2, HEIGHT // 2 - 120)

        if show_level_popup:
            draw_text(f"LEVEL {current_level}!", popup_font, YELLOW, WIDTH // 2, HEIGHT // 2)
            if time.time() - popup_start_time > 2:
                show_level_popup = False
        
        # Pause Overlay
        if paused:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            screen.blit(overlay, (0,0))
            
            draw_text("PAUSED", big_font, WHITE, WIDTH // 2, HEIGHT // 2)
            draw_text("Press P to Resume", font, WHITE, WIDTH // 2, HEIGHT // 2 + 50)

    elif game_state == GAME_OVER:
        # STRICT REQUIREMENT: NO PIPES, NO BIRD.
        # Just background (already filled) and UI.
        
        # Optional dark overlay strictly for visual separation even without pipes
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(100) # Lighter overlay since background is just blue
        overlay.fill(BLACK)
        screen.blit(overlay, (0,0))

        center_y = HEIGHT // 2
        
        draw_text("GAME OVER", big_font, (255, 80, 80), WIDTH // 2, center_y - 80)
        
        # Stats
        draw_text(f"Score: {score}", stats_font, WHITE, WIDTH // 2, center_y - 10)
        draw_text(f"Best: {high_score}", stats_font, YELLOW, WIDTH // 2, center_y + 30)
        draw_text(f"Level: {current_level}", stats_font, WHITE, WIDTH // 2, center_y + 70)
        
        # Controls
        draw_text("Press R to Restart", font, WHITE, WIDTH // 2, center_y + 130)
        draw_text("Press ESC to Quit", font, WHITE, WIDTH // 2, center_y + 160)

    # 3. Final Flip
    pygame.display.update()

pygame.quit()
