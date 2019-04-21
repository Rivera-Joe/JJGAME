# function for level 1
# started on 04/17/2019
# Joe

<<<<<<< HEAD
# Import player class
import Player_Class
=======
#Import player class
from Player_Class import Player
>>>>>>> 405fe458e673b99b519c315d690328974be9c2c1


class Player:

    def __init__(self, name, role, HP, AD, Def):
        self.name = name
        self.role = role
        self.HP = HP
        self.AD = AD
        self.Def = Def


def levelOne():
<<<<<<< HEAD
    role = ' '
    # stats for Knight
    Knight = "Knight"
=======
#stats for Knight
   
>>>>>>> 405fe458e673b99b519c315d690328974be9c2c1
    kHP = 100
    kAD = 20
    kDef = 30

<<<<<<< HEAD
    # stats for Assassin
    Assassin = "Assasssin"
=======
#stats for Assassin
    
>>>>>>> 405fe458e673b99b519c315d690328974be9c2c1
    aHP = 50
    aAD = 50
    aDef = 10

    # gets name for player
    name = input("So you're back again, eh? What was your name again?\n")
<<<<<<< HEAD

    # make sure player chooses correct role
    while (True):
        role = input("Choose your role (Assassin or Knight )\n")
        role = role.lower()
        if (role == 'assassin') or (role == "knight"):
            break

    # sets players stats based on the role selected
    if (role == "assassin"):
        p1 = Player(name, Assassin, aHP, aAD, aDef)
        print('you are an assassin')
    else:
        p1 = Player(name, Knight, kHP, kAD, kDef)
        print('you are a knight')
=======
    
    role = input("Choose your role (Assassin or Knight )\n")
    role.lower()

#make sure player chooses correct role
    if(role != "assassin" or role != "knight"):
        role = input("Choose your role (Assassin or Knight )\n")
        role.lower()

#sets players stats based on the role selected
    if(role == "assassin"):
       p1 = Player(name, role, aHP, aAD, aDef)
       #check assignment
       print(p1.HP)
    else:
       p1 = Player(name, role, kHP, kAD, kDef)
       print(p1.HP)

>>>>>>> 405fe458e673b99b519c315d690328974be9c2c1



levelOne()
