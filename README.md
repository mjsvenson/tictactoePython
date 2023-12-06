# EVILtictactoe
YOU WILL NEVER WIN AGAINST ME!!!

Evil TicTacToe is an attempt at making a TicTacToe AI that you can never win against.

11/27/2023:
Created the backend for the game (Need to add diagonal wins).
Created text display for the game after every turn

12/5/2023:
Error message that pops up after every first execution but works perfectly fine any other time??
Traceback (most recent call last):
  File "c:\Users\thein\Documents\GitHub\EVILtictactoe\main.py", line 58, in <module>
    GameBoard[int(row)-1][int(col)-1] = 2
                          ^^^^^^^^
ValueError: invalid literal for int() with base 10: '& C:/Users/thein/AppData/Local/Programs/Python/Python311/python.exe c:/Users/thein/Documents/GitHub/EVILtictactoe/main.py'

Added functionality to make sure players cannot overwrite other players letters in the gameboard

