import pygame

from Map import Map


class Game:

    def __init__(self):

        #Interface
        self.interface = pygame.Rect(0, 525, 875, 165)

        #Map
        self.map = Map()

        #Entity (mobs and towers)

    def render(self, screen):

        screen.fill((0, 0, 0))

        #Interface
        pygame.draw.rect(screen, (240, 200, 0), self.interface)

        self.map.render(screen)
        # -> Entite

        pass