#my version of the Codecademy Battleship exercise where you can have as many turns as you want

from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

def play(gameplay):
    for turn in range(gameplay):
        print "Turn " + str(turn + 1)
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        guesses(guess_row, guess_col, turn, gameplay)

def guesses(row, column, turn, gameplay):
    if row == ship_row and column == ship_col:
        print "Congratulations! You sank my battleship"
        exit()
    elif row not in range(5) or column not in range(5):
            print "Oops, that's not even in the ocean."
    elif board[row][column] == "X":
            print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[row][column] = "X"
        print_board(board)
        if turn == gameplay - 1:
            print "Game Over"
        else:
            pass

wanted_turns = int(raw_input("How many turns do you want?: "))
print_board(board)
play(wanted_turns)
# Ideas to keep working on: 2 player game; multiple ships; multiple size ships
