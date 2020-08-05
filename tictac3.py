from time import sleep

# Tic Tac Tow Game 3x3
board_copy = []
offical_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_status = "Unfinished"

def start_game():
    #Function to run game
    game_status = "Unfinished"
    print("Hi! Welcome to DB Geiger's new tic tac toe game!")
    input("Press Enter to continue...")
    while game_status == "Unfinished":
        print("JUST BEFORE USER TURN", offical_board, game_status)
        user_turn()
        st = check_state(offical_board)
        if st != "Unfinished":
            game_status = st
            break
        sleep(1)
        print("JUST BEFORE COMPUTER TURN", offical_board, game_status)
        computer_turn()
        st = check_state(offical_board)
        if st != "Unfinished":
            game_status = st
        sleep(1)
    print("BROKE WHILE LOOP FOR UNFINISHED GAME STATUS", offical_board, game_status)
    if game_status == "X win":
        print("Congradulations Human, You have bested me!")
    elif game_status == "O win":
        print("Hahahah human, I have bested you!")
    elif game_status == "Tie":
        print("Ahh! I guess we are evenly matched! Next time I will get you!")
    play_again = input("Would you like to play again? (Y/N)")
    answers = ["Y", "y", "N", "n"]
    while play_again not in answers:
        print("That wasn't a valid selection. Choose Y or N.")
        play_again = input("Would you like to play again? (Y/N)")
    if play_again == "Y" or play_again == "y":
        start_game()
    return

def print_board():
    print("SHOULD BE THE OFFICAL BOARD", offical_board, game_status)
    print(offical_board[0:3])
    print(offical_board[3:6])
    print(offical_board[6:9])


def user_turn():
    print("USER TURN 1", offical_board, game_status)
    print("It is your turn, human!")
    print("Enter a number 1-9 available on the board.")
    print_board()
    val = input()
    entry_val = False
    while entry_val == False:
        if len(val) > 1 or val.isdigit() == False:
            print("That was not a valid entry. Please enter a number 1-9 available on the board.")
            val = input()
        elif offical_board[int(val) - 1] == "X" or offical_board[int(val) - 1] == "O":
            print("That square has already been taken. Please enter a number 1-9 STILL OPEN on the board.")
            val = input()
        else:
            entry_val = True
    offical_board[int(val) - 1] = "X"
    print("USER TURN 2", offical_board, game_status)
    print_board()
    return 

def computer_turn():
    print("COMPUTER TURN 1", offical_board, game_status)
    opts = check_options(offical_board)
    print("COMPUTER TURN OPTS FROM CHECK_OPTIONS OUTPUT: ", opts)
    print("COMPUTER TURN 2", offical_board, game_status)
    for y in range(9):
        if str(offical_board[y]).isalpha():
            opts[y] = -100000
    print("COMPUTER TURN 3", offical_board, game_status)
    highest = max(opts)
    print("COMPUTER TURN 4", offical_board, game_status)
    loc = opts.index(highest)
    offical_board[loc] = "O"
    print("COMPUTER TURN 5", offical_board, game_status)
    print("Here is my response to your move!")
    print_board()
    return

def check_state(board):
    print("OFFICAL BOARD: ", offical_board)
    print("CHECK STATE BOARD", board, board.count("X"), board.count("O"))
    options = [board[0:3], board[3:6], board[6:9], [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]], [board[0], board[4], board[8]], [board[2], board[4], board[6]]]
    for option in options:
        if option.count("X") == 3:
            return "X win"
        elif option.count("O") == 3:
            return "O win"
    print("CHECK STATE COUNT OF X AND O: ", board, board.count("X"), board.count("O"))
    if board.count("X") + board.count("O") == 9:
        print("TIE!!!!!!!!!! IN CHECK STATE")
        return "Tie"
    return "Unfinished"

def check_options(board):
    print("CHECK_OPTIONS 1", offical_board, game_status)
    board_copy = []
    board_copy_copy = []
    chances = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for y in range(9):
        board_copy = list(board)
        # print("CHECK_OPTIONS 2",board_copy, offical_board, game_status)
        if str(board_copy[y]).isdigit():
            board_copy[y] = "O"
            out = check_state(board_copy)
            if out == "O win":
                print("O WIN!!!!!!!!!!")
                chances[y] += 50
            elif out == "Unfinished":
                for z in range(9):
                    board_copy_copy = list(board_copy)
                    if str(board_copy_copy[z]).isdigit():
                        board_copy_copy[z] = "X"
                        outx = check_state(board_copy_copy)
                        if outx == "X win":
                            print("X WIN!!!!!!!!!!")
                            chances[y] -= 50
                        elif outx == "Tie":
                            print("TIE!!!!!!!!!!")
                            chances[y] += 1
                        elif outx == "O win":
                            print("ERROR: THIS SHOULD NOT BE BEING CALLED FROM CHECK_OPTIONS")
                        else:
                            chances[y] += sum(check_options(board_copy_copy))

    print("CHECK_OPTIONS 3", chances)
    return chances
[-6192, 0, -6398, -2448, -2150, -2150, -2150, -2300, -1900]
[-7043, -8090, -5796, -6344, 0, -5248, -5097, -5198, -4045]


# X O X
# O O X
# X 8 9

# ["X", "O", "X", "O", "O", "X", "X", 8 ,9]
# chances = [0, 0, 0, 0, 0, 0, 0, 50, 1]









start_game()