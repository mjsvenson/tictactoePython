# Example file showing a basic pygame "game loop"
import pygame


#def drawTurn(xStart, yStart, xEnd, yEnd, turn):
#    if turn == "X":
#        pygame.draw.line(screen, (0,0,0), (xStart, yStart), (xEnd, yEnd))
#        pygame.draw.line(screen, (0,0,0), (xEnd, yStart), (xStart, yEnd))

boxs = [0,0,0,0,0,0,0,0,0]
turn = 'X'


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

            if 263 <= mouse[0] <= 458 and 85 <= mouse[1] <= 277: 
                pygame.quit();
            if 463 <= mouse[0] <= 658 and 85 <= mouse[1] <= 277: 
                pygame.quit();

            # Row 2 functionality
            if 63 <= mouse[0] <= 258 and 285 <= mouse[1] <= 477: 
                pygame.quit();
            if 263 <= mouse[0] <= 458 and 285 <= mouse[1] <= 477: 
                pygame.quit();
            if 463 <= mouse[0] <= 658 and 285 <= mouse[1] <= 477: 
                pygame.quit();
            
            # Row 3 functionality
            if 63 <= mouse[0] <= 258 and 485 <= mouse[1] <= 677: 
                pygame.quit();
            if 263 <= mouse[0] <= 458 and 485 <= mouse[1] <= 677: 
                pygame.quit();
            if 463 <= mouse[0] <= 658 and 485 <= mouse[1] <= 677: 
                pygame.quit();

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

    pygame.display.flip()


    clock.tick(60)  # limits FPS to 60

pygame.quit()