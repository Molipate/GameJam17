import pygame

from Button import Button
from Blocks import Blocks


class TowersArea:

    def __init__(self):
        self.background = pygame.Rect(155, 525, 360, 200)

        self.tower = Button(160, 530, 105, 90)
        self.tower2 = Button(270, 530, 105, 90)
        self.tower3 = Button(390, 530, 105, 90)

    def render(self, screen):
        pygame.draw.rect(screen, (75, 75, 75), self.background)
        self.tower.render(screen)
        self.tower2.render(screen)
        self.tower3.render(screen)

    def proceedEvent(self, event):

        if event.type == pygame.MOUSEMOTION:
            # Tour 1 Hover
            if self.tower.hover(pygame.mouse.get_pos()):
                self.tower.setMouseHover(True)
            else:
                self.tower.setMouseHover(False)

            # Tour 2 Hover
            if self.tower2.hover(pygame.mouse.get_pos()):
                self.tower2.setMouseHover(True)
            else:
                self.tower2.setMouseHover(False)

            # Tour 3 Hover
            if self.tower3.hover(pygame.mouse.get_pos()):
                self.tower3.setMouseHover(True)
            else:
                self.tower3.setMouseHover(False)

        if event.type == pygame.MOUSEBUTTONUP:
            # Tour 1 Select
            if self.tower.hover(pygame.mouse.get_pos()):
                self.tower.setSelected(True)
                self.tower2.setSelected(False)
                self.tower3.setSelected(False)
                return Blocks.BASIC_TOWER
            # Tour 2 Select
            if self.tower2.hover(pygame.mouse.get_pos()):
                self.tower2.setSelected(True)
                self.tower.setSelected(False)
                self.tower3.setSelected(False)
                return Blocks.BASIC_TOWER
            # Tour 3 Select
            if self.tower3.hover(pygame.mouse.get_pos()):
                self.tower3.setSelected(True)
                self.tower.setSelected(False)
                self.tower2.setSelected(False)
                return Blocks.BASIC_TOWER
