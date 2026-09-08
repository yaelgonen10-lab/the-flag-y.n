import pygame
import sys
print('hello')




def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pass
            #pygame.quit()
            #sys.exit()        #running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
                #go_left()

            elif event.key == pygame.K_RIGHT:
                pass
                #go_right()

            elif event.key == pygame.K_UP:
                pass
                #go_up()

            elif event.key == pygame.K_DOWN:
                pass
                #go_down()

            elif event.key == pygame.K_SPACE:
                pass
                #show_screen_with_bumbs()



