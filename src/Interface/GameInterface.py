import pygame

from Interface.MonstersArea import MonstersArea
from Interface.PlayerArea import PlayerArea
from Interface.TowersArea import TowersArea


class GameInterface:

    def __init__(self):
        self.background = pygame.Rect(0, 525, 875, 200)

        self.towersArea = TowersArea()
        self.monstersArea = MonstersArea()
        self.playerArea = PlayerArea()

    def render(self, screen, towerLVL, tower2LVL, tower3LVL, player):
        pygame.draw.rect(screen, (240, 200, 0), self.background)
        self.towersArea.render(screen, towerLVL, tower2LVL, tower3LVL)
        self.playerArea.render(screen, player)
        self.monstersArea.render(screen)

    def proceedEvent(self, event):
        return self.towersArea.proceedEvent(event)
