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
WHITE = (163, 163, 145)
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

selected_piece = None
selected_position = (0, 0)

# Inicijalizacija šahovske ploče kao 8x8 matrice
chess_board = [[None for _ in range(8)] for _ in range(8)]

# Postavljanje bijelih figura
for i in range(8):
    chess_board[6][i] = 'white_pawn'
chess_board[7][0] = 'white_rook'
chess_board[7][7] = 'white_rook'
chess_board[7][1] = 'white_knight'
chess_board[7][6] = 'white_knight'
chess_board[7][2] = 'white_bishop'
chess_board[7][5] = 'white_bishop'
chess_board[7][3] = 'white_queen'
chess_board[7][4] = 'white_king'

# Postavljanje crnih figura
for i in range(8):
    chess_board[1][i] = 'black_pawn'
chess_board[0][0] = 'black_rook'
chess_board[0][7] = 'black_rook'
chess_board[0][1] = 'black_knight'
chess_board[0][6] = 'black_knight'
chess_board[0][2] = 'black_bishop'
chess_board[0][5] = 'black_bishop'
chess_board[0][3] = 'black_queen'
chess_board[0][4] = 'black_king'




# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Pretvorite koordinate miša u indekse ploče
            row = y // 100
            col = x // 100
            selected_position = (row, col)
            # Ovdje dodajte logiku za određivanje koja je figura odabrana
            selected_piece = chess_board[row][col]
        elif event.type == pygame.MOUSEBUTTONUP and selected_piece:
            new_x, new_y = event.pos
            new_row = new_y // 100
            new_col = new_x // 100
            chess_board[new_row][new_col] = selected_piece
            chess_board[selected_position[0]][selected_position[1]] = None
            selected_piece = None

    
    # Clear the screen and redraw everything
    screen.fill(WHITE)
    
    
    # Code for drawing the chessboard and pieces
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(col*100, row*100, 100, 100))

            piece = chess_board[row][col]
            if piece:
                if piece == 'white_pawn':
                    screen.blit(white_pawn, (col * 100, row * 100))
                elif piece == 'black_pawn':
                    screen.blit(black_pawn, (col * 100, row * 100))
                elif piece == 'white_rook':
                    screen.blit(white_rook, (col * 100, row * 100))
                elif piece == 'black_rook':
                    screen.blit(black_rook, (col * 100, row * 100))
                elif piece == 'white_knight':
                    screen.blit(white_knight, (col * 100, row * 100))
                elif piece == 'black_knight':
                    screen.blit(black_knight, (col * 100, row * 100))
                elif piece == 'white_bishop':
                    screen.blit(white_bishop, (col * 100, row * 100))
                elif piece == 'black_bishop':
                    screen.blit(black_bishop, (col * 100, row * 100))
                elif piece == 'white_queen':
                    screen.blit(white_queen, (col * 100, row * 100))
                elif piece == 'black_queen':
                    screen.blit(black_queen, (col * 100, row * 100))
                elif piece == 'white_king':
                    screen.blit(white_king, (col * 100, row * 100))
                elif piece == 'black_king':
                    screen.blit(black_king, (col * 100, row * 100))
            

    for row in range(8):
        for col in range(8):
            piece = chess_board[row][col]
            if piece:
                # Ovdje dodajte kod za crtanje figure na osnovu tipa figure
                # Na primjer: screen.blit(figure_image, (col*100, row*100))
                pass


    
    pygame.display.flip()

# Closing Pygame and releasing resources
pygame.quit()
sys.exit()
