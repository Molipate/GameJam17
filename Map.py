import pygame

from Blocks import Blocks


class Map:
    def __init__(self):

        self.empty = pygame.image.load("Assets/empty.png")
        self.topBorder = pygame.image.load("Assets/top_border.png")
        self.topLeftBorder = pygame.image.load("Assets/top_left_corner.png")
        self.topRightBorder = pygame.image.load("Assets/top_right_corner.png")
        self.botBorder = pygame.image.load("Assets/bottom_border.png")
        self.botLeftBorder = pygame.image.load("Assets/bottom_left_corner.png")
        self.botRightBorder = pygame.image.load("Assets/bottom_right_corner.png")
        self.leftBorder = pygame.image.load("Assets/left_border.png")
        self.rightBorder = pygame.image.load("Assets/right_border.png")
        self.arrow = pygame.image.load("Assets/arrow.png")
        self.basicTower = pygame.image.load("Assets/basic_tower.png")
        self.grass = pygame.image.load("Assets/weed.png")

        self.tab = []
        for i in range(25):
            self.tab.append([])
            for j in range(15):
                self.tab[i].append(0)



        self.tab[0][0] = Blocks.TOP_LEFT_BORDER
        self.tab[24][0] = Blocks.TOP_RIGHT_BORDER
        for i in range(1, 24):
            self.tab[i][0] = Blocks.TOP_BORDER

        self.tab[0][14] = Blocks.BOT_LEFT_BORDER
        self.tab[24][14] = Blocks.BOT_RIGHT_BORDER
        for i in range(1, 24):
            self.tab[i][14] = Blocks.BOT_BORDER

        for i in range(1, 7):
            self.tab[0][i] = Blocks.LEFT_BORDER
            self.tab[0][i + 7] = Blocks.LEFT_BORDER
            self.tab[24][i] = Blocks.RIGHT_BORDER
            self.tab[24][i + 7] = Blocks.RIGHT_BORDER

            self.tab[0][7] = Blocks.ARROW
            self.tab[24][7] = Blocks.ARROW

    def render(self, screen):

        for i in range(25):
            for j in range(15):
                if self.tab[i][j] == Blocks.EMPTY:
                    screen.blit(self.empty, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.TOP_LEFT_BORDER:
                    screen.blit(self.topLeftBorder, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.TOP_RIGHT_BORDER:
                    screen.blit(self.topRightBorder, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.TOP_BORDER:
                    screen.blit(self.topBorder, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.LEFT_BORDER:
                    screen.blit(self.leftBorder, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.RIGHT_BORDER:
                    screen.blit(self.rightBorder, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.BOT_LEFT_BORDER:
                    screen.blit(self.botLeftBorder, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.BOT_RIGHT_BORDER:
                    screen.blit(self.botRightBorder, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.BOT_BORDER:
                    screen.blit(self.botBorder, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.ARROW:
                    screen.blit(self.arrow, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.GRASS:
                    screen.blit(self.grass, (i * 35, j * 35))
                if self.tab[i][j] == Blocks.BASIC_TOWER:
                    screen.blit(self.basicTower, (i * 35, j * 35))

    def setCell(self, mouse_pos, value):
        if self.tab[mouse_pos[0] / 35][mouse_pos[1] / 35] == Blocks.EMPTY:
            self.tab[mouse_pos[0] / 35][mouse_pos[1] / 35] = value
