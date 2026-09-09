import sys
import pygame
import consts
import game_field
import screen
import soldier

ARROW_KEYS = {
    pygame.K_UP: "up",
    pygame.K_DOWN: "down",
    pygame.K_LEFT: "left",
    pygame.K_RIGHT: "right",
}


def main():
    window_surface = screen.create_game_window()
    images_dictionary = screen.load_game_images()
    bushes_list = screen.generate_bushes_positions()

    clock = pygame.time.Clock()

    game_field.build()  # מטריצה + דגל + מוקשים
    soldier.create()  # חייל בפינה השמאלית-עליונה

    game = {
        "state": consts.STATE_PLAY,
        "since": 0,
        "running": True,
        "window_surface": window_surface,
        "images_dictionary": images_dictionary,
        "bushes_list": bushes_list,
    }

    while game["running"]:
        handle_events(game)
        update(game)
        draw(game)
        screen.update_display()
        clock.tick(consts.FPS)

    pygame.quit()
    sys.exit()


def handle_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game["running"] = False
        elif event.type == pygame.KEYDOWN and game[
            "state"] == consts.STATE_PLAY:
            if event.key == pygame.K_RETURN:
                change_state(game, consts.STATE_REVEAL)
            elif event.key in ARROW_KEYS:
                direction = ARROW_KEYS[event.key]
                if soldier.can_move(direction):
                    soldier.move(direction)


def update(game):
    now = pygame.time.get_ticks()
    state = game["state"]

    if state == consts.STATE_PLAY:
        # ניצחון נבדק מול הגוף, הפסד מול הרגליים - כמו בנספח
        if game_field.touches_flag(soldier.body_cells()):
            change_state(game, consts.STATE_WIN)
        elif game_field.touches_mine(soldier.feet_cells()):
            change_state(game, consts.STATE_LOSE)

    elif state == consts.STATE_REVEAL:
        # אחרי שנייה - חזרה למשחק רגיל
        if now - game["since"] >= consts.REVEAL_MS:
            change_state(game, consts.STATE_PLAY)

    elif state in (consts.STATE_WIN, consts.STATE_LOSE):
        # אחרי שלוש שניות של הודעה - סגירת המשחק
        if now - game["since"] >= consts.END_MESSAGE_MS:
            game["running"] = False


def change_state(game, new_state):
    """מעביר את המשחק למצב חדש ושומר את זמן המעבר."""
    game["state"] = new_state
    game["since"] = pygame.time.get_ticks()


def draw(game):
    """מצייר את הפריים הנוכחי לפי מצב המשחק."""
    state = game["state"]
    surface = game["window_surface"]
    images = game["images_dictionary"]
    bushes = game["bushes_list"]

    if state == consts.STATE_REVEAL:
        screen.draw_reveal_mode(surface, images)
        return

    screen.draw_background_field(surface)
    screen.draw_all_bushes(surface, images, bushes)
    screen.draw_game_flag(surface, images)
    screen.draw_game_soldier(surface, images)

    if state == consts.STATE_PLAY:
        screen.draw_welcome_text(surface)
    elif state == consts.STATE_WIN:
        screen.draw_popup_message(surface, consts.WIN_MESSAGE,
                                  consts.WIN_TEXT_COLOR)
    elif state == consts.STATE_LOSE:
        screen.draw_popup_message(surface, consts.LOSE_MESSAGE,
                                  consts.LOSE_TEXT_COLOR)


if __name__ == "__main__":
    main()
