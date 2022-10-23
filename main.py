from Screen import *
import time


def main():
    game_on = True
    start_game_text = False
    while game_on:
        screen.fill(background_color)

        # Initialize the game board
        MineField.init_board()
        MineField.draw_board()
        MineField.draw_grass()
        if not start_game_text:
            MineField.draw_text("Welcome to the Flag Game", WHITE, x=60, y=20)
            MineField.draw_text("Have Fun !", WHITE, x=60, y=40)
        draw_soldier()

        # Check if the player has pressed any key and moves the player accordingly
        is_key_pressed()

        did_player_touched_border()

        if check_collision_with_mine():
            state["state"] = LOSE_STATE
            draw_lose_message()
            # plays win sound
            pygame.mixer.music.load(WIN_SOUND)
            pygame.mixer.music.play(0)
            game_on = False

        if check_collision_with_flag():
            state["state"] = WIN_STATE
            draw_win_message()
            # plays lose sound
            pygame.mixer.music.load(WIN_SOUND)
            pygame.mixer.music.play(0)
            game_on = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

            if event.type == pygame.KEYUP:
                state["moved"] = False

        pygame.display.flip()
        if state["pressed_enter"]:
            time.sleep(1)
            state["pressed_enter"] = False
        if not game_on:
            time.sleep(3)

    pygame.quit()


if __name__ == '__main__':
    main()
