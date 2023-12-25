from objects import GameClass
from game import *
import random
import time

_game = new_game()

inputs = ["w","s","d","a"]
   
game = GameClass(window_name="py2048")

while game.GAMESTATUS():

    if VERIFY_GAME(_game):

        # Drawing the main window
        game.SET_SCREEN()

        # 2048 TABLE
        game.GAMETABLE()

        get_user_input(random.choice(inputs), _game)

        # Update TABLE
        game.UPDATE_TABLE(values=_game)

        SpawnNumber(_game)

        # Update the display
        game.UPDATE_SCREEN(FPS=60)
