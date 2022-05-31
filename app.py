# The app.py will contain most of the driving logic of the game (things like taking user input, calling functions in other classes, printing out to the screen, etc.)

import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

player_move = input('Select your move: ')
if player_move in ('w','s','a','d'):
    move = (input("Enter your move: "))
# TODO
# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2
# tYLER, wHAT aRE tHE gAMEbOARD aND pLAYER sUPPOSED tO bE? oBJECT? cLASS? 
# |=> rEFERENCE tHE PLAYER.PY dEF fUNCTIONS 

board = [
    gameboard()
]
board = board[0]

played = [
    player(3, 2)
]
played = played[0]


while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
    # so a while loop?
