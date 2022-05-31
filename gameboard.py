# The gameboard will represent the boundaries of the maze

class GameBoard:
    # 19f page 9 says to add winningRow, winningColumn, board to the () below, winningRow, winningColumn, board
    def __init__(self):
        # the next 2 lines define the end point for the player
        self.winningRow = 0
        self.winningColumn = 2
        self.board = [
            [" * ", " * ", "   ", " * ", " * ", " * "],
            [" * ", "   ", "   ", "   ", " * ", " * ",],
            [" * ", "   ", " * ", " * ", "   ", " * ",],
            [" * ", "   ", "   ", "   ", "   ", " * ",],
            [" * ", " * ", " * ", " * ", " * ", " * "],
        ]

    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print("P", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    # TODO
    def checkWin(self, playerRow, playerColumn):
        if (playerRow[0] and playerColumn[2]):
            return True
        else:
            return False
    # Return True if the player is in the winning column and row
    # Return False otherwise
    # def checkWin(self, playerRow, playerColumn):

# board = GameBoard[2]
# print(board)


# elif self.board[testRow][testColumn].find(" ") = -1:
    # print("Moved there!")



        #     [" * ", " * ", "   ", " * ", " * ", " * "],
        #     [
        #         " * ",
        #         "   ",
        #         "   ",
        #         "   ",
        #         " * ",
        #         " * ",
        #     ],
        #     [
        #         " * ",
        #         "   ",
        #         " * ",
        #         " * ",
        #         "   ",
        #         " * ",
        #     ],
        #     [
        #         " * ",
        #         "   ",
        #         "   ",
        #         "   ",
        #         "   ",
        #         " * ",
        #     ],
        #     [" * ", " * ", " * ", " * ", " * ", " * "],
        # ]
        # [