import pygame


class Button:

    def __init__(self, x, y, width, height):

        self.border_width = 5

        self.x = x
        self.y = y

        self.background = pygame.Rect(x, y, width, height)
        self.foreground = pygame.Rect(x + 5, y + 5, width - 10, height - 10)

    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.background)
        pygame.draw.rect(screen, (255, 255, 255), self.foreground)