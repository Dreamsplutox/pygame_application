from random import *
import psycopg2 as p
import pygame

from src.goblin import Enemy
from src.human import Player
from src.projectile import Projectile

con = p.connect("dbname='python_game_data' user='postgres' host='192.168.99.100' password='postgres'")
cur = con.cursor()
cur.execute("select * from game_text")
rows = cur.fetchall()

cur.execute("select score from scores ORDER BY score DESC")
score = cur.fetchall()

# Game part
pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game in Python")

bg = pygame.image.load('images/bg.jpg')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('sounds/bullet.wav')
hitSound = pygame.mixer.Sound('sounds/hit.wav')
screamSound = pygame.mixer.Sound('sounds/scream.wav')
deathSound = pygame.mixer.Sound('sounds/goblin_death_2.wav')
winSound = pygame.mixer.Sound('sounds/win.wav')
looseSound = pygame.mixer.Sound("sounds/loose_zelda.wav")

music = pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))

    textB = fontB.render(rows[0][2], 1, (0, 0, 128))
    textC = font.render('Lives ' + str(man.lives), 1, (200, 0, 0))

    if man.score > score[0][0]:
        text = font.render('Score: ' + str(man.score), 1, (255, 128, 0))
        textD = font.render('Record: ' + str(man.score), 1, (255, 128, 0))
    else:
        text = font.render('Score: ' + str(man.score), 1, (0, 0, 0))
        textD = font.render('Record: ' + str(score[0][0]), 1, (255, 128, 0))

    win.blit(text, (360, 10))
    win.blit(textB, (10, 50))
    win.blit(textC, (10, 10))
    win.blit(textD, (360, 32))

    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# mainloop
font = pygame.font.SysFont('comicsans', 30, True)
fontB = pygame.font.SysFont('comicsans', 18, False, True)
man = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
wait_for_Enemy = False

while run:
    clock.tick(27)

    # win condition
    if man.score >= 2000:
        font1 = pygame.font.SysFont('comicsans', 23, True)
        text = font1.render(rows[2][2], 1, (0, 128, 0))
        win.blit(text, (250 - (text.get_width() / 2), 230))
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.music.set_volume(0.8)
        winSound.play()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cur.execute("INSERT INTO scores (score) VALUES (%s);", (man.score,))
                    con.commit()
                    pygame.quit()
                    break

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                screamSound.play()
                man.hit(win)
                man.score -= 5
    elif wait_for_Enemy == 0:
        pygame.mixer.stop()
        deathSound.play()
        wait_for_Enemy = 50

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[
            1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                    goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                man.score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0 and goblin.visible == True:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(
                Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1

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

    if wait_for_Enemy > 0:
        wait_for_Enemy -= 1
        if wait_for_Enemy == 0:
            del goblin
            goblin = Enemy(randint(90, 400), 410, 64, 64, 450)
    redrawGameWindow()

pygame.quit()
