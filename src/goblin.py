import pygame
from monster import Monster

pygame.init()

looseSound = pygame.mixer.Sound("sounds/loose_zelda.wav")

class Goblin(Monster):
    walkRight = [pygame.image.load('images/goblin/R1E.png'), pygame.image.load('images/goblin/R2E.png'),
                 pygame.image.load('images/goblin/R3E.png'), pygame.image.load('images/goblin/R4E.png'),
                 pygame.image.load('images/goblin/R5E.png'), pygame.image.load('images/goblin/R6E.png'),
                 pygame.image.load('images/goblin/R7E.png'), pygame.image.load('images/goblin/R8E.png'),
                 pygame.image.load('images/goblin/R9E.png'), pygame.image.load('images/goblin/R10E.png'),
                 pygame.image.load('images/goblin/R11E.png')]
    walkLeft = [pygame.image.load('images/goblin/L1E.png'), pygame.image.load('images/goblin/L2E.png'),
                pygame.image.load('images/goblin/L3E.png'), pygame.image.load('images/goblin/L4E.png'),
                pygame.image.load('images/goblin/L5E.png'), pygame.image.load('images/goblin/L6E.png'),
                pygame.image.load('images/goblin/L7E.png'), pygame.image.load('images/goblin/L8E.png'),
                pygame.image.load('images/goblin/L9E.png'), pygame.image.load('images/goblin/L10E.png'),
                pygame.image.load('images/goblin/L11E.png')]

    def __init__(self, x, y, range, power, width, height, end, lives, begin=0, left=True, vel=3, IA='random', look=1):
        Monster.__init__(self, x, y, range, power, width, height, end, lives, begin, left, vel, IA, look)
        self.isJumping = False
        self.jump = 10
        self.name = "golem"

    def draw(self, enemy, win):
        self.move(enemy)
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
        # self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.hitbox = (self.x + 17, self.y + 2, 60, 77)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
