import pygame


class Button:

    def __init__(self, x, y, width, height):

        self.selected = False

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.background = pygame.Rect(x, y, width, height)
        self.foreground = pygame.Rect(x + 5, y + 5, width - 10, height - 10)

    def render(self, screen):
        if self.selected:
            pygame.draw.rect(screen, (255, 40, 0), self.background)
        else:
            pygame.draw.rect(screen, (0, 0, 0), self.background)

        pygame.draw.rect(screen, (255, 255, 255), self.foreground)

    def hover(self, mouse_pos):
        if self.x <= mouse_pos[0] <= self.x + self.width:
            if self.y <= mouse_pos[1] <= self.y + self.height:
                return True
        return False

    def setSelected(self, s):
        self.selected = s
