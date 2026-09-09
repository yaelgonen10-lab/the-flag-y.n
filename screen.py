import random
import pygame
import consts
import game_field
import soldier


def create_game_window():
    pygame.init()

    width = consts.WINDOW_WIDTH
    height = consts.WINDOW_HEIGHT
    window_surface = pygame.display.set_mode((width, height))

    pygame.display.set_caption(consts.WINDOW_TITLE)

    return window_surface


def load_game_images():
    images_dictionary = {}
    soldier_raw = pygame.image.load(consts.SOLDIER_IMAGE).convert_alpha()
    images_dictionary["soldier"] = pygame.transform.scale(soldier_raw,
                                                          consts.SOLDIER_PIXEL_SIZE)

    flag_raw = pygame.image.load(consts.FLAG_IMAGE).convert_alpha()
    images_dictionary["flag"] = pygame.transform.scale(flag_raw,
                                                       consts.FLAG_PIXEL_SIZE)

    mine_raw = pygame.image.load(consts.MINE_IMAGE).convert_alpha()
    images_dictionary["mine"] = pygame.transform.scale(mine_raw,
                                                       consts.MINE_PIXEL_SIZE)

    # טעינת תמונת השיח בגודלה המקורי
    images_dictionary["bush"] = pygame.image.load(
        consts.BUSH_IMAGE).convert_alpha()

    return images_dictionary


def generate_bushes_positions():
    """
    מגרילה מיקומים וגדלים עבור השיחים במשחק בצורה אקראית.
    מוודאת שהשיחים לא עולים אחד על השני, ומחזירה רשימה של מלבנים (Rect) עבור המיקומים שלהם.
    """
    bushes_list = []
    min_size = consts.BUSH_MIN_CELLS * consts.CELL_SIZE
    max_size = consts.BUSH_MAX_CELLS * consts.CELL_SIZE
    attempts = 0

    while len(
            bushes_list) < consts.BUSHES_COUNT and attempts < consts.BUSH_PLACE_ATTEMPTS:
        attempts += 1

        # הגרלת גודל השיח ומיקומו על המסך
        size = random.randint(min_size, max_size)
        x = random.randint(0, consts.WINDOW_WIDTH - size)
        y = random.randint(0, consts.WINDOW_HEIGHT - size)

        candidate_rect = pygame.Rect(x, y, size, size)

        # בדיקה האם השיח החדש מתנגש בשיח שכבר קיים ברשימה
        has_collision = False
        for existing_bush in bushes_list:
            if candidate_rect.colliderect(existing_bush):
                has_collision = True

        # אם אין התנגשות, נוסיף את השיח לרשימה
        if not has_collision:
            bushes_list.append(candidate_rect)

    return bushes_list


def draw_background_field(window_surface):
    """
    צובעת את כל רקע מסך המשחק בצבע השדה הסטנדרטי.
    """
    window_surface.fill(consts.FIELD_COLOR)


def draw_all_bushes(window_surface, images_dictionary, bushes_list):
    """
    עוברת על רשימת המיקומים של השיחים, משנה את גודל תמונת השיח
    בהתאם לגודל שהוגרל לו, ומציירת אותו על המסך.
    """
    for bush_rect in bushes_list:
        bush_image = images_dictionary["bush"]
        scaled_bush = pygame.transform.scale(bush_image, (bush_rect.width,
                                                          bush_rect.height))
        window_surface.blit(scaled_bush, bush_rect.topleft)


def draw_game_flag(window_surface, images_dictionary):
    """
    מחשבת את המיקום המדויק בפיקסלים של הדגל לפי המערך של שדה המשחק,
    ומציירת את תמונת הדגל על המסך.
    """
    row, col = game_field.flag_top_left()
    pixel_x = col * consts.CELL_SIZE
    pixel_y = row * consts.CELL_SIZE

    window_surface.blit(images_dictionary["flag"], (pixel_x, pixel_y))


def draw_game_soldier(window_surface, images_dictionary):
    """
    מציירת את תמונת החייל במיקום הפיקסלים הנוכחי שלו בשדה.
    """
    soldier_position = soldier.pixel_top_left()
    window_surface.blit(images_dictionary["soldier"], soldier_position)


def draw_welcome_text(window_surface):
    """
    מייצרת ומציירת את הודעת הפתיחה וההסבר של המשחק שורה אחר שורה
    בצד ימין של המסך, בהתאם לגופנים ולצבעים שהוגדרו.
    """
    font = pygame.font.SysFont(consts.FONT_NAME, consts.WELCOME_FONT_SIZE,
                               bold=True)

    # חישוב היכן להתחיל לצייר את הטקסט מימין לחייל
    start_x = consts.SOLDIER_COLS * consts.CELL_SIZE + consts.CELL_SIZE
    current_y = consts.CELL_SIZE // 2

    # פירוק הודעת המולטי-ליין לשורות נפרדות וציורן
    message_lines = consts.WELCOME_MESSAGE.split("\n")
    for line in message_lines:
        text_image = font.render(line, True, consts.WELCOME_TEXT_COLOR)
        window_surface.blit(text_image, (start_x, current_y))
        current_y += font.get_linesize()


def draw_reveal_mode(window_surface, images_dictionary):
    """
    מציגה את מצב חשיפת המוקשים (כאשר השחקן מפסיד או לוחץ על מקש החשיפה):
    צובעת את הרקע, מציירת רשת משבצות (גריד), מציגה את כל המוקשים בשדה,
    ולבסוף מציירת את הדגל והחייל.
    """
    window_surface.fill(consts.REVEAL_BG_COLOR)

    # ציור קווי הרשת האנכיים
    for x in range(0, consts.WINDOW_WIDTH + 1, consts.CELL_SIZE):
        pygame.draw.line(window_surface, consts.GRID_LINE_COLOR, (x, 0),
                         (x, consts.WINDOW_HEIGHT))

    # ציור קווי הרשת האופקיים
    for y in range(0, consts.WINDOW_HEIGHT + 1, consts.CELL_SIZE):
        pygame.draw.line(window_surface, consts.GRID_LINE_COLOR, (0, y),
                         (consts.WINDOW_WIDTH, y))

    # מעבר על רשימת המוקשים וציור של כל מוקש במשבצת שלו
    for row, col in game_field.mines:
        pixel_x = col * consts.CELL_SIZE
        pixel_y = row * consts.CELL_SIZE
        window_surface.blit(images_dictionary["mine"], (pixel_x, pixel_y))

    # ציור הדגל והחייל מעל הרשת והמוקשים
    draw_game_flag(window_surface, images_dictionary)
    draw_game_soldier(window_surface, images_dictionary)


def draw_popup_message(window_surface, text, color):
    """
    מציירת תיבת הודעה ריבועית במרכז המסך (למשל עבור הודעת ניצחון או הפסד)
    ומציגה בתוכה את הטקסט המבוקש.
    """
    font = pygame.font.SysFont(consts.FONT_NAME, consts.MESSAGE_FONT_SIZE,
                               bold=True)
    text_image = font.render(text, True, color)

    # מיקום הטקסט בדיוק במרכז החלון
    center_x = consts.WINDOW_WIDTH // 2
    center_y = consts.WINDOW_HEIGHT // 2
    text_rect = text_image.get_rect(center=(center_x, center_y))

    # יצירת תיבת רקע גדולה במעט מהטקסט וציורה
    padding_x = consts.CELL_SIZE * 2
    padding_y = consts.CELL_SIZE
    box_rect = text_rect.inflate(padding_x, padding_y)

    pygame.draw.rect(window_surface, consts.MESSAGE_BOX_COLOR, box_rect)
    window_surface.blit(text_image, text_rect)


def update_display():
    """
    מעדכנת את התצוגה על המסך ומציגה בפועל את כל מה שצויר מאז העדכון האחרון.
    """
    pygame.display.flip()
