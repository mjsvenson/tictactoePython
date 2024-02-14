# Example file showing a basic pygame "game loop"
# Copyright: Matthew Svenson 2024

import pygame

boxs = [0,0,0,0,0,0,0,0,0]
turn = 'X'
win = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Provides functionality for pressing on the box
        if event.type == pygame.MOUSEBUTTONDOWN: 
            # Row 1 functionality
            if boxs[0] == 0:
                if 63 <= mouse[0] <= 258 and 85 <= mouse[1] <= 277: 
                # Edit the box to turn into right symbol
                    if boxs[0] == 0:
                        if turn == "X":
                            boxs[0] = 1
                        if turn == "O":
                            boxs[0] = 2

                    if turn == "X":
                        turn = "O"
                    else:
                        if turn == "O":
                            turn = "X"
            if boxs[1] == 0:
                if 263 <= mouse[0] <= 458 and 85 <= mouse[1] <= 277: 
                    if boxs[1] == 0:
                        if turn == "X":
                            boxs[1] = 1
                        if turn == "O":
                            boxs[1] = 2

                    if turn == "X":
                        turn = "O"
                    else:
                        if turn == "O":
                            turn = "X"
            if boxs[2] == 0:
                if 463 <= mouse[0] <= 658 and 85 <= mouse[1] <= 277: 
                    if boxs[2] == 0:
                        if turn == "X":
                            boxs[2] = 1
                        if turn == "O":
                            boxs[2] = 2

                    if turn == "X":
                        turn = "O"
                    else:
                        if turn == "O":
                            turn = "X"

            # Row 2 functionality
            if boxs[3] == 0:
                if 63 <= mouse[0] <= 258 and 285 <= mouse[1] <= 477: 
                    if boxs[3] == 0:
                        if turn == "X":
                            boxs[3] = 1
                        if turn == "O":
                            boxs[3] = 2

                    if turn == "X":
                        turn = "O"
                    else:
                        if turn == "O":
                            turn = "X"
            if boxs[4] == 0:
                if 263 <= mouse[0] <= 458 and 285 <= mouse[1] <= 477: 
                    if boxs[4] == 0:
                        if turn == "X":
                            boxs[4] = 1
                        if turn == "O":
                            boxs[4] = 2

                    if turn == "X":
                        turn = "O"
                    else:
                        if turn == "O":
                            turn = "X"
                
            if 463 <= mouse[0] <= 658 and 285 <= mouse[1] <= 477: 
                if boxs[5] == 0:
                        if turn == "X":
                            boxs[5] = 1
                        if turn == "O":
                            boxs[5] = 2

                        if turn == "X":
                            turn = "O"
                        else:
                            if turn == "O":
                                turn = "X"
            
            # Row 3 functionality
            if boxs[6] == 0:
                if 63 <= mouse[0] <= 258 and 485 <= mouse[1] <= 677: 
                    if boxs[6] == 0:
                        if turn == "X":
                            boxs[6] = 1
                        if turn == "O":
                            boxs[6] = 2

                    if turn == "X":
                        turn = "O"
                    else:
                        if turn == "O":
                            turn = "X"
            if boxs[7] == 0:
                if 263 <= mouse[0] <= 458 and 485 <= mouse[1] <= 677: 
                    if boxs[7] == 0:
                        if turn == "X":
                            boxs[7] = 1
                        if turn == "O":
                            boxs[7] = 2

                    if turn == "X":
                        turn = "O"
                    else:
                        if turn == "O":
                            turn = "X"
            if boxs[8] == 0:
                if 463 <= mouse[0] <= 658 and 485 <= mouse[1] <= 677: 
                    if boxs[8] == 0:
                        if turn == "X":
                            boxs[8] = 1
                        if turn == "O":
                            boxs[8] = 2

                    if turn == "X":
                        turn = "O"
                    else:
                        if turn == "O":
                            turn = "X"


    # RENDER YOUR GAME HERE
    pygame.display.set_caption("EVIL Tic-Tac-Toe")
    # flip() the display to put your work on screen
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(60, 80, 600, 600), 2)
    # Vertical lines for the tic tac toe game
    pygame.draw.line(screen, (0,0,0), (260,80), (260,678))
    pygame.draw.line(screen, (0,0,0), (460,80), (460,678))
    # Horizontal lines for the tic tac toe game
    pygame.draw.line(screen, (0,0,0), (60,280), (659,280))
    pygame.draw.line(screen, (0,0,0), (60,480), (659,480))

    # Text for the game
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('It is {}\'s turn'.format(turn), True, (0,0,0), (255,255,255))
    textRect = text.get_rect()
    textRect.center = (360, 20)
    screen.blit(text, textRect)

    # Get the mouse position for checking which button was pressed
    mouse = pygame.mouse.get_pos() 

    print(turn)

    # Draws current status of board 
    if boxs[0] == 1:
         pygame.draw.line(screen, (0,0,0), (63, 85), (255, 277))
         pygame.draw.line(screen, (0,0,0), (255, 85), (63, 277))
    if boxs[0] == 2:
        pygame.draw.circle(screen, (0,0,0), (160, 180), 100, 1)

    if boxs[1] == 1:
         pygame.draw.line(screen, (0,0,0), (263, 85), (458, 277))
         pygame.draw.line(screen, (0,0,0), (458, 85), (263, 277))
    if boxs[1] == 2:
         pygame.draw.circle(screen, (0,0,0), (360, 180), 100, 1)

    if boxs[2] == 1:
         pygame.draw.line(screen, (0,0,0), (463, 85), (658, 277))
         pygame.draw.line(screen, (0,0,0), (658, 85), (463, 277))
    if boxs[2] == 2:
         pygame.draw.circle(screen, (0,0,0), (560, 180), 100, 1)

    if boxs[3] == 1:
         pygame.draw.line(screen, (0,0,0), (63, 285), (255, 477))
         pygame.draw.line(screen, (0,0,0), (255, 285), (63, 477))
    if boxs[3] == 2:
         pygame.draw.circle(screen, (0,0,0), (160, 380), 100, 1)

    if boxs[4] == 1:
         pygame.draw.line(screen, (0,0,0), (263, 285), (455, 477))
         pygame.draw.line(screen, (0,0,0), (455, 285), (263, 477))
    if boxs[4] == 2:
         pygame.draw.circle(screen, (0,0,0), (360, 380), 100, 1)
    
    if boxs[5] == 1:
         pygame.draw.line(screen, (0,0,0), (463, 285), (655, 477))
         pygame.draw.line(screen, (0,0,0), (655, 285), (463, 477))
    if boxs[5] == 2:
         pygame.draw.circle(screen, (0,0,0), (560, 380), 100, 1)

    if boxs[6] == 1:
         pygame.draw.line(screen, (0,0,0), (63, 485), (255, 677))
         pygame.draw.line(screen, (0,0,0), (255, 485), (63, 677))
    if boxs[6] == 2:
         pygame.draw.circle(screen, (0,0,0), (160, 580), 100, 1)
        
    if boxs[7] == 1:
         pygame.draw.line(screen, (0,0,0), (263, 485), (455, 677))
         pygame.draw.line(screen, (0,0,0), (455, 485), (263, 677))
    if boxs[7] == 2:
         pygame.draw.circle(screen, (0,0,0), (360, 580), 100, 1)

    if boxs[8] == 1:
         pygame.draw.line(screen, (0,0,0), (463, 485), (655, 677))
         pygame.draw.line(screen, (0,0,0), (655, 485), (463, 677))
    if boxs[8] == 2:
         pygame.draw.circle(screen, (0,0,0), (560, 580), 100, 1)
   
    # Horizontal wins X or O
    if (boxs[0] == boxs[1] == boxs[2] == 1):
        win = 1
    if (boxs[3] == boxs[4] == boxs[5] == 1):
        win = 1
    if (boxs[6] == boxs[7] == boxs[8] == 1):
        win = 1
    if (boxs[0] == boxs[1] == boxs[2] == 2):
        win = 2
    if (boxs[3] == boxs[4] == boxs[5] == 2):
        win = 2
    if (boxs[6] == boxs[7] == boxs[8] == 2):
        win = 2

    # Vertical wins X or O
    if (boxs[0] == boxs[3] == boxs[6] == 1):
        win = 1
    if (boxs[1] == boxs[4] == boxs[7] == 1):
        win = 1
    if (boxs[2] == boxs[5] == boxs[8] == 1):
        win = 1
    if (boxs[0] == boxs[3] == boxs[6] == 2):
        win = 2
    if (boxs[1] == boxs[4] == boxs[7] == 2):
        win = 2
    if (boxs[2] == boxs[5] == boxs[8] == 2):
        win = 2

    # Diagonal wins X or O
    if (boxs[0] == boxs[4] == boxs[8] == 1):
        win = 1
    if (boxs[2] == boxs[4] == boxs[6] == 1):
        win = 1
    if (boxs[0] == boxs[4] == boxs[8] == 2):
        win = 2
    if (boxs[2] == boxs[4] == boxs[6] == 2):
        win = 2


    if (win == 1):
        font = pygame.font.Font('freesansbold.ttf', 112)
        text = font.render('X wins!', True, (0,0,0), (255,255,255))
        textRect = text.get_rect()
        textRect.center = (360, 360)
        screen.blit(text, textRect)

    if (win == 2):
        font = pygame.font.Font('freesansbold.ttf', 112)
        text = font.render('O wins!', True, (0,0,0), (255,255,255))
        textRect = text.get_rect()
        textRect.center = (360, 360)
        screen.blit(text, textRect)

    pygame.display.flip()

    



    clock.tick(60)  # limits FPS to 60

pygame.quit()