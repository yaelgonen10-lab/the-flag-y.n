START_MESSAGE = 'Welcome to The Flag game.\nHave Fun!'
#--------------------------------------------------------------------------------

BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20 # pixels per cell
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE
#--------------------------------------------------------------------------------

SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3 # the upper part
SOLDIER_FEET_ROWS = 1 # the lower part
#--------------------------------------------------------------------------------

FLAG_ROWS = 3
FLAG_COLS = 4
# game_field.py
flag_row = BOARD_ROWS - FLAG_ROWS
flag_col = BOARD_COLS - FLAG_COLS
#--------------------------------------------------------------------------------

MINES_COUNT = 20
MINE_ROWS = 1
MINE_COLS = 3
#--------------------------------------------------------------------------------

EMPTY = "0"
MINE  = "x"
FLAG  = "f"
FLOWER = 'flower'
#--------------------------------------------------------------------------------
