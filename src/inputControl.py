from random import *
import sys
import pygame

from ghost import Ghost #pycharm est une pute
from golem import Golem
from player import Player
from enemy import Enemy
from projectile import Projectile

pygame.init()

#print ("The arguments are: " , str(arguments))
def control_input(arguments):
    list_monsters = ["ghost", "golem", "player", "enemy"]
    list_ia = ["agressive", "fuyarde", "random", "op"]
    list_grounds = ["1", "2", "3"]
    print(len(arguments))
    if len(arguments) < 6:
        if len(arguments) == 1:
            monster_1 = list_monsters[randint(0,3)]
            monster_1_ia = list_ia[randint(0,3)]
            monster_2 = list_monsters[randint(0,3)]
            monster_2_ia = list_ia[randint(0,3)]
            ground = list_grounds[randint(0,2)]
            print("selection des arguments par défaut : monster_1 = ", monster_1, " monster_1_ia = ", monster_1_ia,
                  " monster_2 = ", monster_2, " monster_2_ia = ", monster_2_ia, " ground = ", ground)
            return monster_1, monster_1_ia, monster_2, monster_2_ia, ground
        print("Pas assez d'arguments entrés ! Il faut en entrer 5")
        sys.exit()
    else:
        print("args : monster_1 : ", arguments[1], " monster_1_ia = ", arguments[2],
              "monster_2 : ", arguments[3], " monster_2_ia = ", arguments[4], " ground = ", arguments[5])
        #tests to verify the parameters
        if arguments[1] == list_monsters[0] or arguments[1] == list_monsters[1] or arguments[1] == list_monsters[2] or arguments[1] == list_monsters[3] or arguments[1] == "random":
            if arguments[1] == "random":
                monster_1 = list_monsters[randint(0,3)]
            else:
                monster_1 = arguments[1]
        else:
            print("Ce personnage n'existe pas, choisissez entre golem, ghost, player ou enemy")
            sys.exit()
    
        if arguments[2] == "agressive" or arguments[2] == "fuyarde" or arguments[2] == "random" or arguments[2] == "op":
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
            print("Ce personnage n'existe pas, choisissez entre golem, ghost, player ou enemy")
            sys.exit()
    
        if arguments[4] == "agressive" or arguments[4] == "fuyarde" or arguments[4] == "random" or arguments[4] == "op":
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
    list_monsters = ["ghost", "golem", "player", "enemy"]
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

def init_monster_in_game(monster_name, monster_number, ground):
    list_monsters = ["ghost", "golem", "player", "enemy"]
    if ground == "1":
        start_x_monster_1 = 60
        start_x_monster_2 = 1150
        end = 1150
    elif ground == "2":
        start_x_monster_1 = 60
        start_x_monster_2 = 1040
        end = 1040
    else:
        start_x_monster_1 = 60
        start_x_monster_2 = 950
        end = 950

    if monster_number == 1:
        if monster_name == list_monsters[0]:
            monster = Ghost(start_x_monster_1, 410, 64, 64, end, 5)
            #monster = Ghost(x, y, width, height, end, lives, begin)
        elif monster_name == list_monsters[1]:
            monster = Golem(start_x_monster_1, 380, 64, 64, end, 5)
            #monster = Golem(x, y, width, height, end, lives, begin)
        elif monster_name == list_monsters[2]:
            monster = Player(start_x_monster_1, 410, 64, 64, end, 5)
            #monster = Player(x, y, width, height, end, lives, begin)
        else:
            monster = Enemy(start_x_monster_1, 410, 64, 64, end, 5)
            #monster = Enemy(x, y, width, height, end, lives, begin)
    else:
        if monster_name == list_monsters[0]:
            monster = Ghost(start_x_monster_2, 410, 64, 64, end, 5)
            #monster = Ghost(x, y, width, height, end, lives, begin)
        elif monster_name == list_monsters[1]:
            monster = Golem(start_x_monster_2, 380, 64, 64, end, 5)
            #monster = Golem(x, y, width, height, end, lives, begin)
        elif monster_name == list_monsters[2]:
            monster = Player(start_x_monster_2, 410, 64, 64, end, 5)
            #monster = Player(x, y, width, height, end, lives, begin)
        else:
            monster = Enemy(start_x_monster_2, 410, 64, 64, end, 5)
            #monster = Enemy(x, y, width, height, end, lives, begin)

    return monster

