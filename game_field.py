import consts
import random

matrix_field = []

#create field
def create_matrix_field():
    """creates a field of a specified size"""
    for i in range(consts.BOARD_ROWS):
        matrix_field.append(create_line())


def create_line():
    """creates a row in a field"""
    line = []
    for i in range(consts.BOARD_COLS):
        line.append("0")
    return line


#puts flag in mine ("f"...)
def scatter_flag():
    flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
    flag_col = consts.BOARD_COLS - consts.FLAG_COLS
    for i in range(consts.FLAG_ROWS):
        for j in range(consts.FLAG_COLS):
            matrix_field[flag_row + i][flag_col + j] = "f"


#puts mine in field ("x", "X", "x")
def random_loc_mine():
    """finds a random location for a mine within the matrix range"""
    loc_mine_row = random.randint(0, consts.BOARD_ROWS - 1)
    loc_mine_col = random.randint(0, consts.BOARD_COLS - 1 - consts.MINE_COLS)
    location = [loc_mine_row, loc_mine_col]
    return location

def is_possible_mine(location):
    """checks whether the mine can be placed (makes sure there is space between the mines or flag place)"""
    row = location[0]
    col = location[1]
    if col == 0:
        pass
    elif matrix_field[row][col - 1] == "x":
        return False
    for i in range(consts.MINE_COLS + 1):
            if matrix_field[row][col + i] == "x" or\
                matrix_field[row][col + i] == "f":
                return False
    return True

def scatter_mines():
    """randomly places mines according to the set quantity."""
    count = 0
    while count < consts.MINES_COUNT:
        location = random_loc_mine()
        if is_possible_mine(location):
            in_mine(location)
            count += 1


def in_mine(location):
    """puts the mine in matrix_field"""
    row = location[0]
    col = location[1]
    for i in range(consts.MINE_COLS):
        matrix_field[row][col + i] = "x"




def print_matrix():
    for row in matrix_field:
        for elem in row:
            print(elem, end=" ")
        print()

create_matrix_field()
scatter_mines()
scatter_flag()
print_matrix()

