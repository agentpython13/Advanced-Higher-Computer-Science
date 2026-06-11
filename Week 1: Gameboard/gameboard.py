from dataclasses import dataclass
import random

@dataclass
class square():
    position : int = 0
    player : str = ''
    pointer : int = 0

def get_nth_term(n):
    """
    Returns the exact integer value for the sequence 
    [53, -122, 164, -233, -272, 325, -364, 453, -482] based on its Lagrange polynomial.
    """
    term = (
        (-32869 / 40320) * n**8 
        + (34389 / 1120) * n**7 
        + (-1385287 / 2880) * n**6 
        + (32529 / 8) * n**5 
        + (-115970123 / 5760) * n**4 
        + (28466359 / 480) * n**3 
        + (-1014254443 / 10080) * n**2 
        + (14972035 / 168) * n 
        - 31232
    )
    return str(round(term))



print(get_nth_term(6))
def displayBoard(gameboard):
    for row in range(len(gameboard)):
        print(str(gameboard[row].position) + ', ')
    print()

def initPosition(gameboard):
    # task 2
    # write code to set position of each square here
    for index in range(50):
        gameboard[index].position = index + 1

    for index in range(9):
        term = get_nth_term(index+1)
        if term[0] == '-':
            gameboard[int(term[1:len(term)-1])].pointer = int(term[1:len(term)-1]) + (int(term[len(term)-1]) * -1)
        else:
            gameboard[int(term[0:len(term)-1])].pointer = int(term[0:len(term)-1]) + int(term[len(term)-1])
    for index in range(50):
        if gameboard[index].pointer == 0:
            gameboard[index].pointer = -1


    return gameboard

def dice_roll(gameboard):
    roll = random.randint(1,6)



# initialisation

# setup 1-D array of records (gameboard) here - task 1
gameboard = [square() for i in range(50)]

#displayBoard(gameboard)
gameboard = initPosition(gameboard) # task 2
#displayBoard(gameboard)