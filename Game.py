import pygame

from Map import Map
from State import State
from Interface.GameInterface import GameInterface
from Blocks import Blocks


class Game:
    def __init__(self):

        self.selectedItem = False

        self.interface = GameInterface()
        self.map = Map()

        # Entity (mobs and towers)

    def render(self, screen):
        screen.fill((0, 0, 0))

        self.map.render(screen)
        # -> Entite

        # Interface
        self.interface.render(screen)

    def proceedEvent(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return State.QUIT

        res = self.interface.proceedEvent(event)

        if res == Blocks.BASIC_TOWER and self.selectedItem != Blocks.BASIC_TOWER:
            self.selectedItem = Blocks.BASIC_TOWER
        elif res == Blocks.BASIC_TOWER and self.selectedItem == Blocks.BASIC_TOWER:
            self.selectedItem = False
        elif res == Blocks.MAGIC_TOWER and self.selectedItem != Blocks.MAGIC_TOWER:
            self.selectedItem = Blocks.MAGIC_TOWER
        elif res == Blocks.MAGIC_TOWER and self.selectedItem == Blocks.MAGIC_TOWER:
            self.selectedItem = False
        elif res == Blocks.FROST_TOWER and self.selectedItem != Blocks.FROST_TOWER:
            self.selectedItem = Blocks.FROST_TOWER
        elif res == Blocks.FROST_TOWER and self.selectedItem == Blocks.FROST_TOWER:
            self.selectedItem = False

        if event.type == pygame.MOUSEBUTTONUP:
            if self.selectedItem is not False:
                if 0 <= pygame.mouse.get_pos()[1] / 35 < 15:
                    self.map.setCell(pygame.mouse.get_pos(), self.selectedItem)


