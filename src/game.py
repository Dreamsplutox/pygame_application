from random import *
import pygame
import inputControl
import sys

from ghost import Ghost #pycharm est une pute
from golem import Golem
from player import Player
from projectile import Projectile

# Game part
pygame.init()

#init parameters with console arguments provided
monster_1, monster_1_ia, monster_2, monster_2_ia, ground = inputControl.control_input(sys.argv)
monster_1_img, monster_2_img = inputControl.init_images_for_score(monster_1, monster_2)

print("monster 1 = ", monster_1, " monster 2 = ", monster_2)

bg, music, win, positions_text, positions_monster = inputControl.init_music_ground_and_positions(ground)
#win = pygame.display.set_mode((1210, 598))

pygame.display.set_caption("First Game in Python")

#bg = pygame.image.load('images/arene1.jpg')

clock = pygame.time.Clock()

winSound = pygame.mixer.Sound('sounds/win.wav')
looseSound = pygame.mixer.Sound("sounds/loose_zelda.wav")

#music = pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


def redrawGameWindow():
    global walkCount
    #draw bg and score area
    win.blit(bg, (0, 0))
    #pygame.draw.rect(win, (0, 0, 0), (0, 0, 1210, 110))
    text_lives_monster_1 = font_lives.render("vies restantes : 3", 1, (255, 0, 0))
    text_percentage_monster_1 = font_percentage.render("degats reçus : 50%", 1, (255, 255, 255))
    text_lives_monster_2 = font_lives.render("vies restantes : 2", 1, (255, 0, 0))
    text_percentage_monster_2 = font_percentage.render("degats reçus : 74%", 1, (255, 255, 255))
    win.blit(text_lives_monster_1, (positions_text[0], positions_text[2]))
    win.blit(text_percentage_monster_1, (positions_text[0], positions_text[3]))
    win.blit(text_lives_monster_2, (positions_text[1], positions_text[2]))
    win.blit(text_percentage_monster_2, (positions_text[1], positions_text[3]))
    #draw monsters + score
    win.blit(monster_1_img, (positions_monster[0], positions_monster[2]))
    win.blit(monster_2_img, (positions_monster[1], positions_monster[2]))

    man.draw(win)
    ghost.draw(win)
    golem.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# mainloop
font_lives = pygame.font.SysFont('comicsans', 25, True)
font_percentage = pygame.font.SysFont('comicsans', 28)
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
