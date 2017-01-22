from enum import Enum


class State(Enum):
    MENU = 1
    OPTION = 2
    GAME = 3
    PAUSE = 4
    QUIT = 5
    GAMEOVER = 6
