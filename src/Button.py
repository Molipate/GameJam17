import pygame


class Button:
    def __init__(self, x, y, width, height):

        self.name = pygame.font.Font(None, 60)

        self.mouseHover = False

        self.selected = False

        # VARIALBES DU BOUTON

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.background = pygame.Rect(x, y, width, height)
        self.foreground = pygame.Rect(x + 5, y + 5, width - 10, height - 10)

        # VARIABLES DU TEXTE
        self.txt = ""

        self.txtWidth = 0
        self.txtHeight = 0

        self.txtPosX = 0
        self.txtPosY = 0

    def render(self, screen):
        if self.mouseHover:
            pygame.draw.rect(screen, (255, 40, 0), self.background)
        elif self.selected:
            pygame.draw.rect(screen, (0, 255, 0), self.background)
        else:
            pygame.draw.rect(screen, (0, 0, 0), self.background)

        pygame.draw.rect(screen, (255, 255, 255), self.foreground)

        screen.blit(pygame.font.Font(None, 60).render(self.txt, True, (0, 0, 0)), (self.txtPosX, self.txtPosY))

    def hover(self, mouse_pos):
        if self.x <= mouse_pos[0] <= self.x + self.width:
            if self.y <= mouse_pos[1] <= self.y + self.height:
                return True
        return False

    def setMouseHover(self, h):
        self.mouseHover = h

    def setSelected(self, s):
        self.selected = s

    def setText(self, str):
        self.txt = str
        self.txtWidth = pygame.font.Font(None, 60).size(self.txt)[0]
        self.txtHeight = pygame.font.Font(None, 60).size(self.txt)[1]
        self.txtPosX = self.x + (self.width / 2) - (self.txtWidth / 2)
        self.txtPosY = self.y + (self.height / 2) - (self.txtHeight / 2)
