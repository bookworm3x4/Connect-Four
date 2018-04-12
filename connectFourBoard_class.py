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

    # drop checker
    def dropChecker(self, column, turn):
        """Modifies the board array by adding a checker of the player's
        color in the bottom-most free spot in the given column."""

        column -= 1 # converts label column to column index

        # determines the lowest free cell
        if board[5][column] == 0:
            row = 5
        elif board[4][column] == 0:
            row = 4
        elif board[3][column] == 0:
            row = 3
        elif board[2][column] == 0:
            row = 2
        elif board[1][column] == 0:
            row = 1
        else:
            row = 0

        # assigns the cell "B" for black or "R" for red
        # based on whose turn it is
        board[row][column] = names[turn][1][0].upper()
        
        return row, column

    # checks for a winning combo and returns either winner's index or
    # False if there is no winning combo
    def checkWinner(self, row, column):
        """Seeks four-in-a-rows horizontally, vertically, and diagonally
        from the cell; returns winner's index if there is a winning
        combination, or False otherwise."""

        color = board[row][column]

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
                    current = board[i][j]
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
                    current = board[i][j]
                else:
                    break

        # if none of the while loops find four in a row, returns False to
        # indicate that there is no winning combo yet
        return False
