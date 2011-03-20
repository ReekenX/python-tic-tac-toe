from sys import exit
from random import randint
from board import Board, HUMAN, COMPUTER

def humanize_coord(coord):
    if coord == HUMAN:
        return 'O'
    elif coord == COMPUTER:
        return 'X'
    else:
        return ' '

def print_board(board):
    for x in range(board.max_width):
        print "-------------------------------"
        print "|         |         |         |"
        print "|    %s    |    %s    |    %s    |" % \
            (humanize_coord(board.board[x][0]), humanize_coord(board.board[x][1]), humanize_coord(board.board[x][2]))
        print "|         |         |         |"
    print "-------------------------------"

number = None
while not number in ["1", "2", "0"]:
    print "==========================================================="
    print "   Tic Tac Toe - yep, another game version of this game.   "
    print "==========================================================="
    print
    print "Choose who should start the game first?"
    print
    print "              1) You"
    print "              2) Super Computer"
    print
    print "              0) Exit game, but return later"
    print
    if number == None:
        number = raw_input("Enter number. But choose wisely - all hopes in you: ")
    else:
        number = raw_input("Oops, I have said, that only numbers are allowed: ")
    print

board = Board()

if number == "1":
    print "Ok, you will start the game first! Prepare for action!"
    print
    board.player_starts(HUMAN)
    print_board(board)
elif number == "2":
    print "Super Computer starts the game. He's thinking about first his move, so"
    print "you should be patient..."
    print
    board.player_starts(COMPUTER)
    board.put(randint(0, 2), randint(0, 2), COMPUTER)
    print_board(board)
else:
    exit(0)

while board.get_winner() == None:
    print
    if board.player_turn() == HUMAN:
        x = int(raw_input("Now is your turn. Enter X coord starting from 0 to 2: "))
        y = int(raw_input("                  Enter Y coord starting from 0 to 2: "))
        while x not in [0, 1, 2] or y not in [0, 1, 2] or not board.can_put(x, y):
            first = False
            print
            if x not in [0, 1, 2] or y not in [0, 1, 2]:
                print "Oops, invalid coords. Please try again."
            else:
                print "As you can see, this is reserved place. Choose another one!"
            print
            x = int(raw_input("Enter X coord starting from 0 to 2: "))
            y = int(raw_input("Enter Y coord starting from 0 to 2: "))
    else:
        print "Computer thinking... Oh, here it is:"
        print
        move = board.get_best_move()
        x = move[0]
        y = move[1]

    board.put(x, y, board.player_turn())
    print_board(board)

print
if board.get_winner() == COMPUTER:
    print "Yep, you can't win against Super Computer. But you can try..."
elif board.get_winner() == HUMAN:
    print "Impossible! You won against the Super Computer! Congrats!"

print
raw_input("Game ended, hope you will return back for more. Press ENTER to close...")
