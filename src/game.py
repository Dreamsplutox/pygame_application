from random import *
import pygame

from ghost import Ghost #pycharm est une pute
from golem import Golem
from player import Player
from src.projectile import Projectile

# Game part
pygame.init()

win = pygame.display.set_mode((1200, 675))

pygame.display.set_caption("First Game in Python")

bg = pygame.image.load('images/bg.jpg')

clock = pygame.time.Clock()

winSound = pygame.mixer.Sound('sounds/win.wav')
looseSound = pygame.mixer.Sound("sounds/loose_zelda.wav")

music = pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))

    man.draw(win)
    ghost.draw(win)
    golem.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# mainloop
font = pygame.font.SysFont('comicsans', 30, True)
fontB = pygame.font.SysFont('comicsans', 18, False, True)
man = Player(300, 410, 64, 64)
golem = Golem(300, 380, 64, 64, 370, 5)
ghost = Ghost(100, 410, 64, 64, 450, 5)
shootLoop = 0
bullets = []
run = True

while run:
    clock.tick(27)

    # win condition
    if man.score >= 10:
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.music.set_volume(0.8)
        winSound.play()

    # del goblin
    # goblin = Enemy(randint(90,400), 410, 64, 64, 450)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= - 10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()

pygame.quit()
