from random import *
import pygame
import inputControl
import sys

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
    text_monster_number_1 = font_monster_number.render("J1", 1, (255, 140, 0), True)
    text_monster_number_2 = font_monster_number.render("J2", 1, (255,69,0), True)

    win.blit(text_lives_monster_1, (positions_text[0], positions_text[2]))
    win.blit(text_percentage_monster_1, (positions_text[0], positions_text[3]))
    win.blit(text_lives_monster_2, (positions_text[1], positions_text[2]))
    win.blit(text_percentage_monster_2, (positions_text[1], positions_text[3]))
    win.blit(text_monster_number_1, (monster_in_game_1.x + monster_in_game_1.width // 2.2, monster_in_game_1.y - 30))
    win.blit(text_monster_number_2, (monster_in_game_2.x + monster_in_game_2.width // 2.9, monster_in_game_2.y - 30))

    #draw monsters
    win.blit(monster_1_img, (positions_monster[0], positions_monster[2]))
    win.blit(monster_2_img, (positions_monster[1], positions_monster[2]))

    monster_in_game_1.draw(monster_in_game_2, win)
    monster_in_game_2.draw(monster_in_game_1, win)

    #draw monster number at the top


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
    font_lives, font_percentage, font_test, font_monster_number, shootLoop_monster_1, shootLoop_monster_2 \
    = inputControl.init_vars_before_game_loop(monster_1, monster_2, ground, 1, 1, monster_1_ia, monster_2_ia)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(27)

    #random pour savoir qui a la priorité pour kick
    inputControl.monster_can_kick(monster_in_game_1, monster_in_game_2, win)

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

        if lives[0] > 0 and lives[1] > 0:
            text_pause = font_percentage.render("le joueur " + str(dead_monster) + " est mort, pause temporaire", 1,
                                                (255, 0, 0))
            win.blit(text_pause, (250 - (text_pause.get_width() / 2), 200))
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(0.8)
            looseSound.play()
            pygame.time.delay(2500)

            monster_1_ia = monster_in_game_1.IA
            monster_2_ia = monster_in_game_2.IA

            del monster_in_game_1
            del monster_in_game_2

            monster_in_game_1 = inputControl.init_monster_in_game(monster_1, 1, ground, lives[0], monster_1_ia)
            monster_in_game_2 = inputControl.init_monster_in_game(monster_2, 2, ground, lives[1], monster_2_ia)
            bullets_monster_1 = []
            bullets_monster_2 = []
            shootLoop_monster_1 = 0
            shootLoop_monster_2 = 0
            #pause_before_restart(monster_1, monster_2, monster_in_game_1, monster_in_game_2, ground, lives, font_percentage, dead_monster, win, looseSound)

        else:
            print("end")
            monster_in_game_1, monster_in_game_2, bullets_monster_1, bullets_monster_2, shootLoop_monster_1, shootLoop_monster_2, text_pause = \
                inputControl.game_win(monster_in_game_1, monster_in_game_2, lives, font_lives, positions_text, win,
                                  winSound)

    #Cooldown pour les projectiles
    shootLoop_monster_1, shootLoop_monster_2 = inputControl.cooldown_for_projectiles(shootLoop_monster_1, shootLoop_monster_2)

    #Gestion des projectiles

    #mise à jour projectile du monstre 1
    bullets_monster_1 = inputControl.update_projectiles(bullets_monster_1, monster_in_game_1, monster_in_game_2, ground_max_x)

    # mise à jour projectile du monstre 1
    bullets_monster_2 = inputControl.update_projectiles(bullets_monster_2, monster_in_game_2, monster_in_game_1, ground_max_x)

    #Tir automatique
    if randint(0, 40) == 5 and shootLoop_monster_1 == 0:
        if monster_in_game_1.look == -1:
            facing_monster_1 = -1
        else:
            facing_monster_1 = 1
        if len(bullets_monster_1) < 5:
            bulletSound.play()
            bullets_monster_1.append(
                Projectile(round(monster_in_game_1.x + monster_in_game_1.width // 2), round(monster_in_game_1.y + monster_in_game_1.height // 2), 6, (0, 0, 0), facing_monster_1))

    if randint(0, 40) == 5 and shootLoop_monster_2 == 0:
        if monster_in_game_2.look == -1:
            facing_monster_2 = -1
        else:
            facing_monster_2 = 1
        if len(bullets_monster_2) < 5:
            bulletSound.play()
            bullets_monster_2.append(
                Projectile(round(monster_in_game_2.x + monster_in_game_2.width // 2), round(monster_in_game_2.y + monster_in_game_2.height // 2), 6, (0, 0, 0), facing_monster_2))

    #déclenchement des sauts si jamais l'attribut isJump a été passé à True
    monster_in_game_1.jump()
    monster_in_game_2.jump()



    #possibilité de quitter en cliquant sur la croix rouge en haut à droite
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update l'affichage
    redrawGameWindow()

pygame.quit()
