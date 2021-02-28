# Project idea: Tic Tac Toe App //
# welcome page
    # -user login and registration APP(username, email, PW)---User model **one to one
# Main game page/profile
    # -player avatar, levels up per number of wins ---wins model ***one to many
    # -play against computer
    # -play against a person
    # -change difficulty
    # create board on front end and play game
# 1. create game board
# 2. diplay board
# 3. Play the game
#       -handle turn
# 4 check if win
    # -check rows 
    # -check columns
    # check diagonals
# 5. check tie
# 6. flip player
#-----global variables-------
    #Game Board
board =[["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]

	#If game is still going
game_still_going =True

	#Who won? Or tie?
winner = None

	#Who's turn is it
current_player = "X"

#Display board
	
def display_board():
	return board

#Play game function of tic tac toe
	
def play_game():
		# display initial board
	display_board()

		# while the game is still going
	while game_still_going:

			# handle a single turn
		handle_turn(current_player)

			# check if the game has ended
		check_if_game_over()

			# flip to the other player
		flip_player()

		# the game has ended
	if winner == "X" or winner == "O":
			print(winner + "Won!")
	elif winner == None:
			print ("tie")

# Handle a single turns function of a player (take in input, and render on board
	
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position 1-9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position 1-9: ")

        position = int(position) - 1
    
        if board[position] == "-":
            valid = True
        else:
            print ("You can’t go there. Go again.")

        board[position] = player

        display_board()

#Check win function function

def check_for_winner():
    # Set up global variables
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

#Check rows
def check_rows():
    # set up game variables
    global game_still_going
    #check if any of the roses have all the same value( and not empty)
    row1 = board[0] == board[1] ==board[2] != "-"
    row2 = board[3] == board[4] ==board[5] != "-"
    row3 = board[6] == board[7] ==board[8] != "-"
    # if any row does match, flag that there is a win
    if row1 or row2 or row3:
        game_still_going =False
    # return the winner (X or O)
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

#Check columns
def check_columns():
    # set up game variables
    global game_still_going
    #check if any of the roses have all the same value( and not empty)
    column1 = board[0] == board[3] ==board[6] != "-"
    column2 = board[1] == board[5] ==board[7] != "-"
    column3 = board[2] == board[6] ==board[8] != "-"
    # if any row does match, flag that there is a win
    if column1 or column2 or column3:
        game_still_going =False
    # return the winner (X or O)
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

#Check diagonals
def check_diagonals ():
# set up game variables
    global game_still_going
    #check if any of the roses have all the same value( and not empty)
    diagonal1 = board[0] == board[4] ==board[8] != "-"
    diagonal2 = board[2] == board[4] ==board[6] != "-"
    # if any row does match, flag that there is a win
    if diagonal1 or diagonal2:
        game_still_going =False
    # return the winner (X or O)
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[1]


#Check tie function

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

#Check if game over
def check_if_game_over():
    check_for_winner()
    check_if_tie()

#Flip player function- X or O turn

def flip_player():
    # set global variable
    global current_player
        # if current player was X, then change it to O
    if current_player == "X":
        current_player == "O"
    # if current player was O, then chance it to X
    elif current_player == "O":
        current_player == "X"
    return