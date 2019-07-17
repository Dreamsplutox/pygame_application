import pygame
import random
pygame.init()

looseSound = pygame.mixer.Sound("sounds/loose_zelda.wav")
muda = pygame.mixer.Sound("sounds/MUDA.wav")
muda.set_volume(0.3)
ora = pygame.mixer.Sound("sounds/ORA.wav")
ora.set_volume(0.4)

class Monster(object):
    def __init__(self, x, y, range, power, width, height, end, lives, begin=0, vel=3, IA='agressive', look=1):
        self.x = x  # position x du monstre
        self.y = y  # position y du monstre
        self.IA = IA  # type IA du monstre
        self.range = range + width  # portée d'attaque du monstre
        self.power = power  # puissance du monstre
        self.cooldown = 0  # temps de recharge avant prochaine attaque au corps à corps (pour éviter les spams)
        self.width = width  # largeur du monstre
        self.height = height  # hauteur du monstre
        self.path = [begin, end]  # zone de déplacement autorisée pour le monstre ==> évite de sortir de la carte
        self.walkCount = 0  # statut pour l'affichage du personnage ==> 1 image pour 3 frames
        self.vel = vel  # vitesse du monstre
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)  # à modifier selon la taille du monstre
        self.health = 10  # la vie
        self.lives = lives  # nombre de vie, détermine la manche
        self.percentage = 0  # c'est smash
        self.look = look  # direction dans laquelle il regarde
        self.resistance = 0  # résistance aux dégats
        self.choice = IA  # dans le cas où l'IA est une IA random
        self.isHitting = False  # savoir s'il tape pour la représentation (voir partie draw des autres clases
        self.isJump = False  # savoir s'il est en plein saut (pour animation
        self.jumpCount = 10  # hauteur du saut
        self.isKnockingBack = False
        self.knockBackCount = 10
        random.randint(0,1)
        if random.randint(0,1) == 0 :
            self.hitSound = muda
        else:
            self.hitSound = ora

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
            if random.randint(0, 100) == 1 or self.choice == "random":
                choice = random.choice('afj')
                if choice == 'a':
                    self.choice = 'agressive'
                elif choice == 'f':
                    self.choice = 'fuyarde'
                if choice == 'j':
                    self.isJump = True

        elif self.IA == 'try':
            if self.percentage > enemy.percentage:
                self.choice = 'fuyarde'
            else:
                self.choice = 'agressive'

        if self.choice == 'agressive':
            if enemy.percentage >= 250 or self.cooldown <= 0:
                self.choice == 'fuyarde'
            if test <= actual:
                self.x += self.vel * self.look
                newDirection = 1 * self.look
            else:
                self.x -= self.vel * self.look
                newDirection = -1 * self.look

        elif self.choice == 'fuyarde':
            if enemy.percentage >= 250:
                self.choice == 'agressive'
            if actual < 1.5 * self.range:
                self.isJump = True
            elif test_fuyarde <= self.path[0] or test_fuyarde >= self.path[1] - self.width:
                print("don't move")
            else:
                if test <= actual :
                    self.x -= self.vel * self.look
                    newDirection = 1 * self.look
                else:
                    self.x += self.vel * self.look
                    newDirection = -1 * self.look

        #on regarde dans une nouvelle direction
        if newDirection != self.look:
            self.walkCount = 0

    def canKick(self, enemy, win):
        if self.cooldown <= 0:
            self.kick(enemy, win)
        else:
            self.cooldown -= self.vel

    def kick(self, enemy,win):
        diff = abs(self.y - enemy.y)
        if abs(self.x - enemy.x) <= self.range and diff <= self.height - 10:
            self.isHitting = True
            self.hitSound.play()
            self.draw(enemy, win)
            enemy.hit(self)
            enemy.isKnockingBack = True
            self.cooldown = 70
            if abs(self.x - enemy.x) <= enemy.range and diff <= enemy.height - 10:
                enemy.isHitting = True
                enemy.draw(enemy, win)
                self.hit(enemy)
                self.isKnockingBack = True
                enemy.cooldown = 70

    def hit(self, enemy):
        self.percentage += (enemy.power - self.resistance)

    def knockBack(self, direction):
        if self.isKnockingBack:
            if self.knockBackCount >= - 10:
                neg = 1
                if self.knockBackCount < 0:
                    neg = -1

                self.y -= (self.knockBackCount ** 2) * 0.02 * neg
                self.x += direction * self.percentage * 0.1
                self.knockBackCount -= 1
            else:
                self.isKnockingBack = False
                self.knockBackCount = 10

    def jump(self):
        if self.isJump:
            calcul = self.x + (self.look * self.vel * 6) * 20
            if calcul < self.path[0] or calcul > self.path[1]:
                self.look *= -1
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


