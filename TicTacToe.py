# Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#if game is still going
game_still_going = True

#who won/tie?
winner = None

#whose turn is it?
current_player = "X"

# display board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


# play a game of noughts and crosses
def play_game():

  #display initial board
  display_board()

  #while the game is still going
  while game_still_going:

    # handle a signle turn of an arbitary player
     handle_turn(current_player)

     #check if game has ended
     check_if_game_over()

     #flip player to other user
     flip_player()
  # the game has ended
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("This is a tie.") 


# handle a signle turn of an arbitary player
def handle_turn(player):
 
 print(player + "'s turn")
 position = input("Choose a position from 1 to 9: ")
 valid = False

 while not valid:
   while position not in ["1","2","3","4","5","6","7","8","9"]:
     position = input("Invalid input. Choose a position from 1 to 9: ")
    
   position = int(position) - 1
    
   if board[position] == "-":
      valid = True
   else:
      print("You cannot go there. Try again!")
      
 board[position] = player

 display_board()


def check_if_game_over():
  check_if_there_is_win()
  check_if_tie()


def check_if_there_is_win():
  
  #set up global variable
  global winner

  #check rows
  row_winner = check_rows()

  #check columns
  column_winner = check_columns

  #check diagonal
  diagonal_winner = check_diagonal

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
 #Set up global variable
 global game_still_going

 #Check if any of the rows have the same value
 row_1 = board[0] == board[1] == board[2] != "-"
 row_2 = board[3] == board[4] == board[5] != "-"
 row_3 = board[6] == board[7] == board[8] != "-"
 
 #if any row does have a match, flag that there is a row win
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
 #Set up global variable
 global game_still_going

 #Check if any of the column have the same value
 column_1 = board[0] == board[3] == board[6] != "-"
 column_2 = board[1] == board[4] == board[7] != "-"
 column_3 = board[2] == board[5] == board[8] != "-"
 
 #if any column does have a match, flag that there is a column win
 if column_1 or column_2 or column_3:
   game_still_going = False

 if column_1:
   return board[0]
 elif column_2:
   return board[1]
 elif column_3:
   return board[2]
 
 return

def check_diagonal():
 #Set up global variable
 global game_still_going

 #Check if any of the diagonal have the same value
 diagonal_1 = board[0] == board[5] == board[8] != "-"
 diagonal_2 = board[6] == board[4] == board[2] != "-"
 
 #if any diagonal does have a match, flag that there is a diagonal win
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
 #the global variable that we need
 global current_player

 if current_player == "X":
   current_player = "O"
 elif current_player == "O":
   current_player = "X"

play_game()

# play a game
# handle turn
# check win
#check rows
#check columns
#check diagonals
# check tie
#flip player
