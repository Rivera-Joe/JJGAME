#function for level 1
#started on 04/17/2019
#Joe

#Import player class
from Player_Class import Player
def levelOne():
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

#gets name for player
    name = input("So you're back again, eh? What was your name again?\n")
    
    

#make sure player chooses correct role
    while(role !=Knight or role !=Assassin):
        role = input("Choose your role (Assassin or Knight )\n")
        r = role.lower()

#sets players stats based on the role selected
    if(r == "assassin"):
       p1 = Player(name, Assassin, aHP, aAD, aDef)
    else:
       p1 = Player(name, Knight, kHP, kAD, kDef)
role = 'temp'
print(p1.role) 

levelOne()

