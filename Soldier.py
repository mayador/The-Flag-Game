from const import *
import MineField
import pygame
from pygame.locals import *

state = {
    "image": pygame.transform.scale(soldier_img, (60, 80)),
    "image_night": pygame.transform.scale(soldier_night_img, (60, 80)),
    "player_x": 0,
    "player_y": 0,
    "moved": False,
    "touched_mine": False,
    "touched_flag": False,
    "is_window_open": True,
    "state": RUNNING_STATE,
    "player_rect": Rect(0, 0, 40, 80),
    "flag_rect": Rect(screen_width - (tile_size * 4), screen_height - (tile_size * 3) - tile_size, 80, 60),
    "rect_x": 0,
    "rect_y": 0,
    "pressed_enter": False
}


def init_soldier():
    pass


def draw_soldier():
    did_player_touched_border()
    screen.blit(state["image"], (state["player_x"], state["player_y"]))


def draw_soldier_night():
    screen.blit(state["image_night"], (state["player_x"], state["player_y"]))


def move_right():
    state["player_x"] += tile_size
    draw_soldier()


def move_left():
    state["player_x"] -= tile_size
    draw_soldier()


def move_up():
    state["player_y"] -= tile_size
    draw_soldier()


def move_down():
    state["player_y"] += tile_size
    draw_soldier()


def calc_leg_y():
    return state["player_y"] + 60


def check_collision_with_mine():
    for tile in MineField.tile_list_mine:
        if tile[1].colliderect(state["player_x"], state["player_y"] + 60, 40, 20):
            return True
    return False


def check_collision_with_flag():
    for tile in MineField.tile_list_flag:
        if tile[1].colliderect((state["player_x"] + 20, state["player_y"], 20, 40)):
            return True
    return False


def did_player_touched_border():
    if state["player_x"] <= 0:
        state["player_x"] = 0
    if state["player_x"] >= screen_width - 40:
        state["player_x"] = screen_width - 40
    if state["player_y"] <= 0:
        state["player_y"] = 0
    if state["player_y"] >= screen_height - 80:
        state["player_y"] = screen_height - 80
