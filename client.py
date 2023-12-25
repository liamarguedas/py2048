from objects import GameClass
from game import *

_game = new_game()
   
game = GameClass(window_name="py2048")

game.CLEAR_CACHE()

while game.GAMESTATUS():

    # Drawing the main window
    game.SET_SCREEN()

    # 2048 TABLE
    game.GAMETABLE()

    # If not winner/loser
    if VERIFY_GAME(_game):

        # Update TABLE
        game.UPDATE_TABLE(values=_game)

        # Update the display
        game.UPDATE_SCREEN(FPS=60)

        # User Input
        ExecuteUserAction(game.USER_INPUT(), _game)

        # Spawn new number in board
        SpawnNumber(_game)

        # Update the display
        game.UPDATE_SCREEN(FPS=60)
