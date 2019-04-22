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
    if role == "assassin":
        p1 = Player(name, Assassin, aHP, aAD, aDef)
        print('''You are an assassin.
                 Your stats are:''')
        print("HP: " , p1.HP , "\n")
        print("AD: " , p1.AD , "\n")
        print("DEF: " , p1.Def , "\n")
    else:
        p1 = Player(name, Knight, kHP, kAD, kDef)
        print('''You are a knight.
                 Your stats are:''')
        print("HP: " , p1.HP , "\n")
        print("AD: " , p1.AD , "\n")
        print("DEF: " , p1.Def , "\n")


    print("Now that we've got you set up, let's start our adventure.\n")
    #asks player if they wish to continue to level two
    start = input("Shall we?(y or n)\n")
    if 'y' in start:
        levelTwo()
    else:
        #player chose not to continue so offer player choice to change
        #information or quit the game
        choice = input('''What would you like to do?
                1. Change name
                2. Change role
                3. Quit\n''')
        if choice == '1':
            p1.name = input('Enter your new name\n')

        elif choice == '2':
            p1.role = input('Enter your new role\n')
            if p1.role == "knight":
                p1.HP = kHP
                p1.AD = kAD
                p1.Def = kDef
            else:
                p1.HP = aHP
                p1.AD = aAD
                p1.Def = aDef

        else:
            print('Ok! See you later!')

    



    




levelOne()
