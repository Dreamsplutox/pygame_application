import pygame
from monster import Monster
pygame.init()


class Golem(Monster):
    walkRight = [pygame.image.load('images/golem/golemR1.png'), pygame.image.load('images/golem/golemR1.png'),
                 pygame.image.load('images/golem/golemR2.png'), pygame.image.load('images/golem/golemR2.png'),
                 pygame.image.load('images/golem/golemR3.png'), pygame.image.load('images/golem/golemR3.png')]
    walkLeft = [pygame.image.load('images/golem/golemL1.png'), pygame.image.load('images/golem/golemL1.png'),
                 pygame.image.load('images/golem/golemL2.png'), pygame.image.load('images/golem/golemL1.png'),
                 pygame.image.load('images/golem/golemL3.png'), pygame.image.load('images/golem/golemL3.png')]

    def __init__(self, x, y, width, height, end, lives, begin=0):
        Monster.__init__(self, x, y, width, height, end, lives, begin)
        self.isJumping = False
        self.jump = 10

    def draw(self, win):
        self.move()
        if self.alive:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0

            if self.vel > 0:
                self.left = False
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                self.left = True
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1