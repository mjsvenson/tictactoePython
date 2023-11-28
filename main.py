#First lets make a game of tictactoe

GAMEBOARDSIZE = 3

GameBoard = [[0]*GAMEBOARDSIZE]*GAMEBOARDSIZE

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
            
      return False
      

print("Welcome to my game of TicTacToe!")
XWin = False
victory = False

while not victory:
        #X's turn
      col = input("Where would you like place your X? Input the column first\n")
      row = input("Now input the row\n")
      GameBoard[int(col)-1][int(row)-1] = 1
        # XWin is checking whether X is the winner or not
      XWin = True
      victory = checkWin()
      XWin = False
        # O's turn
      col = input("Where would you like place your O? Input the column first\n")
      row = input("Now input the row\n")
      GameBoard[int(col)-1][int(row)-1] = 2
      victory = checkWin()

print("Victory!")
