import pygame
import os

from State import State
from GameState import GameState
from MainMenu import MainMenu



def WaveCraft():

    pygame.init()
    pygame.font.init()

    state = GameState()
    mainMenu = MainMenu()


    screen = pygame.display.set_mode((900, 600), pygame.NOFRAME)

    state.addState(State.MENU)

    main_Loop = True
    while main_Loop:

    #render here
        screen.fill((255, 255, 255))
        if state.getCurrentState() == State.MENU:
            mainMenu.render(screen)
        #-> Interface
        #-> Map
        #-> Entite

        pygame.display.update()

        #Handle Event
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                main_Loop = False

        #Update frame

if __name__ == '__main__':
    os.environ['SDL_VIDEO_WINDOW_POS'] = "75,75"
    WaveCraft()