# Example file showing a basic pygame "game loop"
import pygame


# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: 
            pygame.quit();

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

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
    turn = "O"
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('It is {}\'s turn'.format(turn), True, (0,0,0), (255,255,255))
    textRect = text.get_rect()
    textRect.center = (360, 20)
    screen.blit(text, textRect)



    pygame.display.flip()


    clock.tick(60)  # limits FPS to 60

pygame.quit()