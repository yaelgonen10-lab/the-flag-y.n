from itertools import count

import consts

import consts
import game_field


def save_start_body_loc():
    body_loc = []
    for row in range(consts.SOLDIER_BODY_ROWS):
        for col in range(consts.SOLDIER_COLS):
            location = [row, col]
            body_loc.append(location)
    return body_loc


def save_start_leg_loc():
    leg_loc = []
    for row in range(consts.SOLDIER_FEET_ROWS):
        for col in range(consts.SOLDIER_COLS):
            location = [consts.SOLDIER_BODY_ROWS + row, col]
            leg_loc.append(location)
    return leg_loc



def print_matrix(body_lst):
    for row in body_lst:
        for elem in row:
            print(elem, end=" ")
        print()

def is_reach_the_flag(body_loc):
    for location in body_loc:
        row = location[0]
        col = location[1]
        if game_field.matrix_field[row][col] == "f":
            return True
    return False



save_start_body_loc()
save_start_leg_loc()
