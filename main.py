import random
print("Welcome in the world of Snack, water , gun game! ")
print('''--------------------------------------------------------------------------------------------------------------

''')
print("you chhoce for Snack is 's' , for water is 'w' and for gun is 'g'! ")

def game(comp, player):
    if comp == player:
        return None

    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True

    elif comp == 'w':
        if player == 's':
            return True
        elif player == 'g':
            return True

    elif comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True

# print("computer turn: ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
print("Enter Your choice  : Snack(s), water(w) or gun(g)?")
player = input()
decision=game(comp, player)
print(f"computer chhoce {comp}")
print(f"you chhoce {player}")
if decision==None:
    print("the game is Tie!")
elif decision:
    print("you win!")
else:
    print("Better luck next time!")

print('''---------------------------------------------------------------------------------------------------------------''')
