from const import *
import random


index_flag = [(21, 46), (21, 47), (21, 48), (21, 49), (22, 46), (22, 47), (22, 48), (22, 49), (23, 46),
              (23, 47), (23, 48), (23, 49)]
invalid_index_player = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]
mine_exist = []
num_mines = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
grass_exist = []
num_grass = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
my_image = pygame.image.load(GRASS_IMAGE)
my_image_reduce = pygame.transform.scale(my_image, (60, 40))


def is_valid_grass(grass):
    rand_row = random.randint(0, 24)
    rand_col = random.randint(0, 49)
    if (rand_row, rand_col) not in grass_exist and (rand_row, rand_col) not in invalid_index_player:
        num_grass.remove(grass)
        BOARD[rand_row][rand_col] = GRASS_VALUE


def is_valid_mine(mine):
    rand_row = random.randint(0, 24)
    rand_col = random.randint(0, 49)
    if (rand_row, rand_col) not in index_flag and (rand_row, rand_col) not in invalid_index_player and (
            rand_row, rand_col) not in mine_exist and len(
        BOARD[rand_row]) > rand_col + 3 and BOARD[rand_row][rand_col + 1] == 0 and BOARD[rand_row][
        rand_col + 2] == 0:
        num_mines.remove(mine)
        BOARD[rand_row][rand_col] = MINE_VALUE
        start_mine_x = rand_row * tile_size
        start_mine_y = rand_col * tile_size
        mine_exist.append((start_mine_x, start_mine_y))
        mine_exist.append((start_mine_x, start_mine_y + tile_size))
        mine_exist.append((start_mine_x, start_mine_y + tile_size + tile_size))


def place_mines():
    place_flag()
    while len(num_mines) > 0:
        for mine in num_mines:
            is_valid_mine(mine)


def place_grass():
    while len(num_grass) > 0:
        for grass in num_grass:
            is_valid_grass(grass)


def place_flag():
    for row, col in index_flag:
        BOARD[row][col] = FLAG_VALUE


def draw_text(text, text_color, x=SCREEN_WIDTH // 2 + 50, y=SCREEN_HEIGHT // 2):
    font = pygame.font.SysFont("candara", 24)
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


tile_list_flag = []
tile_list_mine = []
tile_list_grass = []


def init_board():

    place_mines()
    place_grass()
    row_count = 0
    flag_draw = False
    num_mines_draw = 0
    num_grass_draw = 0
    for row in BOARD:
        col_count = 0
        for tile in row:
            if tile == MINE_VALUE and num_mines_draw < 20:
                num_mines_draw += 1
                img = pygame.transform.scale(mine_img, (60, 20))
                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                img_rect.y = row_count * tile_size
                tile = (img, img_rect)
                tile_list_mine.append(tile)
            if tile == FLAG_VALUE and not flag_draw:
                flag_draw = True
                img = pygame.transform.scale(flag_img, (tile_size * 4, tile_size * 4))
                img_rect = img.get_rect()
                img_rect.x = screen_width - (tile_size * 4)
                img_rect.y = screen_height - (tile_size * 3) - tile_size
                tile = (img, img_rect)
                tile_list_flag.append(tile)
            if tile == GRASS_VALUE and num_grass_draw < 20:
                num_grass_draw += 1
                img = pygame.transform.scale(grass_img, (60, 40))
                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                img_rect.y = row_count * tile_size
                tile = (img, img_rect)
                tile_list_grass.append(tile)
            col_count += 1
        row_count += 1


def draw_mine():
    for tile in tile_list_mine:
        screen.blit(tile[0], tile[1])


def draw_grass():
    for tile in tile_list_grass:
        screen.blit(tile[0], tile[1])


def draw_board():
    for tile in tile_list_flag:
        screen.blit(tile[0], tile[1])
