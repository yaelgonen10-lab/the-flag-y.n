from itertools import count
import consts
import game_field

"""start location saved"""
def save_start_body_loc():
    """saves the solider starting body position in the matrix.
    ([ [0,0], [0,1]
       [1,0], [1,1]
       [2,0], [2,1] ])"""
    body_loc = []
    for row in range(consts.SOLDIER_BODY_ROWS):
        for col in range(consts.SOLDIER_COLS):
            location = [row, col]
            body_loc.append(location)
    return body_loc


def save_start_leg_loc():
    """saves the solider starting leg position in the matrix.
        ([ [3,0], [3,1] ])"""
    leg_loc = []
    for row in range(consts.SOLDIER_FEET_ROWS):
        for col in range(consts.SOLDIER_COLS):
            location = [consts.SOLDIER_BODY_ROWS + row, col]
            leg_loc.append(location)
    return leg_loc


"""update and remove solider locations"""
def update_solider_location(body_loc,leg_loc):
    """updates the soldier's location in the matrix
    if body = s
    if leg = l"""
    for location in body_loc:
        row = location[0]
        col = location[1]
        game_field.matrix_field[row][col] = "s"
    for location in leg_loc:
        row = location[0]
        col = location[1]
        game_field.matrix_field[row][col] = "l"

def remove_solider_location(body_loc,leg_loc):
    """removes the soldier's position from the matrix
    (update to start value 0)"""
    for location in body_loc:
        row = location[0]
        col = location[1]
        game_field.matrix_field[row][col] = "0"
    for location in leg_loc:
        row = location[0]
        col = location[1]
        game_field.matrix_field[row][col] = "0"



"""cheks if win or loss"""
def is_win_reach_the_flag(body_loc):
    """checks whether the player won (the soldier's body reached the flag)"""
    for location in body_loc:
        row = location[0]
        col = location[1]
        if game_field.matrix_field[row][col] == "f":
            return True
    return False

def is_loss_reach_mine(leg_loc):
    """Checks whether the player lost (the soldier's feet reached the mine)"""
    for location in leg_loc:
        row = location[0]
        col = location[1]
        if game_field.matrix_field[row][col] == "x":
            return True
    return False


"""chekes movements requests of solider"""
def is_possible_left(body_loc):
    """checks whether the player can be moved to the left"""
    check_loc = body_loc[0]
    if check_loc[1] == 0:
        return False
    return  True

def is_possible_right(body_loc):
    """checks whether the player can be moved to the right"""
    check_loc = body_loc[1]
    if check_loc[1] == consts.BOARD_COLS - 1:
        return False
    return  True

def is_possible_up(body_loc):
    """checks whether the player can be moved up"""
    check_loc = body_loc[0]
    if check_loc[0] == 0:
        return False
    return True

def is_possible_down(leg_loc):
    """checks whether the player can be moved to the down"""
    check_loc = leg_loc[0]
    if check_loc[0] == consts.BOARD_ROWS - 1:
        return False
    return True


"""moves solider as requested"""
def move_solider_right(body_loc,leg_loc):
    """moves the player right in the matrix"""
    for location in body_loc:
        location[1] += 1
    for location in leg_loc:
        location[1] += 1

def move_solider_left(body_loc,leg_loc):
    """moves the player left in the matrix"""
    for location in body_loc:
        location[1] -= 1
    for location in leg_loc:
        location[1] -= 1

def move_solider_up(body_loc,leg_loc):
    """moves the player up in the matrix"""
    for location in body_loc:
        location[0] -= 1
    for location in leg_loc:
        location[0] -= 1

def move_solider_down(body_loc,leg_loc):
    """moves the player down in the matrix"""
    for location in body_loc:
        location[0] += 1
    for location in leg_loc:
        location[0] += 1

def print_matrix(body_lst):
    for row in body_lst:
        for elem in row:
            print(elem, end=" ")
        print()

body_loc = save_start_body_loc()
leg_loc = save_start_leg_loc()
update_solider_location(body_loc, leg_loc)

print(is_win_reach_the_flag(body_loc))
print(is_loss_reach_mine(leg_loc))
print_matrix(game_field.matrix_field)
print()


remove_solider_location(body_loc, leg_loc)
while (is_possible_right(body_loc)):
    remove_solider_location(body_loc, leg_loc)
    move_solider_right(body_loc, leg_loc)
    update_solider_location(body_loc, leg_loc)


print_matrix(game_field.matrix_field)
