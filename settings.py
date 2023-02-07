import pygame as pg

# Display settings
WIDTH = 750
HEIGHT = 750
FPS = 60
TITLE = 'Timbiriche'

# Board settings
BOARD_X = 100
BOARD_Y = 100
DOTS_PER_ROW = 10
ROWS = 10
DISTANCE_BETWEEN_DOTS = 50
WIDTH_LINE = 5
TEXT_SIZE = 30
TEXT_Y = 700
TURN_INFO_X = 375
SCORE_A_X = 150
SCORE_B_X = HEIGHT - SCORE_A_X

# Dots settings
RADIUS = 5

# Mouse settings
MOUSE_RECT_WIDTH = 5
MOUSE_RECT_HEIGHT = 5

DIRECTIONS = [(-1,0),(0,1),(1,0),(0,-1)]

# Font
font_name = pg.font.match_font('arial')

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (128,128,128)
GREEN = (0,255,0)
PLAYER_A_COLOR = (230,230,250)
PLAYER_A_LINE_COLOR = (105, 0, 168)

PLAYER_B_COLOR = (224,255,255)
PLAYER_B_LINE_COLOR = (127,255,212)
