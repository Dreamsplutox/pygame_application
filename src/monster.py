import pygame
import random
pygame.init()

looseSound = pygame.mixer.Sound("sounds/loose_zelda.wav")

class Monster(object):
    def __init__(self, x, y, range, power, width, height, end, lives, begin=0, left=True, vel=3, IA='agressive', look=1):
        self.x = x
        self.y = y
        self.IA = IA
        self.range = range + width
        self.power = power
        self.cooldown = 0
        self.direction = 0 #pas sur utilisé
        self.width = width
        self.height = height
        self.path = [begin, end]
        self.walkCount = 0 #statut pour l'affichage du personnage ==> 1 image pour 3 frames
        self.vel = vel #vitesse
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) #à modifier selon la taille du personnage
        self.health = 10 #la vie
        self.alive = True #est-il en vie?
        self.lives = lives
        self.left = left
        self.percentage = 0
        self.look = look
        self.resistance = 0
        self.choice = IA
        self.isHitting = False
        self.isJump = False
        self.jumpCount = 10

    def move(self, enemy):
        actual = abs(self.x - enemy.x)
        test = abs(self.x + self.look - enemy.x)
        test_fuyarde = self.x + self.vel * self.look * -1
        newDirection = 0

        if self.x > enemy.x and self.isJump == False:
            self.look = -1
        elif self.x < enemy.x and self.isJump == False:
            self.look = 1

        if self.IA == 'random':
            if random.randint(0, 100) == 1:
                choice = random.choice('afj')
                if choice == 'a':
                    self.choice = 'agressive'
                elif choice == 'f':
                    self.choice = 'fuyarde'
                else:
                    print('player is jumping')
        if self.choice == 'agressive':
            if test <= actual:
                self.x += self.vel * self.look
                newDirection = 1 * self.look
            else:
                self.x -= self.vel * self.look
                newDirection = -1 * self.look
        elif self.choice == 'fuyarde':
            print("path 0 = ", self.path[0], "path 1 = ", self.path[1], "width = ", self.width, "look = ", self.look, "tes2t = ", test_fuyarde)
            if actual < 1.5 * self.range:
                print('jump fdp')
                self.isJump = True
            elif test_fuyarde <= self.path[0] or test_fuyarde >= self.path[1] - self.width:
                print("don't move")
            else:
                print("move fuyarde")
                if test <= actual :
                    self.x -= self.vel * self.look
                    newDirection = 1 * self.look
                else:
                    self.x += self.vel * self.look
                    newDirection = -1 * self.look

        # on regarde dans une nouvelle direction
        if newDirection != self.look:
            self.walkCount = 0

    def canKick(self, enemy, win):
        if self.cooldown <= 0:
            self.kick(enemy, win)
        else:
            self.cooldown -= self.vel

    def kick(self, enemy,win):
        diff = abs(self.y - enemy.y)
        if abs(self.x - enemy.x) <= self.range and diff <= self.height:
            self.isHitting = True
            self.draw(enemy, win)
            enemy.hit(self)
            enemy.knockBack(self.look)
            self.cooldown = 50
            if abs(self.x - enemy.x) <= enemy.range and diff <= enemy.height:
                enemy.isHitting = True
                enemy.draw(enemy, win)
                self.hit(enemy)
                self.knockBack(enemy.look)
                enemy.cooldown = 50

    def hit(self, enemy):
        self.percentage += (enemy.power - self.resistance)

    def knockBack(self, direction):
        if direction == -1:
            self.x = self.x - (self.percentage)
        else:
            self.x = self.x + (self.percentage)

    def jump(self):
        if self.isJump == True:
            if self.jumpCount >= - 10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.2 * neg
                self.x += self.look * self.vel * 6
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10


