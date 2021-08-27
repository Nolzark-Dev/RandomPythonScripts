import random

player1dice = random.randint(1,20)
player2dice = random.randint(1,20)
print("####################")
print("player 1 roll: ") 
print(player1dice)
print("####################")
print("")
print("####################")
print("player 2 roll: ")
print(player2dice)
print("####################")
if player1dice > player2dice:
    print("")
    print("####################")
    print("PLAYER 1 WINS")
    print("####################")
if player2dice > player1dice:
    print("")
    print("####################")
    print("PLAYER 2 WINS")
    print("####################")
if player1dice == player2dice:
    print("")
    print("####################")
    print("TIE")
    print("####################")

