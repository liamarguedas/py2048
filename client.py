from objects import GameClass
import sys, pygame

game = GameClass(window_name="py2048")

while game.GAMESTATUS():
    # Drawing the main window
    game.SET_SCREEN()

    # 2048 TABLE
    game.GAMETABLE()

    # Update the display
    game.UPDATE_SCREEN(FPS=60)
