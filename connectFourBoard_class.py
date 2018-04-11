# connectFourBoard_class.py

# Emmett Wald
# created 11 Apr. 2018

"""connectFourBoard_class.py
Provides a class for a Connect Four board and the
interactions needed to play a game on it."""

# parameters:
# - width = number of cells wide
# - height = number of cells high
# - array = a [width x height] array representing every cell on the board
# methods:
# - constructor
# - default string format
# - dropChecker
# - checkWinner

class Board:
    
    # constructor
    def __init__(self, width, height):
        """Creates a Board object with a given width and height."""
        self.width = width
        self.height = height

        # creates an empty array with the correct dimensions
        row = []
        for x in range(width):
            row.append(0)
        self.array = []
        for y in range(height):
            self.array.append(row)

    # print board
    def __str__(self):
        """Provides a default format for displaying/printing."""

        # creates a row that displays nicely
        def printRow(row):
            row2print = " | "
            for x in range(width):
                if board[row][x] == 0:
                    board[row][x] = " "
                row2print.append(board[row][x] + " | ")
            return row2print

        edgebar =  " +===+===+===+===+===+===+===+"
        crossbar = " +---+---+---+---+---+---+---+"
        feet = " |" + " " * 27 + "|" + "\n" + "==" + " " * 27 + "=="

        # assembles row2print rows, crossbars, and feet into nicely
        # formatted triple-quoted string for displaying the board
        board2print = """
           1   2   3   4   5   6   7
        """
        board2print += "\n" + edgebar
        for y in range(height - 1):
            board2print += "\n" + printRow(y) + "\n" + crossbar
        board2print += "\n" + printRow(height) + edgebar
        board2print += "\n" + feet
            
        # empty board will look like:
        '''
           1   2   3   4   5   6   7
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

        return board2print

    # drop checker
    def dropChecker(self, column, player):
        """Modifies the board array by adding a checker of the player's
        color in the bottom-most free spot in the given column."""

        

    # check for a winning combo
