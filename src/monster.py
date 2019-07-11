import pygame

pygame.init()

class Monster(object):
    def __init__(self, x, y, width, height, end, lives, begin=0, left=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [begin, end]
        self.walkCount = 0 #statut pour l'affichage du personnage ==> 1 image pour 3 frames
        self.vel = 3 #vitesse
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) #à modifier selon la taille du personnage
        self.health = 10 #la vie
        self.alive = True #est-il en vie?
        self.lives = lives
        self.left = left

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
            self.alive = False
    # print('hit')
