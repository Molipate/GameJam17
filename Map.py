import pygame

class Map:

    def __init__(self):

        self.green = pygame.image.load("Assets/green.png")
        self.red = pygame.image.load("Assets/red.png")

        self.tab = []
        for i in range(25):
            self.tab.append([])
            for j in range(15):
                self.tab[i].append(0)

        for i in range(7):
            self.tab[0][i] = 1
            self.tab[0][i + 8] = 1
            self.tab[24][i] = 1
            self.tab[24][i + 8] = 1

    def render(self, screen):

        for i in range(25):
            for j in range(15):
                if self.tab[i][j] == 0:
                    screen.blit(self.green, (i * 35, j * 35))
                if self.tab[i][j] == 1:
                    screen.blit(self.red, (i * 35, j * 35))