from objects import GameClass
from game import new_game, VERIFY_GAME, ExecuteUserAction, SpawnNumber


def py2048():
    table = new_game()

    game = GameClass(window_name="py2048")

    game.CLEAR_CACHE()

    while game.GAMESTATUS():
        # Drawing the main window
        game.SET_SCREEN()

        # 2048 TABLE
        game.GAMETABLE()

        # If not winner/loser
        if VERIFY_GAME(table):
            # Update TABLE
            game.UPDATE_TABLE(values=table)

            # Update the display
            game.UPDATE_SCREEN(FPS=60)

            # User Input
            ExecuteUserAction(game.USER_INPUT(), table)

            # Spawn new number in board
            SpawnNumber(table)

            # Update the display
            game.UPDATE_SCREEN(FPS=60)
