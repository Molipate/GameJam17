import pygame

from Button import Button
from State import State


class MainMenu:
    def __init__(self):
        self.title = pygame.font.Font(None, 60).render("WaveCraft", True, (0, 0, 0))
        self.playButton = Button(100, 100, 150, 150)
        self.quitButton = Button(100, 275, 150, 150)

    def render(self, screen):
        screen.blit(self.title, (450, 250))
        self.playButton.render(screen)
        self.playButton.setText("PLAY")
        self.quitButton.render(screen)
        self.quitButton.setText("QUIT")

    def proceedEvent(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return State.QUIT

        if event.type == pygame.MOUSEMOTION:
            if self.playButton.hover(pygame.mouse.get_pos()):
                self.playButton.setSelected(True)
            else:
                self.playButton.setSelected(False)
            if self.quitButton.hover(pygame.mouse.get_pos()):
                self.quitButton.setSelected(True)
            else:
                self.quitButton.setSelected(False)

        if event.type == pygame.MOUSEBUTTONUP:
            if self.playButton.hover(pygame.mouse.get_pos()):
                return State.GAME
            if self.quitButton.hover(pygame.mouse.get_pos()):
                return State.QUIT
