# connectFourBoard_class.py

# Emmett Wald
# created 11 Apr. 2018

"""connectFourBoard_class.py
Provides a class for a Connect Four board and the
interactions needed to play a game on it."""

# attributes:
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

        # creates an empty array with the given dimensions
        self.array = []
        for j in range(height):
            row = []
            for i in range(width):
                row.append(" ")
            self.array.append(row)

    # print board
    def __str__(self):
        """Provides a default format for displaying/printing."""

        # creates a row that displays nicely
        def printRow(row):
            row2print = " | "
            cells = self.array[row]
            for x in range(self.width):
                if cells[x] == 0:
                    cells[x] = " "
                row2print += cells[x] + " | "
            return row2print

        edgebar =  " +===+===+===+===+===+===+===+"
        crossbar = " +---+---+---+---+---+---+---+"
        feet = " |" + " "*27 + "|" + "\n" + "==" + " "*27 + "=="

        # assembles row2print rows, crossbars, and feet into nicely
        # formatted triple-quoted string for displaying the board
        board2print = """   1   2   3   4   5   6   7"""
        board2print += "\n" + edgebar
        for y in range(self.height-1):
            board2print += "\n" + printRow(y) + "\n" + crossbar
        board2print += "\n" + printRow(self.height-1) + "\n" + edgebar
        board2print += "\n" + feet + "\n"
            
        # board2print for empty board will look like:
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

    # check whether column is full
    def columnFull(self, column):
        """Returns True if every cell in a column has been filled."""

        if self.array[0][column] == "B" or self.array[0][column] == "R": ### should be able to just be "if self.array[0][col]" bc default is 0 ~ ?
            return True
        else:
            return False

    # drop checker
    def dropChecker(self, column, turn, names):
        """Modifies the board array by adding a checker of the player's
        color in the bottom-most free spot in the given column."""

        column -= 1 # converts label column to column index

        # determines the lowest free cell
        if self.array[5][column] == " ":
            row = 5
        elif self.array[4][column] == " ":
            row = 4
        elif self.array[3][column] == " ":
            row = 3
        elif self.array[2][column] == " ":
            row = 2
        elif self.array[1][column] == " ":
            row = 1
        else:
            row = 0

        # assigns the cell "B" for black or "R" for red
        # based on whose turn it is
        self.array[row][column] = names[turn][1][0].upper()
        
        return row, column

    # checks for a winning combo and returns either winner's index or
    # False if there is no winning combo
    def checkWinner(self, row, column, names):
        """Seeks four-in-a-rows horizontally, vertically, and diagonally
        from the cell; returns winner's index if there is a winning
        combination, or False otherwise.""" ### figure out why insta-winner

        color = self.array[row][column]

        # derives winner index from color initial
        if color == "B":
            winner = "black"
        else: # color == "R"
            winner = "red"
        for i in [0,1]:
            if winner in names[i]:
                winner = i
        
        # increments for seeking four in a row vertically, horizontally,
        # diagonally down, and diagonally up
        increments = ((1, 0), (0, 1), (1, 1), (1, -1))
        for inc in increments:
            incI = inc[0]
            incJ = inc[1]

            # initializes counter and sentinel variables
            count = 0
            current = color
            i = row
            j = column

            # steps in initial direction from starting cell
            while color == current:
                count += 1
                if count >= 4:
                    return winner
                i += incI
                j += incJ
                if 0 <= i <= 5 and 0 <= j <= 6:
                    current = self.array[i][j]
                else:
                    break

            # resets counter and sentinel variables
            count -= 1 # compensate for adding one at start of loop, so center cell isn't double counter
            current = color
            i = row
            j = column

            # steps in opposite direction from starting cell
            while color == current:
                count += 1
                if count >= 4:
                    return winner
                i -= incI
                j -= incJ
                if 0 <= i <= 5 and 0 <= j <= 6:
                    current = self.array[i][j]
                else:
                    break

        # if none of the while loops find four in a row, returns False to
        # indicate that there is no winning combo yet
        return False
