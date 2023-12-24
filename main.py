from game import *

_game = [[" ", " ", 2, " "],
         [2, " ", " ", " "],
         [2, " ", 4, " "],
         [2, " ", 4, " "]]


def main():
    _game = new_game()
    update_table(_game)

    while VERIFY_GAME(_game):
        update_table(_game)

        get_user_input(input(), _game)

        SpawnNumber(_game)


if __name__ == "__main__":
    main()
