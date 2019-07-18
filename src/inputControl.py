from random import *
import sys
import pygame

from ghost import Ghost #pycharm est une pute
from golem import Golem
from human import Human
from goblin import Goblin
from projectile import Projectile

pygame.init()

def control_input(arguments):
    list_monsters = ["ghost", "golem", "human", "goblin"]
    list_ia = ["agressive", "fuyarde", "random", "try"]
    list_grounds = ["1", "2", "3"]

    if len(arguments) < 6:
        if len(arguments) == 1:
            monster_1 = list_monsters[randint(0,3)]
            monster_1_ia = list_ia[randint(0,2)]
            monster_2 = list_monsters[randint(0,3)]
            monster_2_ia = list_ia[randint(0,2)]
            ground = list_grounds[randint(0,2)]
            return monster_1, monster_1_ia, monster_2, monster_2_ia, ground
        print("Pas assez d'arguments entrés ! Il faut en entrer 5")
        sys.exit()
    else:
        #tests to verify the parameters
        if arguments[1] == list_monsters[0] or arguments[1] == list_monsters[1] or arguments[1] == list_monsters[2] or arguments[1] == list_monsters[3] or arguments[1] == "random":
            if arguments[1] == "random":
                monster_1 = list_monsters[randint(0,3)]
            else:
                monster_1 = arguments[1]
        else:
            print("Ce personnage n'existe pas, choisissez entre golem, ghost, human ou goblin")
            sys.exit()
    
        if arguments[2] == "agressive" or arguments[2] == "fuyarde" or arguments[2] == "random" or arguments[2] == "try":
            monster_1_ia = arguments[2]
        else:
            print("Cette ia (", arguments[2], ") n'existe pas, choisissez entre agressive, fuyarde, op ou random")
            sys.exit()
    
        if  arguments[3] == list_monsters[0] or arguments[3] == list_monsters[1] or arguments[3] == list_monsters[2] or arguments[3] == list_monsters[3] or arguments[3] == "random":
            if arguments[1] == "random":
                monster_2 = list_monsters[randint(0,3)]
            else:
                monster_2 = arguments[3]
        else:
            print("Ce personnage n'existe pas, choisissez entre golem, ghost, human ou goblin")
            sys.exit()
    
        if arguments[4] == "agressive" or arguments[4] == "fuyarde" or arguments[4] == "random" or arguments[4] == "try":
            monster_2_ia = arguments[4]
        else:
            print("Cette ia (", arguments[4], ") n'existe pas, choisissez entre agressive, fuyarde, op ou random")
            sys.exit()
    
        if arguments[5] == '1' or arguments[5] == '2' or arguments[5] == '3':
            ground = arguments[5]
        else:
            print("ce terrain n'existe pas, choisissez un terrain entre 1 et 3")
            sys.exit()

        return monster_1, monster_1_ia, monster_2, monster_2_ia, ground

def init_music_ground_and_positions(ground):
    if ground == "1":
        bg = pygame.image.load('images/arene1.jpg')
        music = pygame.mixer.music.load('sounds/musiques/musicArene1.mp3')
        win = pygame.display.set_mode((1210, 598))
        positions_text = [130, 900, 17, 47]
        positions_monster = [10, 1120, 7]
        ground_max_x = 1210
    elif ground == "2":
        bg = pygame.image.load('images/arene2.png')
        music = pygame.mixer.music.load('sounds/musiques/musicArene2.mp3')
        win = pygame.display.set_mode((1100, 675))
        positions_text = [130, 800, 17, 47]
        positions_monster = [10, 1020, 7]
        ground_max_x = 1100
    else:
        bg = pygame.image.load('images/arene3.png')
        music = pygame.mixer.music.load('sounds/musiques/musicArene3.mp3')
        win = pygame.display.set_mode((1050, 590))
        positions_text = [130, 750, 17, 47]
        positions_monster = [10, 970, 7]
        ground_max_x = 1050

    return bg, music, win, positions_text, positions_monster, ground_max_x

def init_images_for_score(monster_1, monster_2):
    list_monsters = ["ghost", "golem", "human", "goblin"]
    #select good image for monster_1
    if monster_1 == list_monsters[0]:
        monster_1_img = pygame.image.load('images/ghost/ghost_char_R.png')
    elif monster_1 == list_monsters[1]:
        monster_1_img = pygame.image.load('images/golem/golem_char_R.png')
    elif monster_1 == list_monsters[2]:
        monster_1_img = pygame.image.load('images/human/human_char_R.png')
    else:
        monster_1_img = pygame.image.load('images/goblin/goblin_char_R.png')

    #select good image for monster_2
    if monster_2 == list_monsters[0]:
        monster_2_img = pygame.image.load('images/ghost/ghost_char_L.png')
    elif monster_2 == list_monsters[1]:
        monster_2_img = pygame.image.load('images/golem/golem_char_L.png')
    elif monster_2 == list_monsters[2]:
        monster_2_img = pygame.image.load('images/human/human_char_L.png')
    else:
        monster_2_img = pygame.image.load('images/goblin/goblin_char_L.png')

    return monster_1_img, monster_2_img

def init_monster_in_game(monster_name, monster_number, ground, lives, IA):
    list_monsters = ["ghost", "golem", "human", "goblin"]
    if ground == "1":
        start_x_monster_1 = 60
        start_x_monster_2 = 850
        end = 1210
    elif ground == "2":
        start_x_monster_1 = 60
        start_x_monster_2 = 740
        end = 1100
    else:
        start_x_monster_1 = 350
        start_x_monster_2 = 650
        end = 1050

    if monster_number == 1:
        if monster_name == list_monsters[0]:
            monster = Ghost(start_x_monster_1, 417, end, lives, 0, IA, 1)
        elif monster_name == list_monsters[1]:
            monster = Golem(start_x_monster_1, 410, end, lives, 0, IA, 1)
        elif monster_name == list_monsters[2]:
            monster = Human(start_x_monster_1, 420, end, lives, 0, IA, 1)
        else:
            monster = Goblin(start_x_monster_1, 430, end, lives, 0, IA, 1)
    else:
        if monster_name == list_monsters[0]:
            monster = Ghost(start_x_monster_2, 417, end, lives, 0, IA, 1)
        elif monster_name == list_monsters[1]:
            monster = Golem(start_x_monster_2, 410, end, lives, 0, IA, -1)
        elif monster_name == list_monsters[2]:
            monster = Human(start_x_monster_2, 420, end, lives, 0, IA, -1)
        else:
            monster = Goblin(start_x_monster_2, 430, end, lives, 0, IA, -1)

    return monster

def get_win_text(monster_name, winner=1):
    if winner == 0:
        my_font = pygame.font.SysFont('comicsans', 75, True)
        my_text = my_font.render("Egalité !", 1, (0, 0, 0))
    elif winner == 1:
        if monster_name == "ghost":
            my_font = pygame.font.Font("fonts/ghost.otf", 100)
            my_text = my_font.render("VICTOIRE DU JOUEUR 1 !", 1,  (200, 200, 200) , True)
        elif monster_name == "human":
            my_font = pygame.font.Font("fonts/human.ttf", 65)
            my_text = my_font.render("Victoire du joueur 1 !", 1,  (255, 215, 0))
        elif monster_name == "golem":
            my_font = pygame.font.Font("fonts/golem.ttf", 65)
            my_text = my_font.render("Victoire du joueur 1 !", 1, (142, 84, 52))
        else:
            my_font = pygame.font.Font("fonts/goblin.ttf", 75)
            my_text = my_font.render("Victoire du joueur 1 !", 1, (127, 221, 76), True)
    else:
        if monster_name == "ghost":
            my_font = pygame.font.Font("fonts/ghost.otf", 100)
            my_text = my_font.render("VICTOIRE DU JOUEUR 2 !", 1, (200, 200, 200), True)
        elif monster_name == "human":
            my_font = pygame.font.Font("fonts/human.ttf", 65)
            my_text = my_font.render("Victoire du joueur 2 !", 1,  (255, 215, 0))
        elif monster_name == "golem":
            my_font = pygame.font.Font("fonts/golem.ttf", 65)
            my_text = my_font.render("Victoire du joueur 2 !", 1, (142, 84, 52))
        else:
            my_font = pygame.font.Font("fonts/goblin.ttf", 75)
            my_text = my_font.render("Victoire du joueur 2 !", 1, (127, 221, 76), True)

    return my_font, my_text

def init_vars_before_game_loop(monster_1, monster_2, ground, lives_monster_1, lives_monster_2, ia_monster_1, ia_monster_2):
    monster_in_game_shooter = init_monster_in_game(monster_1, 1, ground, lives_monster_1, ia_monster_1)
    monster_in_game_damaged = init_monster_in_game(monster_2, 2, ground, lives_monster_2, ia_monster_2)

    lives = [lives_monster_1, lives_monster_2]

    bullets_monster_1 = []
    bullets_monster_2 = []

    font_lives = pygame.font.SysFont('comicsans', 25, True)
    font_percentage = pygame.font.SysFont('comicsans', 28)
    font_test = pygame.font.Font("fonts/ghost.ttf", 26)
    font_monster_number = pygame.font.SysFont('comicsans', 30)

    shootLoop_monster_1 = 0
    shootLoop_monster_2 = 0

    return monster_in_game_shooter, monster_in_game_damaged, lives, bullets_monster_1, bullets_monster_2, font_lives, font_percentage, font_test, font_monster_number, shootLoop_monster_1, shootLoop_monster_2

def init_game_music():
    winSound = pygame.mixer.Sound('sounds/win.wav')
    looseSound = pygame.mixer.Sound("sounds/loose_zelda.wav")
    bulletSound = pygame.mixer.Sound("sounds/bullet.wav")

    return winSound, looseSound, bulletSound

def cooldown_for_projectiles(shootLoop_monster_1, shootLoop_monster_2):
    if shootLoop_monster_1 > 0:
        shootLoop_monster_1 += 1
    if shootLoop_monster_1 > 3:
        shootLoop_monster_1 = 0

    if shootLoop_monster_2 > 0:
        shootLoop_monster_2 += 1
    if shootLoop_monster_2 > 3:
        shootLoop_monster_2 = 0

    return shootLoop_monster_1, shootLoop_monster_2

def update_projectiles(bullets_monster, monster_in_game_shooter , monster_in_game_damaged, ground_max_x):
    for bullet in bullets_monster:
        if bullet.y - bullet.radius < monster_in_game_damaged.hitbox[1] + monster_in_game_damaged.hitbox[3] \
                and bullet.y + bullet.radius > monster_in_game_damaged.hitbox[1]:
            if bullet.x + bullet.radius > monster_in_game_damaged.hitbox[0] and bullet.x - bullet.radius < \
                    monster_in_game_damaged.hitbox[0] + monster_in_game_damaged.hitbox[2]:
                monster_in_game_damaged.hit(monster_in_game_shooter)
                if monster_in_game_damaged.percentage > 150:
                    if(bullet.x < monster_in_game_damaged.x):
                        monster_in_game_damaged.knockBack(1, -2)
                    else:
                        monster_in_game_damaged.knockBack(-1, -2)
                bullets_monster.pop(bullets_monster.index(bullet))

        if bullet.x < ground_max_x and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets_monster.pop(bullets_monster.index(bullet))
    return bullets_monster

def monster_can_kick(monster_in_game_1, monster_in_game_2, win):
    if randint(0, 9) >= 5:
        monster_in_game_1.canKick(monster_in_game_2, win)
        monster_in_game_2.canKick(monster_in_game_1, win)
    else:
        monster_in_game_2.canKick(monster_in_game_1, win)
        monster_in_game_1.canKick(monster_in_game_2, win)

def game_win(monster_in_game_1, monster_in_game_2, lives, font_lives, positions_text, win, winSound):
    if lives[0] == 0 and lives[1] == 0:
        text_lives_monster_1 = font_lives.render("vies restantes : " + str(lives[0]), 1, (255, 0, 0))
        text_lives_monster_2 = font_lives.render("vies restantes : " + str(lives[1]), 1, (255, 0, 0))
        win.blit(text_lives_monster_1, (positions_text[0], positions_text[2]))
        win.blit(text_lives_monster_2, (positions_text[1], positions_text[2]))
        font_loose, text_loose = get_win_text(monster_in_game_1.name, 0)
    elif lives[0] == 0:
        print("joueur 1 perd")
        text_lives_monster_1 = font_lives.render("vies restantes : " + str(lives[0]), 1, (255, 0, 0))
        win.blit(text_lives_monster_1, (positions_text[0], positions_text[2]))
        font_loose, text_loose = get_win_text(monster_in_game_2.name, 2)
    elif lives[1] == 0:
        print("joueur 2 perd")
        text_lives_monster_2 = font_lives.render("vies restantes : " + str(lives[1]), 1, (255, 0, 0))
        win.blit(text_lives_monster_2, (positions_text[1], positions_text[2]))
        font_loose, text_loose = get_win_text(monster_in_game_1.name, 1)

    win.blit(text_loose, (650 - (text_loose.get_width() / 2), 300))
    pygame.display.update()
    pygame.mixer.music.stop()
    pygame.mixer.music.set_volume(0.8)
    winSound.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def pause_before_restart(monster_1, monster_2, monster_in_game_1, monster_in_game_2, ground, lives, font_percentage, dead_monster, win, looseSound):
    text_pause = font_percentage.render("le joueur " + str(dead_monster) + " est mort, pause temporaire", 1,
                                        (255, 0, 0))
    win.blit(text_pause, (250 - (text_pause.get_width() / 2), 200))
    pygame.display.update()
    pygame.mixer.music.stop()
    pygame.mixer.music.set_volume(0.8)
    looseSound.play()
    pygame.time.delay(2500)

    ia_monster_1 = monster_in_game_1.IA
    ia_monster_2 = monster_in_game_2.IA

    del monster_in_game_1
    del monster_in_game_2

    monster_in_game_1 = init_monster_in_game(monster_1, 1, ground, lives[0], ia_monster_1)
    monster_in_game_2 = init_monster_in_game(monster_2, 2, ground, lives[1], ia_monster_2)
    bullets_monster_1 = []
    bullets_monster_2 = []
    shootLoop_monster_1 = 0
    shootLoop_monster_2 = 0

    return monster_in_game_1, monster_in_game_2, bullets_monster_1, bullets_monster_2, shootLoop_monster_1, shootLoop_monster_2, text_pause
