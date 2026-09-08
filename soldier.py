from itertools import count

import consts


def create_solider_body():
    body_lst = []
    for i in range(consts.SOLDIER_BODY_ROWS):
        body_lst.append([])
        for j in range(consts.SOLDIER_COLS):
            body_lst[i].append("s")
    return body_lst

def start_lst_loc_body_solider():



def print_matrix(body_lst):
    for row in body_lst:
        for elem in row:
            print(elem, end=" ")
        print()

def create_solider_feet():
    feet_lst = []
    for i in range(consts.SOLDIER_FEET_ROWS):
        for j in range(consts.SOLDIER_COLS):
            feet_lst.append("f")
    return feet_lst

create_solider_body()
create_solider_feet()
print_matrix(create_solider_body())
print_matrix(create_solider_feet())