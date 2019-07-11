import pygame

pygame.init()

class Enemy(object):
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

    def __init__(self, x, y, width, height, end, begin=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [begin, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                self.left = False
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                self.left = True
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            #pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) #vie totale
            #pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) #vie restante
            self.hitbox = (self.x + 23, self.y - 10 , 31, 69)
            pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
    # print('hit')
