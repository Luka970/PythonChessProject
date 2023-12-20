# Import libraries
import pygame
import sys

# Initializing Pygame
pygame.init()

# Setting up the window
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Python Chess')

# Colors
WHITE = (238, 238, 210)
GREEN = (0, 255, 0)
BLACK = (118, 150, 86)

# Loading images of white figures
white_king = pygame.image.load('images/king (1).png')
white_queen = pygame.image.load('images/queen (1).png')
white_bishop = pygame.image.load('images/bishop (1).png')
white_knight = pygame.image.load('images/chess (1).png')
white_rook = pygame.image.load('images/chess-piece (1).png')
white_pawn = pygame.image.load('images/chess-pawn (1).png')

# Loading pictures of black figures
black_king = pygame.image.load('images/king.png')
black_queen = pygame.image.load('images/queen.png')
black_bishop = pygame.image.load('images/bishop.png')
black_knight = pygame.image.load('images/chess.png')
black_rook = pygame.image.load('images/chess-piece.png')
black_pawn = pygame.image.load('images/chess-pawn.png')

# Defining pieces sizes
piece_size = (64, 64)

# Scaling black pieces
black_king = pygame.transform.scale(black_king, piece_size)
black_queen = pygame.transform.scale(black_queen, piece_size)
black_bishop = pygame.transform.scale(black_bishop, piece_size)
black_knight = pygame.transform.scale(black_knight, piece_size)
black_rook = pygame.transform.scale(black_rook, piece_size)
black_pawn = pygame.transform.scale(black_pawn, piece_size)

# Scaling white pieces
white_king = pygame.transform.scale(white_king, piece_size)
white_queen = pygame.transform.scale(white_queen, piece_size)
white_bishop = pygame.transform.scale(white_bishop, piece_size)
white_knight = pygame.transform.scale(white_knight, piece_size)
white_rook = pygame.transform.scale(white_rook, piece_size)
white_pawn = pygame.transform.scale(white_pawn, piece_size)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Logic for moving pieces will be implemented here
            pass
    
    # Clear the screen and redraw everything
    screen.fill(WHITE)
    
    # Code for drawing the chessboard and pieces will go here
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(col*100, row*100, 100, 100))

    # Updating the display
            
    # Positioning black pawn pieces       
    for i in range(8):
        screen.blit(black_pawn, (i * 100, 6 * 103))
    # Positioning the other black pieces at starting positions
    screen.blit(black_rook, (0, 7 * 102))
    screen.blit(black_knight, (1 * 100, 7 * 102))
    screen.blit(black_bishop, (2 * 100, 7 * 102))
    screen.blit(black_queen, (3 * 100, 7 * 102))
    screen.blit(black_king, (4 * 100, 7 * 102))
    screen.blit(black_bishop, (5 * 100, 7 * 102))
    screen.blit(black_knight, (6 * 100, 7 * 102))
    screen.blit(black_rook, (7 * 100, 7 * 102))

    # Positioning white pawn pieces
    for i in range(8):
        screen.blit(white_pawn, (i * 100, 1 * 120))
    # Positioning the other white pieces at starting positions
    screen.blit(white_rook, (0, 20))
    screen.blit(white_knight, (1 * 100, 20))
    screen.blit(white_bishop, (2 * 100, 20))
    screen.blit(white_queen, (3 * 100, 20))
    screen.blit(white_king, (4 * 100, 20))
    screen.blit(white_bishop, (5 * 100, 20))
    screen.blit(white_knight, (6 * 100, 20))
    screen.blit(white_rook, (7 * 100, 20))
        
    pygame.display.flip()

# Closing Pygame and releasing resources
pygame.quit()
sys.exit()
