from random import *
import pygame
import inputControl
import sys
import time

from ghost import Ghost #pycharm est une pute
from golem import Golem
from human import Human
from goblin import Goblin
from projectile import Projectile

# Game part
pygame.init()

#init parameters with console arguments provided
monster_1, monster_1_ia, monster_2, monster_2_ia, ground = inputControl.control_input(sys.argv)
monster_1_img, monster_2_img = inputControl.init_images_for_score(monster_1, monster_2)

#init screen
bg, music, win, positions_text, positions_monster, ground_max_x = inputControl.init_music_ground_and_positions(ground)
pygame.display.set_caption("Super IA bros")

#init sounds
winSound, looseSound, bulletSound = inputControl.init_game_music()
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

def redrawGameWindow():
    global walkCount
    #draw bg and score area
    win.blit(bg, (0, 0))

    text_lives_monster_1 = font_lives.render("vies restantes : " + str(monster_in_game_1.lives), 1, (255, 0, 0))
    text_percentage_monster_1 = font_percentage.render("degats reçus : "+ str(monster_in_game_1.percentage) +"%", 1, (255, 255, 255))
    text_lives_monster_2 = font_lives.render("vies restantes : " + str(monster_in_game_2.lives), 1, (255, 0, 0))
    text_percentage_monster_2 = font_percentage.render("degats reçus : " + str(monster_in_game_2.percentage) +"%", 1, (255, 255, 255))

    win.blit(text_lives_monster_1, (positions_text[0], positions_text[2]))
    win.blit(text_percentage_monster_1, (positions_text[0], positions_text[3]))
    win.blit(text_lives_monster_2, (positions_text[1], positions_text[2]))
    win.blit(text_percentage_monster_2, (positions_text[1], positions_text[3]))

    #draw monsters
    win.blit(monster_1_img, (positions_monster[0], positions_monster[2]))
    win.blit(monster_2_img, (positions_monster[1], positions_monster[2]))

    monster_in_game_1.draw(monster_in_game_2, win)
    monster_in_game_2.draw(monster_in_game_1, win)

    #draw projectiles
    for bullet_1 in bullets_monster_1:
        bullet_1.draw(win)

    for bullet_2 in bullets_monster_2:
        bullet_2.draw(win)

    #update screen
    pygame.display.update()


# mainloop

#init vars
monster_in_game_1, monster_in_game_2, lives, bullets_monster_1, bullets_monster_2,\
    font_lives, font_percentage, font_test, shootLoop_monster_1, shootLoop_monster_2 \
    = inputControl.init_vars_before_game_loop(monster_1, monster_2, ground, 1, 1, monster_1_ia, monster_2_ia)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(27)

    if randint(0, 9) >= 5:
        monster_in_game_1.canKick(monster_in_game_2, win)
        monster_in_game_2.canKick(monster_in_game_1, win)
    else:
        monster_in_game_2.canKick(monster_in_game_1, win)
        monster_in_game_1.canKick(monster_in_game_2, win)
    #si un monstre est en dehors du terrain, afficher la boucle de loose
    dead_monster = 0
    if monster_in_game_1.x > ground_max_x or monster_in_game_1.x < -10:
        dead_monster = 1
    elif monster_in_game_2.x > ground_max_x or monster_in_game_2.x < -10:
        dead_monster = 2

    if dead_monster != 0:
        if dead_monster == 1:
            lives[0] -= 1
        else:
            lives[1] -= 1

        #si vie d'un personnage == 0, activer fonction de victoire, sinon relancer
        if lives[0] == 0 and lives[1] == 0:
            text_lives_monster_1 = font_lives.render("vies restantes : " + str(lives[0]), 1, (255, 0, 0))
            text_lives_monster_2 = font_lives.render("vies restantes : " + str(lives[1]), 1, (255, 0, 0))
            win.blit(text_lives_monster_1, (positions_text[0], positions_text[2]))
            win.blit(text_lives_monster_2, (positions_text[0], positions_text[2]))

            font_loose, text_loose = inputControl.get_win_text(monster_in_game_1.name, 0)

            win.blit(text_loose, (650 - (text_loose.get_width() / 2), 300))
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(0.8)
            winSound.play()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

        elif lives[0] == 0:
            text_lives_monster_1 = font_lives.render("vies restantes : " + str(lives[0]), 1, (255, 0, 0))
            win.blit(text_lives_monster_1, (positions_text[0], positions_text[2]))

            font_loose, text_loose = inputControl.get_win_text(monster_in_game_2.name, 2)

            win.blit(text_loose, (650 - (text_loose.get_width() / 2), 300))
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(0.8)
            winSound.play()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
        elif lives[1] == 0:
            text_lives_monster_2 = font_lives.render("vies restantes : " + str(lives[1]), 1, (255, 0, 0))
            win.blit(text_lives_monster_2, (positions_text[1], positions_text[2]))

            font_loose, text_loose = inputControl.get_win_text(monster_in_game_1.name, 1)

            win.blit(text_loose, (650 - (text_loose.get_width() / 2), 300))
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(0.8)
            winSound.play()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

        text_pause = font_percentage.render("le joueur " + str(dead_monster) + " est mort, pause temporaire", 1,
                                            (255, 0, 0))
        win.blit(text_pause, (250 - (text_pause.get_width() / 2), 200))
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.music.set_volume(0.8)
        looseSound.play()
        pygame.time.delay(2500)

        del monster_in_game_1
        del monster_in_game_2

        monster_in_game_1 = inputControl.init_monster_in_game(monster_1, 1, ground, lives[0])
        monster_in_game_2 = inputControl.init_monster_in_game(monster_2, 2, ground, lives[1])
        bullets_monster_1 = []
        bullets_monster_2 = []
        shootLoop_monster_1 = 0
        shootLoop_monster_2 = 0



    #Cooldown pour les projectiles
    if shootLoop_monster_1 > 0:
        shootLoop_monster_1 += 1
    if shootLoop_monster_1 > 3:
        shootLoop_monster_1 = 0

    if shootLoop_monster_2 > 0:
        shootLoop_monster_2 += 1
    if shootLoop_monster_2 > 3:
        shootLoop_monster_2 = 0

    #Gestion des projectiles
    for bullet_1 in bullets_monster_1:
        if bullet_1.y - bullet_1.radius < monster_in_game_2.hitbox[1] + monster_in_game_2.hitbox[3] and bullet_1.y + bullet_1.radius > monster_in_game_2.hitbox[
            1]:
            if bullet_1.x + bullet_1.radius > monster_in_game_2.hitbox[0] and bullet_1.x - bullet_1.radius < monster_in_game_2.hitbox[0] + \
                    monster_in_game_2.hitbox[2]:

                monster_in_game_2.hit(monster_in_game_1)
                bullets_monster_1.pop(bullets_monster_1.index(bullet_1))

        if bullet_1.x < ground_max_x  and bullet_1.x > 0:
            bullet_1.x += bullet_1.vel
        else:
            bullets_monster_1.pop(bullets_monster_1.index(bullet_1))

    for bullet_2 in bullets_monster_2:
        if bullet_2.y - bullet_2.radius < monster_in_game_1.hitbox[1] + monster_in_game_1.hitbox[3] and bullet_2.y + bullet_2.radius > monster_in_game_1.hitbox[
            1]:
            if bullet_2.x + bullet_2.radius > monster_in_game_1.hitbox[0] and bullet_2.x - bullet_2.radius < monster_in_game_1.hitbox[0] + \
                    monster_in_game_1.hitbox[2]:
                monster_in_game_1.hit(monster_in_game_2)
                bullets_monster_2.pop(bullets_monster_2.index(bullet_2))
        if bullet_2.x < ground_max_x  and bullet_2.x > 0:
            bullet_2.x += bullet_2.vel
        else:
            bullets_monster_2.pop(bullets_monster_2.index(bullet_2))

    #Tir automatique
    if randint(0, 30) == 5 and shootLoop_monster_1 == 0:
        if monster_in_game_1.look == -1:
            facing_monster_1 = -1
        else:
            facing_monster_1 = 1
        if len(bullets_monster_1) < 5:
            bulletSound.play()
            bullets_monster_1.append(
                Projectile(round(monster_in_game_1.x + monster_in_game_1.width // 2), round(monster_in_game_1.y + monster_in_game_1.height // 2), 6, (0, 0, 0), facing_monster_1))

    if randint(0, 30) == 5 and shootLoop_monster_2 == 0:
        if monster_in_game_2.look == -1:
            facing_monster_2 = -1
        else:
            facing_monster_2 = 1
        if len(bullets_monster_2) < 5:
            bulletSound.play()
            bullets_monster_2.append(
                Projectile(round(monster_in_game_2.x + monster_in_game_2.width // 2), round(monster_in_game_2.y + monster_in_game_2.height // 2), 6, (0, 0, 0), facing_monster_2))

    monster_in_game_1.jump()
    monster_in_game_2.jump()



    #possibilité de quitter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()

pygame.quit()
