import pygame

from Button import Button
from Blocks import Blocks


class TowersArea:

    def __init__(self):
        self.background = pygame.Rect(155, 525, 360, 200)

        self.tower = Button(160, 530, 105, 90)

    def render(self, screen):
        pygame.draw.rect(screen, (75, 75, 75), self.background)
        self.tower.render(screen)

    def proceedEvent(self, event):

        if event.type == pygame.MOUSEMOTION:
            if self.tower.hover(pygame.mouse.get_pos()):
                self.tower.setSelected(True)
            else:
                self.tower.setSelected(False)

        if event.type == pygame.MOUSEBUTTONUP:
            if self.tower.hover(pygame.mouse.get_pos()):
                return Blocks.BASIC_TOWER


