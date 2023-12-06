#First lets make a game of tictactoe

GAMEBOARDSIZE = 3

GameBoard = [[0 for i in range(GAMEBOARDSIZE)] for j in range(GAMEBOARDSIZE)]

# 1 = X
# 2 = O

def checkWin():
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


def display():
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
     
      

print("Welcome to my game of TicTacToe!")
XWin = False

while True:
        #X's turn
      row = input("Where would you like place your X? Input the row (1, 2, or 3) first:\n")
      col = input("Now input the column (1, 2, or 3):\n")
      GameBoard[int(row)-1][int(col)-1] = 1
        # Checking if X Won
      if checkWin():
            XWin = True
            break
      display()
        # O's turn
      row = input("Where would you like place your O? Input the row (1, 2, or 3) first:\n")
      col = input("Now input the column (1, 2, or 3):\n")
      GameBoard[int(row)-1][int(col)-1] = 2
        # Checking if O Won
      if checkWin():
            break
      display()



print("Victory!")
display()


