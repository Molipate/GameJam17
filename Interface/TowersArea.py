import pygame

from Button import Button


class TowersArea:

    def __init__(self):
        self.background = pygame.Rect(155, 490, 360, 200)

        self.tower = Button(160, 495, 105, 90)

    def render(self, screen):
        pygame.draw.rect(screen, (75, 75, 75), self.background)
        self.tower.render(screen)

    def proceedEvent(self, event):

        if event.type == pygame.MOUSEMOTION:
            if self.tower.hover(pygame.mouse.get_pos()):
                self.tower.setSelected(True)


