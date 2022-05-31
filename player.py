# The player will represent the avatar for our player moving through the maze

class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # TODO  
    def moveUp(self):
        self.rowPosition -= 1
# if 'u' then -1 from rows
        
        

    # TODO
    def moveDown(self):
# if 'd' then +1 to rows
        self.rowPosition += 1

    # TODO
    def moveLeft(self):
# if L then -1 from columns
        self.columnPosition -= 1


    # TODO
    def moveRight(self):
# if r the +1 to columns
        self.columnPosition += 1





# tYLER
# kEEP iN mIND tHE cOLUMNS/rOWS aRE 0 iNDEXED
#         [       0      1      2      3      4      5     <- cOLUMNS ->
#   0          [" * ", " * ", " x ", " * ", " * ", " * "],
#   1          [" * ", " x ", " x ", "   ", " * ", " * ",],
#   2          [" * ", " x ", " * ", " * ", "   ", " * ",],
#   3     A    [" * ", " x ", " P ", "   ", "   ", " * ",],
#   4    /|\   [" * ", " * ", " * ", " * ", " * ", " * "],
#   rOWS/ | \  ]
        # |            sTART aT X 3,2 (rOWS, cOLUMNS) eND aT 0,2
        # wINNING sEQUENCE L,U,U,R,U
        # -1 Column, -1 row, -1 row, +1 column, -1 row




# player_move = input('Select your move: ')
# if player_move in ('w','s','a','d'):
#     move = input("Enter your move: ")
    
    # how do i do actually "move"? aNSWER bELOW
# if L then -1 from columns
# if r the +1 to columns
# if u then -1 from rows
# if d then +1 to rows
     
    # if player_move == 'w':
    #     # move up
    # elif player_move == 's':
    #     # move down
    # elif player_move == 'd':
    #     # move right
    # elif player_move == 'a':
    #     # move left
    # else:
    #     print('error')

