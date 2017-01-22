import pygame
import os

from State import State
from GameState import GameState
from MainMenu import MainMenu
from Game import Game


def WaveCraft():

    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()
    dt = clock.tick(60)

    state = GameState()
    mainMenu = MainMenu()
    game = Game()

    screen = pygame.display.set_mode((875, 725), pygame.NOFRAME)

    state.addState(State.MENU)

    main_Loop = True
    while main_Loop:

        # Handle Event
        for event in pygame.event.get():

            if state.getCurrentState() == State.MENU:
                res = mainMenu.proceedEvent(event)
                if res == State.QUIT:
                    main_Loop = False
                if res == State.GAME:
                    state.addState(State.GAME)

            if state.getCurrentState() == State.GAME:
                res = game.proceedEvent(event)
                if res == State.QUIT:
                    state.removeFirstState()
                if res == State.GAMEOVER:
                    state.removeFirstState()
                    game = Game()


        # render here
        screen.fill((255, 255, 255))

        if state.getCurrentState() == State.MENU:
            mainMenu.render(screen)
        if state.getCurrentState() == State.GAME:
            game.render(screen)
        pygame.display.update()

        # Update frame
        if state.getCurrentState() == State.GAME:
            game.update(dt)

        dt = clock.tick(60)



if __name__ == '__main__':
    os.environ['SDL_VIDEO_WINDOW_POS'] = "5,5"
    WaveCraft()
