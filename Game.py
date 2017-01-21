import pygame

from Map import Map
from State import State
from Interface.GameInterface import GameInterface
from Towers import Towers


class Game:
    def __init__(self):

        self.selectedItem = False
        # Interface
        self.interface = GameInterface()

        # Map
        self.map = Map()

        # Entity (mobs and towers)

    def render(self, screen):
        screen.fill((0, 0, 0))

        self.map.render(screen)
        # -> Entite

        # Interface
        self.interface.render(screen)

        pass

    def proceedEvent(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return State.QUIT

        res = self.interface.proceedEvent(event)


        if event.type == pygame.MOUSEBUTTONUP:
            if self.selectedItem is not False:
                print pygame.mouse.get_pos()[0] / 35, pygame.mouse.get_pos()[1] / 35
                if 0 <= pygame.mouse.get_pos()[1] / 35 < 15:
                    self.map.setCell(pygame.mouse.get_pos(), self.selectedItem)


