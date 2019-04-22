# function for level 1
# started on 04/17/2019
# Joe




#Import player class
from Player_Class import Player

#Import enemy class
from enemyClass import Enemy




def levelOne():

    role = ' '
  
    

#stats for Knight
    Knight = "Knight"
    kHP = 100
    kAD = 20
    kDef = 30



    
#stats for Assassin
    Assassin = "Assasssin"
    aHP = 50
    aAD = 50
    aDef = 10

    # gets name for player
    name = input("So you're back again, eh? What was your name again?\n")


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


    



    




levelOne()
