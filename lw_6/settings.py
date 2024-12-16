import math

WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)
FOOTSTEP_COOLDOWN = 0.7

NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = math.pi / 3.0 / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(math.pi / 6.0))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 0.3
player_angle_speed = 0.003
