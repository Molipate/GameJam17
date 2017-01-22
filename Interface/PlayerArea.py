import pygame


class PlayerArea:
    def __init__(self):
        self.background = pygame.Rect(515, 525, 360, 200)

    def render(self, screen, player):
        screen.blit(pygame.font.Font(None, 60).render(str(player.money), True, (0, 0, 0)), (25, 550))
        screen.blit(pygame.font.Font(None, 60).render(str(player.life), True, (0, 0, 0)), (25, 650))
