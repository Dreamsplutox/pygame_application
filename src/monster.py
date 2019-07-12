import pygame
pygame.init()

looseSound = pygame.mixer.Sound("sounds/loose_zelda.wav")

class Monster(object):
    def __init__(self, x, y, width, height, end, lives, begin=0, left=True, vel=3):
        self.x = x
        self.y = y
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

    def hit(self, direction, limit, win):
        self.percentage += 100
        # décalage gauche ou droite
        if direction == -1:
            self.x = self.x - (self.percentage)
        else:
            self.x = self.x + (self.percentage)
        # restart condition, for now pause the game, we will see that later
            '''
            font1 = pygame.font.SysFont('comicsans', 28, True)
            text = font1.render("Un joueur est tombé, pause temporaire", 1, (255, 0, 0))
            win.blit(text, (250 - (text.get_width() / 2), 200))
            self.draw(win)
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(0.8)
            looseSound.play()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            '''
        if self.health > 1:
            self.health -= 1
        else:
            wait = 1
            #self.alive = False
    # print('hit')
