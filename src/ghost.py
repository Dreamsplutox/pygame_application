import pygame
from monster import Monster
pygame.init()


class Ghost(Monster):
    walkRight = [pygame.image.load('images/ghost/fantomeR1.png'), pygame.image.load('images/ghost/fantomeR2.png'),
                 pygame.image.load('images/ghost/fantomeR3.png'), pygame.image.load('images/ghost/fantomeR4.png'),
                 pygame.image.load('images/ghost/fantomeR5.png'), pygame.image.load('images/ghost/fantomeR6.png'),
                 pygame.image.load('images/ghost/fantomeR7.png'), pygame.image.load('images/ghost/fantomeR8.png'),
                 pygame.image.load('images/ghost/fantomeR9.png'), pygame.image.load('images/ghost/fantomeR10.png')]
    walkLeft = [pygame.image.load('images/ghost/fantomeL1.png'), pygame.image.load('images/ghost/fantomeL2.png'),
                pygame.image.load('images/ghost/fantomeL3.png'), pygame.image.load('images/ghost/fantomeL4.png'),
                pygame.image.load('images/ghost/fantomeL5.png'), pygame.image.load('images/ghost/fantomeL6.png'),
                pygame.image.load('images/ghost/fantomeL7.png'), pygame.image.load('images/ghost/fantomeL8.png'),
                pygame.image.load('images/ghost/fantomeL9.png'), pygame.image.load('images/ghost/fantomeL10.png')]

    def __init__(self, x, y, range, power, width, height, end, lives, begin=0, vel=3, IA='random', look=1):
        Monster.__init__(self, x, y, range, power, width, height, end, lives, begin, vel, IA, look)
        self.name = "ghost"

    def draw(self, enemy, win):
        self.move(enemy)
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        if self.look == 1:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        self.hitbox = (self.x + 10, self.y - 10, 25, 55)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)