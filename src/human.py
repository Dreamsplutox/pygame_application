import pygame
from monster import Monster

pygame.init()


looseSound = pygame.mixer.Sound("sounds/loose_zelda.wav")

font = pygame.font.SysFont('comicsans', 30, True)


class Human(Monster):
    walkRight = [pygame.image.load('images/human/R1.png'), pygame.image.load('images/human/R2.png'),
                 pygame.image.load('images/human/R3.png'), pygame.image.load('images/human/R4.png'),
                 pygame.image.load('images/human/R5.png'), pygame.image.load('images/human/R6.png'),
                 pygame.image.load('images/human/R7.png'), pygame.image.load('images/human/R8.png'),
                 pygame.image.load('images/human/R9.png')]
    walkLeft = [pygame.image.load('images/human/L1.png'), pygame.image.load('images/human/L2.png'),
                pygame.image.load('images/human/L3.png'), pygame.image.load('images/human/L4.png'),
                pygame.image.load('images/human/L5.png'), pygame.image.load('images/human/L6.png'),
                pygame.image.load('images/human/L7.png'), pygame.image.load('images/human/L8.png'),
                pygame.image.load('images/human/L9.png')]

    def __init__(self, x, y, end, lives, begin=0, IA='random', look=1):
        Monster.__init__(self, x, y, 10, 15, 40, 60, 6, 40, 8, end, lives, begin, 4, IA, look)
        self.name = "human"

    def draw(self, enemy, win):
        self.move(enemy)
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.look == 1:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        self.hitbox = (self.x + 10, self.y + 10, self.width, self.height)