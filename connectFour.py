# connectFour.py

# Emmett Wald
# created 16 Mar. 2018

# Simulation for a two-player game of Connect Four.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

                        # MAIN FUNCTION(S) #

def main():
    SETUP()
    PLAY()


def SETUP():
    intro()
    players()
    firstPlayer()

def PLAY():
    runGame()
    playAgain()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

                            # OUTLINE #
'''
main()
    SETUP()
	intro()
	players()
	firstPlayer()
    PLAY()
	runGame()
	    getMove(turn)
	    placeMove(turn, move)
	    checkWinner(board, move)
		possibleWins(move)
            announceWinner(winner)
	    nextTurn(turn)
	playAgain()
            PLAY()
'''


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

                        # MAJOR FUNCTIONS #

def intro():
    print(welcomeMsg, end = "\n\n")
    print("Here's what the board looks like:\n")
    print(board)
    print("On your turn, type the letter corresponding to",
          "the column you want to drop your checker in.\n",
          sep = "\n")
    print("Hit Enter to start game.")
    input()
    print("Let's get started!\n")
    
def players():    
    print("Who's playing?")
    global names
    names[0][0] = input("One player: ").capitalize()
    names[1][0] = input("The other player: ").capitalize()
    print()

def firstPlayer():
    i = coinFlip()
    global names
    names[i][1] = "black"
    names[abs(i-1)][1] = "red"
    print(names[0][0], "is", names[0][1],"and",
          names[1][0], "is", names[1][1] + ";")
    j = coinFlip()
    names[0][2] = j
    names[1][2] = abs(j-1)
    print(names[j][0], "goes first.\n")
    print()

def runGame():
    turn = names[0][2]
    for i in range(42):
        move = getMove(turn)
        row, column = board.dropChecker(move, turn, names)
        winner = board.checkWinner(row, column, names)
        if winner:
            announceWinner(winner)
            break
        elif i == 41:
            print("Oops, looks like it's a draw!\n")
        else:
            turn = nextTurn(turn)

def getMove(turn):
    move = int(input("It's " + names[turn][0] + "'s turn. Where do you want to drop your checker?\n> "))
    print()
    while move not in range(1, 8) or board.columnFull(move):
        if move not in range(1, 8):
            move = int(input("That's not a valid option. Try again. Drop your checker where?\n> "))
        else:
            move = int(input("That column is full. Try again. Drop your checker where?\n> "))
        print()
    return move

def announceWinner(winner):
    message = "Four in a row! " + names[winner][0] + " wins!"
    bar = "*" * len(message)
    print(bar)
    print(message)
    print(bar)
    print()

def nextTurn(T): # T = turn
    if T == 0:
        T = 1
    else:
        T = 0
    return T

def playAgain():
    print("Game over. Play again?")
    again = input("> ").upper()[0]
    if again == "Y":
        global names
        names[0][2], names[1][2] = names[1][2], names[0][2]
        if names[0][2] == 0:
            first = names[0][0]
        else:
            first = names[1][0]
        print("\nOkay, new game. This time", first, "goes first.\n")
        PLAY()
    else:
        print("Goodbye!\n")
        

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

                            # GRAPHICS #
# set up graphic window
# draw static elements
# draw input boxes
# draw dynamic elements


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

                # DEFINITIONS & MINOR FUNCTIONS #

welcomeMsg = """
               W E L C O M E   T O
  ____                                          _
 / ___|  ___    ____    ____     ___    ___   _| |_
| |     / _ \  |  _ \  |  _ \   / _ \  / __| |_   _|
| |___ | |_| | | | | | | | | | |  __/ | |__    | |_
 \____| \___/  |_| |_| |_| |_|  \___|  \___|    \__|
            _____
           |  ___|  ___    _   _    ___
           | |__   / _ \  | | | |  / __|
           |  __| | |_| | | |_| | | |
           |_|     \___/   \____| |_|

                 _for two players_
"""

names = [["","",0], ["","",0]] # [name, color, order]

import random
def coinFlip():
    return random.randint(0, 1)

from connectFourBoard_class import Board
board = Board(7, 6)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

main()
