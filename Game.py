import pygame

from BasicTower import BasicTower
from FrostTower import FrostTower
from MagicTower import MagicTower
from Map import Map
from Player import Player
from State import State
from Interface.GameInterface import GameInterface
from Blocks import Blocks
from Mob import Mob
from Tower import Tower


class Game:
    def __init__(self):

        self.selectedItem = False
        self.cost = 0

        self.interface = GameInterface()
        self.map = Map()

        self.player = Player()
        self.player.money = 1000
        self.player.life = 20

        # Entity (mobs and towers)
        self.mobList = [Mob(), Mob()]
        self.towersList = []
        self.line = []

        self.basicTower = BasicTower()
        self.magicTower = MagicTower()
        self.frostTower = FrostTower()

    def render(self, screen):
        screen.fill((0, 0, 0))

        self.map.render(screen)
        # -> Entite
        screen.blit(pygame.font.Font(None, 60).render(str(self.player.money), True, (0, 0, 0)), (750, 250))
        # Interface
        self.interface.render(screen, self.basicTower, self.magicTower, self.frostTower)

        self.mobList[0].render(screen)

        for l in self.line:
            pygame.draw.line(screen, (0, 0, 0), l[0], l[1], 2)

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
        elif res == "upgradeT1":
            self.cost = self.basicTower.getCost()
            if self.player.money >= self.cost and self.basicTower.level < 5:
                self.basicTower.upgrade()
                self.player.money -= self.cost
        elif res == "upgradeT2":
            self.cost = self.magicTower.getCost()
            if self.player.money >= self.cost and self.magicTower.level < 5:
                self.magicTower.upgrade()
                self.player.money -= self.cost
        elif res == "upgradeT3":
            self.cost = self.frostTower.getCost()
            if self.player.money >= self.cost and self.frostTower.level < 5:
                self.frostTower.upgrade()
                self.player.money -= self.cost

        if event.type == pygame.MOUSEBUTTONUP:
            if self.selectedItem is not False:
                if 0 <= pygame.mouse.get_pos()[1] / 35 < 15:
                    if self.selectedItem == Blocks.BASIC_TOWER:
                        self.map.setCell(pygame.mouse.get_pos(), self.selectedItem)
                        self.basicTower = BasicTower()
                        self.basicTower.posX = pygame.mouse.get_pos()[0] / 35
                        self.basicTower.posY = pygame.mouse.get_pos()[1] / 35
                        self.towersList.append(self.basicTower)
                    elif self.selectedItem == Blocks.MAGIC_TOWER:
                        self.map.setCell(pygame.mouse.get_pos(), self.selectedItem)
                        self.magicTower = MagicTower()
                        self.magicTower.posX = pygame.mouse.get_pos()[0] / 35
                        self.magicTower.posY = pygame.mouse.get_pos()[1] / 35
                        self.towersList.append(self.magicTower)
                    elif self.selectedItem == Blocks.FROST_TOWER:
                        self.map.setCell(pygame.mouse.get_pos(), self.selectedItem)
                        self.frostTower = FrostTower()
                        self.frostTower.posX = pygame.mouse.get_pos()[0] / 35
                        self.frostTower.posY = pygame.mouse.get_pos()[1] / 35
                        self.towersList.append(self.frostTower)

    def update(self, dt):
        for m in self.mobList:
            m.update(dt)

        self.line = []
        for t in self.towersList:
            for m in self.mobList:
                if t.posX - 4 < m.x / 35 < t.posX + 4 and t.posY - 4 < m.y / 35 < t.posY + 4:
                    self.line.append(((t.posX * 35+35/2, t.posY * 35+35/2), (m.x+35/2, m.y+35/2)))
