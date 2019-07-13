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

    def move(self, enemy):
        actual = abs(self.x - enemy.x)
        test = abs(self.x + self.look - enemy.x)
        newDirection = 0

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
            if test >= actual:
                self.x -= self.vel
                newDirection = -1
            else:
                self.x += self.vel
                newDirection = 1

        # on regarde dans une nouvelle direction
        if newDirection != self.look:
            self.walkCount = 0

    def canKick(self, enemy, win):
        if self.cooldown <= 0:
            self.kick(enemy, win)
        else:
            self.cooldown -= self.vel

    def kick(self, enemy,win):
        if abs(self.x - enemy.x) <= self.range:
            self.isHitting = True
            self.draw(enemy, win)
            enemy.hit(self)
            enemy.knockBack(self.look)
            self.cooldown = 50
            if abs(self.x - enemy.x) <= enemy.range:
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
