import pygame
import sys





def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if soldier.is_possible_left():
                    soldier.remove_solider_location()
                    soldier.move_solider_left()
                    soldier.update_solider_location(body_loc,leg_loc)


            elif event.key == pygame.K_RIGHT:
                if soldier.is_possible_right():
                    soldier.remove_solider_location()
                    soldier.move_solider_right()
                    soldier.update_solider_location(body_loc, leg_loc)

            elif event.key == pygame.K_UP:
                if soldier.is_possible_up():
                    soldier.remove_solider_location()
                    soldier.move_solider_up()
                    soldier.update_solider_location(body_loc, leg_loc)

            elif event.key == pygame.K_DOWN:
                if soldier.is_possible_down():
                    soldier.remove_solider_location()
                    soldier.move_solider_down()
                    soldier.update_solider_location(body_loc, leg_loc)


            elif event.key == pygame.K_RETURN:
                pass
                #show_screen_with_bumbs()
