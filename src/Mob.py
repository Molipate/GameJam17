import pygame

from Directions import Directions


class Mob:
    def __init__(self):

        self.life = 5000
        self.speed = 1
        self.income = 50

        self.x = 35
        self.y = 245

        self.sprite = pygame.image.load("Assets/mob_test.png")
        self.sprite.set_colorkey((0, 255, 0))

        self.direction = Directions.RIGHT

        self.way = []

    def update(self, dt):

        if self.direction == Directions.LEFT:
            self.x -= self.speed * dt / 10
        if self.direction == Directions.TOP:
            self.y -= self.speed * dt / 10
        if self.direction == Directions.RIGHT:
            self.x += self.speed * dt / 10
        if self.direction == Directions.BOTTOM:
            self.y += self.speed * dt / 10

        if 210 <= self.x <= 245 and 245 <= self.y <= 280:
            self.direction = Directions.BOTTOM
        if 210 <= self.x <= 245 and 385 <= self.y <= 420:
            self.direction = Directions.RIGHT
        if 315 <= self.x <= 350 and 385 <= self.y <= 420:
            self.direction = Directions.TOP
        if 315 <= self.x <= 350 and 70 <= self.y <= 105:
            self.direction = Directions.RIGHT
        if 630 <= self.x <= 665 and 70 <= self.y <= 105:
            self.direction = Directions.BOTTOM
        if 630 <= self.x <= 665 and 245 <= self.y <= 280:
            self.direction = Directions.LEFT
        if 455 <= self.x <= 490 and 245 <= self.y <= 280:
            self.direction = Directions.BOTTOM
        if 455 <= self.x <= 490 and 315 <= self.y <= 350:
            self.direction = Directions.RIGHT
        if 560 <= self.x <= 595 and 315 <= self.y <= 350:
            self.direction = Directions.BOTTOM
        if 560 <= self.x <= 595 and 420 <= self.y <= 455:
            self.direction = Directions.RIGHT
        if 770 <= self.x <= 805 and 420 <= self.y <= 455:
            self.direction = Directions.TOP
        if 770 <= self.x <= 805 and 210 <= self.y <= 245:
            self.direction = Directions.RIGHT


    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
