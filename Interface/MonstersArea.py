import pygame

class MonstersArea:

    def __init__(self):
        self.background = pygame.Rect(515, 525, 360, 200)

    def render(self, screen):
        pygame.draw.rect(screen, (175, 175, 175), self.background)
