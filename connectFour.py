# connectFour.py

# Simulation for a two-player game of Connect Four.

# created 16 Mar. 2018

'''
TASK LIST:
~ fix playAgain for new names format
~ fix announceWinner
~ make names into a global variable?
~ import winningCombos from txt file?
~ create graphic interface
'''


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

                        # MAIN FUNCTION(S) #

def main():
    names = SETUP()
    PLAY(names)


def SETUP():
    intro()
    names = firstPlayer(players())
    return names

def PLAY(names):
    runGame(names)
    playAgain(names)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

                            # OUTLINE #
'''
main()
    SETUP()
	intro()
	players()
	firstPlayer(names)
    PLAY(names)
	runGame(names)
	    getMove(names, turn)
	    placeMove(names, turn, move)
	    checkWinner(board, move)
		possibleWins(move)
            announceWinner(winner, names)
	    nextTurn(turn)
	playAgain(names)
            PLAY(names)
'''


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

                        # MAJOR FUNCTIONS #

def intro():
    print("Welcome to Connect Four!\n")
    print("Here's what the board looks like:")
    printBoard(board)
    print("Hit Enter to start game.")
    input()
    print("Let's get started!\n")
    
def players():    
    print("Who's playing?")
    names[0][0] = input("One player: ").capitalize()
    names[1][0] = input("The other player: ").capitalize()
    print()
    return names

def firstPlayer(names):
    i = coinFlip()
    names[i][1] = "black"
    names[abs(i-1)][1] = "red"
    print(names[0][0], "is", names[0][1],"and",
          names[1][0], "is", names[1][1] + ";")
    j = coinFlip()
    names[0][2] = j
    names[1][2] = abs(j-1)
    print(names[j][0], "goes first.\n")
    print()
    return names

def runGame(names):
    turn = names[0][2]
    for i in range(42):
        move = getMove(names, turn)
        move = placeMove(names, turn, move)
        winner = checkWinner(board, move)
        if winner != "":
            announceWinner(winner, names)
            break
        elif i == 41:
            print("Oops, looks like it's a draw!\n")
        else:
            turn = nextTurn(turn)

def getMove(names, turn):
    move = input("It's " + names[turn][0] + "'s turn. Where do you want to drop your checker?\n> ").upper()
    print()
    while move not in columns or board[move + "6"] != " ":
        if move not in columns:
            move = input("That's not a valid option. Try again. Drop your checker where?\n> ").upper()
        else:
            move = input("That column is full. Try again. Drop your checker where?\n> ").upper()
        print()
    return move

def placeMove(names, turn, move):
    if board[move + "1"] == " ":
        move = move + "1"
    elif board[move + "2"] == " ":
        move = move + "2"
    elif board[move + "3"] == " ":
        move = move + "3"
    elif board[move + "4"] == " ":
        move = move + "4"
    elif board[move + "5"] == " ":
        move = move + "5"
    else:
        move = move + "6"
    board[move] = names[turn][1][0].upper()
    printBoard(board)
    return move

def checkWinner(B, move):
    winner = ""
    toCheck = possibleWins(move)
    for i in toCheck:
        if board[i[0]] == board[i[1]] == board[i[2]] == board[i[3]]:
            winner = board[i[0]] # sets it to B or R
            break
    if winner == "B":
        winner = "black"
    elif winner == "R":
        winner = "red"
    return winner

def possibleWins(move):
    toCheck = []
    for i in winningCombos:
        if move in i:
            toCheck.append(i)
    return toCheck

def announceWinner(winner, names):
    for i in [0,1]:
        if winner in names[i]:
            winner = i
    message = "Four in a row!", names[winner][0], "wins!"
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

def playAgain(names):
    print("Game over. Play again?")
    again = input("> ").upper()[0]
    if again == "Y":
        print("\nOkay, new game. This time", names[0], "goes first.\n")
        PLAY(names)
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

import random
def coinFlip():
    return random.randint(0, 1)

board = {"A6":" ", "B6":" ", "C6":" ", "D6":" ", "E6":" ", "F6":" ", "G6":" ",
         "A5":" ", "B5":" ", "C5":" ", "D5":" ", "E5":" ", "F5":" ", "G5":" ",
         "A4":" ", "B4":" ", "C4":" ", "D4":" ", "E4":" ", "F4":" ", "G4":" ",
         "A3":" ", "B3":" ", "C3":" ", "D3":" ", "E3":" ", "F3":" ", "G3":" ",
         "A2":" ", "B2":" ", "C2":" ", "D2":" ", "E2":" ", "F2":" ", "G2":" ",
         "A1":" ", "B1":" ", "C1":" ", "D1":" ", "E1":" ", "F1":" ", "G1":" "}

columns = ["A", "B", "C", "D", "E", "F", "G"]

edgebar =  " +===+===+===+===+===+===+===+"
crossbar = " +---+---+---+---+---+---+---+"

def printRow(board, row):
    return " | "  + board["A" + row] + " | " + board["B" + row] + \
           " | " + board["C" + row] + " | " + board["D" + row] + \
           " | " + board["E" + row] + " | " + board["F" + row] + \
           " | " + board["G" + row] + " |"

def printBoard(board):
    print("   A   B   C   D   E   F   G")
    print(edgebar)
    print(printRow(board, "6"))
    print(crossbar)
    print(printRow(board, "5"))
    print(crossbar)
    print(printRow(board, "4"))
    print(crossbar)
    print(printRow(board, "3"))
    print(crossbar)
    print(printRow(board, "2"))
    print(crossbar)
    print(printRow(board, "1"))
    print(edgebar)
    print(" |" + " " * 27 + "|")
    print("==" + " " * 27 + "==")
    print()
    
'''
empty board will look like:
   A   B   C   D   E   F   G
 +===+===+===+===+===+===+===+
 |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   |   |
 +===+===+===+===+===+===+===+
 |                           |
==                           ==
'''

winningCombos = (# vertical
                 ['A1', 'A2', 'A3', 'A4'], ['A2', 'A3', 'A4', 'A5'], ['A3', 'A4', 'A5', 'A6'],
                 ['B1', 'B2', 'B3', 'B4'], ['B2', 'B3', 'B4', 'B5'], ['B3', 'B4', 'B5', 'B6'],
                 ['C1', 'C2', 'C3', 'C4'], ['C2', 'C3', 'C4', 'C5'], ['C3', 'C4', 'C5', 'C6'],
                 ['D1', 'D2', 'D3', 'D4'], ['D2', 'D3', 'D4', 'D5'], ['D3', 'D4', 'D5', 'D6'],
                 ['E1', 'E2', 'E3', 'E4'], ['E2', 'E3', 'E4', 'E5'], ['E3', 'E4', 'E5', 'E6'],
                 ['F1', 'F2', 'F3', 'F4'], ['F2', 'F3', 'F4', 'F5'], ['F3', 'F4', 'F5', 'F6'],
                 ['G1', 'G2', 'G3', 'G4'], ['G2', 'G3', 'G4', 'G5'], ['G3', 'G4', 'G5', 'G6'],

                 # horizontal
                 ['A1', 'B1', 'C1', 'D1'], ['B1', 'C1', 'D1', 'E1'], ['C1', 'D1', 'E1', 'F1'], ['D1', 'E1', 'F1', 'G1'],
                 ['A2', 'B2', 'C2', 'D2'], ['B2', 'C2', 'D2', 'E2'], ['C2', 'D2', 'E2', 'F2'], ['D2', 'E2', 'F2', 'G2'],
                 ['A3', 'B3', 'C3', 'D3'], ['B3', 'C3', 'D3', 'E3'], ['C3', 'D3', 'E3', 'F3'], ['D3', 'E3', 'F3', 'G3'],
                 ['A4', 'B4', 'C4', 'D4'], ['B4', 'C4', 'D4', 'E4'], ['C4', 'D4', 'E4', 'F4'], ['D4', 'E4', 'F4', 'G4'],
                 ['A5', 'B5', 'C5', 'D5'], ['B5', 'C5', 'D5', 'E5'], ['C5', 'D5', 'E5', 'F5'], ['D5', 'E5', 'F5', 'G5'],
                 ['A6', 'B6', 'C6', 'D6'], ['B6', 'C6', 'D6', 'E6'], ['C6', 'D6', 'E6', 'F6'], ['D6', 'E6', 'F6', 'G6'],

                 # diagonal up
                 ['A1', 'B2', 'C3', 'D4'], ['A2', 'B3', 'C4', 'D5'], ['A3', 'B4', 'C5', 'D6'],
                 ['B1', 'C2', 'D3', 'E4'], ['B2', 'C3', 'D4', 'E5'], ['B3', 'C4', 'D5', 'E6'],
                 ['C1', 'D2', 'E3', 'F4'], ['C2', 'D3', 'E4', 'F5'], ['C3', 'D4', 'E5', 'F6'],
                 ['D1', 'E2', 'F3', 'G4'], ['D2', 'E3', 'F4', 'G5'], ['D3', 'E4', 'F5', 'G6'],

                 # diagonal down
                 ['A6', 'B5', 'C4', 'D3'], ['A5', 'B4', 'C3', 'D2'], ['A4', 'B3', 'C2', 'D1'],
                 ['B6', 'C5', 'D4', 'E3'], ['B5', 'C4', 'D3', 'E2'], ['B4', 'C3', 'D2', 'E1'],
                 ['C6', 'D5', 'E4', 'F3'], ['C5', 'D4', 'E3', 'F2'], ['C4', 'D3', 'E2', 'F1'],
                 ['D6', 'E5', 'F4', 'G3'], ['D5', 'E4', 'F3', 'G2'], ['D4', 'E3', 'F2', 'G1'])

names = [["","",0], ["","",0]] # [name, color, order]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

main()
