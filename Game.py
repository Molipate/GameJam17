import pygame

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

        self.interface = GameInterface()
        self.map = Map()

        self.player = Player()
        self.player.money = 1000
        self.player.life = 20

        # Entity (mobs and towers)
        self.mobList = [Mob(), Mob()]

        self.towers = []
        self.tower = Tower()
        self.tower2 = Tower()
        self.tower3 = Tower()

    def render(self, screen):
        screen.fill((0, 0, 0))

        self.map.render(screen)
        # -> Entite
        screen.blit(pygame.font.Font(None, 60).render(str(self.player.money), True, (0, 0, 0)), (750, 250))
        # Interface
        self.interface.render(screen, self.tower, self.tower2, self.tower3)

        self.mobList[0].render(screen)

    def proceedEvent(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return State.QUIT

        res = self.interface.proceedEvent(event)

        if res == Blocks.BASIC_TOWER and self.selectedItem != Blocks.BASIC_TOWER:
            self.selectedItem = Blocks.BASIC_TOWER
            self.towers.append(Tower())
        elif res == Blocks.BASIC_TOWER and self.selectedItem == Blocks.BASIC_TOWER:
            self.selectedItem = False
        elif res == Blocks.MAGIC_TOWER and self.selectedItem != Blocks.MAGIC_TOWER:
            self.selectedItem = Blocks.MAGIC_TOWER
            self.towers.append(Tower())
        elif res == Blocks.MAGIC_TOWER and self.selectedItem == Blocks.MAGIC_TOWER:
            self.selectedItem = False
        elif res == Blocks.FROST_TOWER and self.selectedItem != Blocks.FROST_TOWER:
            self.selectedItem = Blocks.FROST_TOWER
        elif res == Blocks.FROST_TOWER and self.selectedItem == Blocks.FROST_TOWER:
            self.selectedItem = False
        elif res == "upgradeT1":
            self.cost = self.tower.getCost()
            if self.player.money >= self.cost and self.tower.level < 5:
                self.tower.upgrade()
                self.player.money -= self.cost
        elif res == "upgradeT2":
            self.cost = self.tower2.getCost()
            if self.player.money >= self.cost and self.tower2.level < 5:
                self.tower2.upgrade()
                self.player.money -= self.cost
        elif res == "upgradeT3":
            self.cost = self.tower3.getCost()
            if self.player.money >= self.cost and self.tower3.level < 5:
                self.tower3.upgrade()
                self.player.money -= self.cost


        if event.type == pygame.MOUSEBUTTONUP:
            if self.selectedItem is not False:
                if 0 <= pygame.mouse.get_pos()[1] / 35 < 15:
                    self.map.setCell(pygame.mouse.get_pos(), self.selectedItem)


    def update(self, dt):
        for m in self.mobList:
            m.update(dt)
