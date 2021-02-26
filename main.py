
#------ Global variables --------
#Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# Ig game is still going
game_still_going = True

# Who won? or tie?
winner = None

#Who's turn is it?
current_player = "X"

#Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():


# Display initial board
    display_board()
    #while the game is still going
    while game_still_going:
        # handle a single turn of a arbitrary player
        handle_turn(current_player)
        # check if the game ended
        check_if_game_over()
        # FLip to other player
        flip_player()
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie!")

def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    # set up for global variables
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return
def check_rows():
    #set up global variables
    global game_still_going
    #check if any of the rows have the same value (and not empty cells
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    Column_1 = board[0] == board[3] == board[6] != "-"
    Column_2 = board[1] == board[4] == board[7] != "-"
    Column_3 = board[2] == board[5] == board[8] != "-"
    if Column_1 or Column_2 or Column_3:
        game_still_going = False
    if Column_1:
        return board[0]
    elif Column_2:
        return board[1]
    elif Column_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    #Global variabels we need
    global current_player
    #If the current player was x, then change it to O
    if current_player == "X":
        current_player = "O"
    #if the current player was O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()
