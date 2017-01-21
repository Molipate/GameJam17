import pygame

from Button import Button
from Blocks import Blocks


class TowersArea:

    def __init__(self):
        self.background = pygame.Rect(155, 525, 360, 200)

        self.tower = Button(162, 530, 105, 90)
        self.tower2 = Button(283, 530, 105, 90)
        self.tower3 = Button(403, 530, 105, 90)
        self.tower4 = Button(162, 630, 105, 90)
        self.tower5 = Button(283, 630, 105, 90)
        self.tower6 = Button(403, 630, 105, 90)

    def render(self, screen):
        pygame.draw.rect(screen, (75, 75, 75), self.background)
        self.tower.render(screen)
        self.tower2.render(screen)
        self.tower3.render(screen)
        self.tower4.render(screen)
        self.tower5.render(screen)
        self.tower6.render(screen)

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

            # Tour 4 Hover
            if self.tower4.hover(pygame.mouse.get_pos()):
                self.tower4.setMouseHover(True)
            else:
                self.tower4.setMouseHover(False)

            # Tour 5 Hover
            if self.tower5.hover(pygame.mouse.get_pos()):
                self.tower5.setMouseHover(True)
            else:
                self.tower5.setMouseHover(False)

            # Tour 6 Hover
            if self.tower6.hover(pygame.mouse.get_pos()):
                self.tower6.setMouseHover(True)
            else:
                self.tower6.setMouseHover(False)

        if event.type == pygame.MOUSEBUTTONUP:
            # Tour 1 Select
            if self.tower.hover(pygame.mouse.get_pos()):
                self.tower.setSelected(True)
                self.tower2.setSelected(False)
                self.tower3.setSelected(False)
                self.tower4.setSelected(False)
                self.tower5.setSelected(False)
                self.tower6.setSelected(False)
                return Blocks.BASIC_TOWER
            # Tour 2 Select
            if self.tower2.hover(pygame.mouse.get_pos()):
                self.tower2.setSelected(True)
                self.tower.setSelected(False)
                self.tower3.setSelected(False)
                self.tower4.setSelected(False)
                self.tower5.setSelected(False)
                self.tower6.setSelected(False)
                return Blocks.MAGIC_TOWER
            # Tour 3 Select
            if self.tower3.hover(pygame.mouse.get_pos()):
                self.tower3.setSelected(True)
                self.tower.setSelected(False)
                self.tower2.setSelected(False)
                self.tower4.setSelected(False)
                self.tower5.setSelected(False)
                self.tower6.setSelected(False)
                return Blocks.BASIC_TOWER
            # Tour 4 Select
            if self.tower4.hover(pygame.mouse.get_pos()):
                self.tower4.setSelected(True)
                self.tower.setSelected(False)
                self.tower2.setSelected(False)
                self.tower3.setSelected(False)
                self.tower5.setSelected(False)
                self.tower6.setSelected(False)
                return Blocks.BASIC_TOWER
            # Tour 5 Select
            if self.tower5.hover(pygame.mouse.get_pos()):
                self.tower5.setSelected(True)
                self.tower.setSelected(False)
                self.tower2.setSelected(False)
                self.tower3.setSelected(False)
                self.tower4.setSelected(False)
                self.tower6.setSelected(False)
                return Blocks.MAGIC_TOWER
            # Tour 6 Select
            if self.tower6.hover(pygame.mouse.get_pos()):
                self.tower6.setSelected(True)
                self.tower.setSelected(False)
                self.tower2.setSelected(False)
                self.tower3.setSelected(False)
                self.tower4.setSelected(False)
                self.tower5.setSelected(False)
                return Blocks.BASIC_TOWER
