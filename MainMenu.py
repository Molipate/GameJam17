import pygame

from Button import Button


class MainMenu():

    def __init__(self):
        self.title = pygame.font.Font(None, 60).render("WaveCraft", True, (0, 0, 0))
        self.playButton = Button(100, 100, 150, 150)
        self.quitButton = Button(100, 275, 150, 150)

    def render(self, screen):
        screen.blit(self.title, (450, 250))
        self.playButton.render(screen)
        self.quitButton.render(screen)