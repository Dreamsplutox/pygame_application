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

    hitRight = [pygame.image.load('images/golem/golemR4.png'), pygame.image.load('images/golem/golemR4.png'),
                 pygame.image.load('images/golem/golemR5.png'), pygame.image.load('images/golem/golemR5.png'),
                 pygame.image.load('images/golem/golemR6.png'), pygame.image.load('images/golem/golemR6.png')]
    hitLeft = [pygame.image.load('images/golem/golemL4.png'), pygame.image.load('images/golem/golemL4.png'),
                pygame.image.load('images/golem/golemL5.png'), pygame.image.load('images/golem/golemL5.png'),
                pygame.image.load('images/golem/golemL6.png'), pygame.image.load('images/golem/golemL6.png')]


    def __init__(self, x, y, range, power, width, height, end, lives, begin=0, vel=3, IA='agressive', look=1):
        Monster.__init__(self, x, y, range, power, width, height, end, lives, begin, vel, IA, look)
        self.name = "golem"

    def draw(self, enemy, win):
        self.move(enemy)
        if self.isHitting:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0
                self.isHitting = False
            if self.look == 1:
                win.blit(self.hitRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.hitLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0
            if self.look == 1:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        self.hitbox = (self.x + 17, self.y + 2, 60, 77)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)