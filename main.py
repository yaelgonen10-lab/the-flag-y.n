import pygame
import sys
import screen
import game_field
import soldier

def main():
    """מאתחל את המשחק ומריץ את הלולאה הראשית עד לסגירה."""
    screen.init_game()
    clock = pygame.time.Clock()
    #creates the game matrix with flag and mines
    game_field.create_matrix_field()
    game_field.scatter_flag()
    loc_mines = game_field.scatter_mines() #נועה- למקם את תמונות הפצצות לפי loc_mines
    #places and saves the soldier's position in the matrix
    body_loc = soldier.save_start_body_loc()
    leg_loc =soldier.save_start_leg_loc()# חייל בפינה השמאלית-עליונה
    soldier.update_solider_location(body_loc, leg_loc)

    game = {
        "state": consts.STATE_PLAY,
        "since": 0,
        "running": True,
    }

    while game["running"]:
        handle_user_events(body_loc, leg_loc)
        #נועה- לעדכן את מצב המשחק, לצייר בהתאם את המסך, להציג בהתאם את המסך
        """update(game)
        draw(game)
        screen.update_display()
        #שעון?
        clock.tick(consts.FPS)"""

    pygame.quit()
    sys.exit()


def handle_user_events(body_loc, leg_loc):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        #אי אפשר לזוז אם מצב חשיפה
        #elif event.type == pygame.KEYDOWN and game["state"] == consts.STATE_PLAY:
        #if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if soldier.is_possible_left(body_loc):
                    soldier.remove_solider_location(body_loc,leg_loc)
                    soldier.move_solider_left(body_loc,leg_loc)
                    soldier.update_solider_location(body_loc,leg_loc)


            elif event.key == pygame.K_RIGHT:
                if soldier.is_possible_right(body_loc):
                    soldier.remove_solider_location(body_loc,leg_loc)
                    soldier.move_solider_right(body_loc,leg_loc)
                    soldier.update_solider_location(body_loc, leg_loc)

            elif event.key == pygame.K_UP:
                if soldier.is_possible_up(body_loc):
                    soldier.remove_solider_location(body_loc,leg_loc)
                    soldier.move_solider_up(body_loc,leg_loc)
                    soldier.update_solider_location(body_loc, leg_loc)

            elif event.key == pygame.K_DOWN:
                if soldier.is_possible_down(leg_loc):
                    soldier.remove_solider_location(body_loc,leg_loc)
                    soldier.move_solider_down(body_loc,leg_loc)
                    soldier.update_solider_location(body_loc, leg_loc)


            elif event.key == pygame.K_RETURN:
                pass
                #show_screen_with_bumbs()
