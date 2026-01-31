# settings.py

WIDTH = 400
HEIGHT = 600
FPS = 60

# Bird physics - FLIGHT TUNING
# Reduced gravity for a floatier, easier feel (was 0.5)
GRAVITY = 0.25  
# Reduced jump strength to match lower gravity (was -8)
JUMP_STRENGTH = -5.5

# Pipes - OBSTACLE TUNING
# Increased gap to make passing pipes easier (was 170)
PIPE_GAP = 200  
PIPE_WIDTH = 80

# Pipe Speed
# Starting speed (slow motion will reduce this further at start)
PIPE_SPEED_START = 3  
# Reduced max speed prevents it from becoming impossible (was 8)
PIPE_SPEED_MAX = 6    

# New Features
SLOW_MOTION_DURATION = 3.0  # Seconds of slow motion at start

# Colors
SKY_BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
