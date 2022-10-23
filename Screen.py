from Soldier import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_grid():
    for row in range(0, 60):
        pygame.draw.line(screen, GRID_COLOR, (0, row * tile_size), (screen_width, row * tile_size))
        pygame.draw.line(screen, GRID_COLOR, (row * tile_size, 0), (row * tile_size, screen_height))


def is_key_pressed():
    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN] and not state["pressed_enter"]:
        screen.fill(BLACK)
        MineField.draw_mine()
        draw_grid()
        draw_soldier_night()
        state["pressed_enter"] = True
    if key[pygame.K_RIGHT] and not state["moved"]:
        move_right()
        state["moved"] = True
    if key[pygame.KEYDOWN] is False:
        state["moved"] = False
    if key[pygame.K_LEFT] and not state["moved"]:
        move_left()
        state["moved"] = True
    if key[pygame.KEYDOWN] is False:
        state["moved"] = False
    if key[pygame.K_UP] and not state["moved"]:
        move_up()
        state["moved"] = True
    if key[pygame.KEYDOWN] is False:
        state["moved"] = False
    if key[pygame.K_DOWN] and not state["moved"]:
        move_down()
        state["moved"] = True
    if key[pygame.KEYDOWN] is False:
        state["moved"] = False


def draw_lose_message():
    draw_message(LOSE_MESSAGE, WIN_LOSE_FONT_SIZE,
                 LOSE_COLOR, WIN_LOSE_LOCATION)


def draw_win_message():
    draw_message(WIN_MESSAGE, WIN_LOSE_FONT_SIZE,
                 WIN_COLOR, WIN_LOSE_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def player_lost():
    draw_lose_message()


def player_won():
    draw_win_message()
