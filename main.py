# 1 = X
# 2 = O

# Function to check if there is a winner
# GameBoard: The GameBoard the game is being played on
def checkWin(GameBoard):
      # First lets check horizontal wins
      for x in range(GAMEBOARDSIZE):
            if (GameBoard[0][x] == GameBoard[1][x] == GameBoard[2][x] == 1 or GameBoard[0][x] == GameBoard[1][x] == GameBoard[2][x] == 2):
                  return True     
      # Second check vertical wins
      for x in range(GAMEBOARDSIZE):
            if (GameBoard[x][0] == GameBoard[x][1] == GameBoard[x][2] == 1 or GameBoard[x][0] == GameBoard[x][1] == GameBoard[x][2] == 2):
                  return True    
      # Lastly, Check for diagonal wins
      if (GameBoard[0][2] == GameBoard[1][1] == GameBoard[2][0] == 1 or GameBoard[0][2] == GameBoard[1][1] == GameBoard[2][0] == 2):
           return True
      if (GameBoard[0][0] == GameBoard[1][1] == GameBoard[2][2] == 1 or GameBoard[0][0] == GameBoard[1][1] == GameBoard[2][2] == 2):
           return True
      # All wins were checked for, no one won yet
      return False

# Displays the current board to the console
# GAMEBOARDSIZE: The size of the gameboard (2x2? 3x3?)
# GameBoard: The GameBoard the Game is being played on
def display(GAMEBOARDSIZE, GameBoard):
      for x in range(GAMEBOARDSIZE):
       print("-------------------------\n")
       print("|", end="")
       for i in range(GAMEBOARDSIZE):
          if GameBoard[x][i] == 2:
            print("  O   |", end=" ")
          if GameBoard[x][i] == 1:
            print("  X   |", end=" ")
          if GameBoard[x][i] == 0:
            print("      |", end=" ")
       print("\n")
     
# Places an X or O on the Gameboard 
# Player: Is it X (1) or O (2)  
# GameBoard: The GameBoard the Game is being played on 
def placeLetter(Player, GameBoard):
     inputNeeded = True
     while inputNeeded:
      if (Player == 1):
         row = input("Where would you like place your X? Input the row (1, 2, or 3) first:\n")
      else:
         row = input("Where would you like place your O? Input the row (1, 2, or 3) first:\n")
          
      col = input("Now input the column (1, 2, or 3):\n")

      if (GameBoard[int(row)-1][int(col)-1] == 0):
       if (Player == 1):
        GameBoard[int(row)-1][int(col)-1] = 1
        inputNeeded = False
       else: 
        GameBoard[int(row)-1][int(col)-1] = 2
        inputNeeded = False
      else:
          print("This position already has a letter in it, please choose another position.")
          

# Size of the board
GAMEBOARDSIZE = 3
# Making the board
GameBoard = [[0 for i in range(GAMEBOARDSIZE)] for j in range(GAMEBOARDSIZE)]
          
print("Welcome to my game of TicTacToe!")
XWin = False

while True:
        #X's turn
      placeLetter(1, GameBoard)
        # Checking if X Won
      if checkWin(GameBoard):
            XWin = True
            break
      display(GAMEBOARDSIZE, GameBoard)
        # O's turn
      placeLetter(2, GameBoard)
        # Checking if O Won
      if checkWin(GameBoard):
            break
      display(GAMEBOARDSIZE, GameBoard)

print("Victory!")
display(GAMEBOARDSIZE, GameBoard)


