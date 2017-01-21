import pygame

from Interface.MonstersArea import MonstersArea
from Interface.TowersArea import TowersArea


class GameInterface:

    def __init__(self):
        self.background = pygame.Rect(0, 490, 875, 200)

        self.towersArea = TowersArea()
        self.monstersArea = MonstersArea()

    def render(self, screen):
        pygame.draw.rect(screen, (240, 200, 0), self.background)
        self.towersArea.render(screen)
        self.monstersArea.render(screen)

    def proceedEvent(self, event):
        self.towersArea.proceedEvent(event)
