import pygame
import sys
import consts
import random


FLOWER_SIZE = (55, 55)  # Size of flowers (instead of the grass)
GREEN = (34, 139, 34)  # The color green
NUM_FLOWERS = 20  # The required number of flowers
MAX_ATTEMPTS = 100  # The number of times it will randomly select a location for the flowers
BUFFER_PIXELS = 15  # To ensure the flowers don't overlap and remain truly separated, we will space them out by using pixels
WHITE = (255, 255, 255)  # Font color of the text



def init_game():
    """Initializes the game ,creates the window, and loads the flower image"""
    pygame.init()
    screen = pygame.display.set_mode(
            (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("game")

    original_image = pygame.image.load("flower.png").convert_alpha()
    flower_image = pygame.transform.scale(original_image, FLOWER_SIZE)

    return screen, flower_image


def generate_flower_positions():
    """Generates random locations for the flowers, ensuring no overlap between them"""
    flower_rects = []
    attempts = 0

    while len(flower_rects) < NUM_FLOWERS and attempts < MAX_ATTEMPTS:
        attempts += 1
        x = random.randint(0, consts.WINDOW_WIDTH - FLOWER_SIZE[0])
        y = random.randint(0, consts.WINDOW_HEIGHT - FLOWER_SIZE[1])

        new_rect = pygame.Rect(x, y, FLOWER_SIZE[0], FLOWER_SIZE[1])
        buffered_rect = new_rect.inflate(BUFFER_PIXELS, BUFFER_PIXELS)

        overlap = False
        for existing_rect in flower_rects:
            if buffered_rect.colliderect(
                    existing_rect.inflate(BUFFER_PIXELS, BUFFER_PIXELS)):
                overlap = True
                break

        if not overlap:
            flower_rects.append(new_rect)

    return flower_rects


def draw_start_message(screen):
    """Draws the opening message in the top left corner of the screen."""
    font = pygame.font.Font(None, 36)
    text_surface = font.render(consts.START_MESSAGE, True, WHITE)

    # שינוי המיקום לפינה השמאלית העליונה (עם מרווח קטן של 70 פיקסלים מהקצוות(ביחס לציר איקס))
    text_rect = text_surface.get_rect(topleft=(70, 10))

    screen.blit(text_surface, text_rect)


def run_game_loop(screen, flower_image, flower_rects):
    """Manages the main game loop, updates events, and draws elements on the screen"""
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(GREEN)

        for rect in flower_rects:
            screen.blit(flower_image, rect.topleft)

        draw_start_message(screen)

        pygame.display.flip()


screen, flower_image = init_game()
flower_rects = generate_flower_positions()
run_game_loop(screen, flower_image, flower_rects)

pygame.quit()
sys.exit()

