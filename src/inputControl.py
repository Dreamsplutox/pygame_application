from random import *
import sys

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
                monster_2 = arguments[1]
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