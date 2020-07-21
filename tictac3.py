# Tic Tac Tow Game 3x3

offical_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def start_game():
    #Function to run game
    print("Hi! Welcome to DB Geiger's new tic tac toe game!")
    input("Press Enter to continue...")
    return

def print_board():
    print board[0:3]
    print board[3:6]
    print board[6:9]


def user_turn():
    print("It is your turn, human!")
    print("Enter a number 1-9 available on the board.")
    print_board(board)
    val = input()
    entry_val = False
    while entry_val == False:
        if len(val) > 1 or val.isdigit() == False:
            print("That was not a valid entry. Please enter a number 1-9 available on the board.")
            val = input()
        elif board[val] == "X" or board[val] == "O":
            print("That square has already been taken. Please enter a number 1-9 STILL OPEN on the board.")
            val = input()
        else:
            entry_val = True
    board[val] = "X"
    return 

def check_state(board):
    options = [board[0:3], board[3:6], board[6:9], [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]], [board[0], board[4], board[8]], [board[2], board[4], board[6]]]
    for option in options:
        if option.count("X") == 3:
            return "X win"
        elif option.count("O") == 3:
            return "O win"
    if board.count("X") + board.count("O") == 9:
        return "Tie"
    return "Unfinished"

def check_options(board):
    board_copy = []
    chances = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for y in range(9):
        board_copy = board
        if board_copy[y].isdigit():
            board_copy[y] = "O"
            out = check_state(board_copy)
            if out == "O win":
                chances[y] += 50
            elif out == "Unfinished":
                for z in range(9):
                    if board_copy[y].isdigit():
                        board_copy[y] = "X"
                        outx = check_state(board_copy)
                        if outx


