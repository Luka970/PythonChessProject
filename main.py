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

# Initializing the chessboard as an 8x8 matrix
chess_board = [[None for _ in range(8)] for _ in range(8)]

# Placing the white pieces
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

# Placing the black pieces
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


# Function definitions for piece movements (pawn_moves, rook_moves, knight_moves, king_moves, queen_moves, bishop_moves)

def pawn_moves(board, x, y, color):
    moves = []
    direction = 1 if color == 'black' else -1
    if 0 <= y + direction < 8:
        if board[y + direction][x] is None:
            moves.append((x, y + direction))
            if (color == 'white' and y == 6) or (color == 'black' and y == 1):
                if board[y + 2 * direction][x] is None:
                    moves.append((x, y + 2 * direction))
        if x > 0 and board[y + direction][x - 1] is not None:
            moves.append((x - 1, y + direction))
        if x < 7 and board[y + direction][x + 1] is not None:
            moves.append((x + 1, y + direction))
    return moves

def rook_moves(board, x, y):
    moves = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x, y
        while True:
            nx, ny = nx + dx, ny + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if board[ny][nx] is None:
                    moves.append((nx, ny))
                else:
                    moves.append((nx, ny))
                    break
            else:
                break
    return moves

def knight_moves(board, x, y):
    moves = []
    L_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for dx, dy in L_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            moves.append((nx, ny))
    return moves

def king_moves(board, x, y):
    moves = []
    directions = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            moves.append((nx, ny))
    return moves

def queen_moves(board, x, y):
    moves = []
    directions = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        nx, ny = x, y
        while True:
            nx, ny = nx + dx, ny + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                moves.append((nx, ny))
                if board[ny][nx] is not None:  
                    break
            else:
                break
    return moves

def bishop_moves(board, x, y):
    moves = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        nx, ny = x, y
        while True:
            nx, ny = nx + dx, ny + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                moves.append((nx, ny))
                if board[ny][nx] is not None:  
                    break
            else:
                break
    return moves

allowed_moves = []

# After initialization
is_white_turn = True


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Convert mouse coordinates to board indices
            row = y // 100
            col = x // 100
            selected_position = (row, col)
            # Add logic here to determine which piece is selected
            selected_piece = chess_board[row][col]
            if selected_piece:
                piece_color = 'white' if 'white' in selected_piece else 'black'
                if is_white_turn and piece_color == 'white' or not is_white_turn and piece_color == 'black':
                    # Reset allowed moves
                    allowed_moves = []
                    # Determine the allowed moves based on the type of the selected piece
                    if 'white_pawn' in selected_piece or 'black_pawn' in selected_piece:
                        color = 'white' if 'white' in selected_piece else 'black'
                        allowed_moves = pawn_moves(chess_board, col, row, color)
                    elif 'rook' in selected_piece:
                        allowed_moves = rook_moves(chess_board, col, row)
                    elif 'knight' in selected_piece:
                        allowed_moves = knight_moves(chess_board, col, row)
                    elif 'white_king' in selected_piece or 'black_king' in selected_piece:
                        allowed_moves = king_moves(chess_board, col, row)
                    elif 'white_queen' in selected_piece or 'black_queen' in selected_piece:
                        allowed_moves = queen_moves(chess_board, col, row)
                    elif 'white_bishop' in selected_piece or 'black_bishop' in selected_piece:
                        allowed_moves = bishop_moves(chess_board, col, row)
        elif event.type == pygame.MOUSEBUTTONUP and selected_piece:
            new_x, new_y = event.pos
            new_row = new_y // 100
            new_col = new_x // 100
            # Check if the move is within the allowed moves for the selected piece
            if (new_col, new_row) in allowed_moves:
                chess_board[new_row][new_col] = selected_piece
                chess_board[selected_position[0]][selected_position[1]] = None
                is_white_turn = not is_white_turn
            selected_piece = None
    
    # Clear the screen and redraw everything
    screen.fill(WHITE)
    
    
    # Code for drawing the chessboard and pieces
    for row in range(8):
        for col in range(8):
            # Determine the color of the square based on its position
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(col*100, row*100, 100, 100))
            piece = chess_board[row][col]
            if piece:
                # Calculate the centered position
                centered_x = col * 100 + (100 - piece_size[0]) // 2
                centered_y = row * 100 + (100 - piece_size[1]) // 2
                if piece == 'white_pawn':
                    screen.blit(white_pawn, (centered_x, centered_y))
                elif piece == 'black_pawn':
                    screen.blit(black_pawn, (centered_x, centered_y))
                elif piece == 'white_rook':
                    screen.blit(white_rook, (centered_x, centered_y))
                elif piece == 'black_rook':
                    screen.blit(black_rook, (centered_x, centered_y))
                elif piece == 'white_knight':
                    screen.blit(white_knight, (centered_x, centered_y))
                elif piece == 'black_knight':
                    screen.blit(black_knight, (centered_x, centered_y))
                elif piece == 'white_bishop':
                    screen.blit(white_bishop, (centered_x, centered_y))
                elif piece == 'black_bishop':
                    screen.blit(black_bishop, (centered_x, centered_y))
                elif piece == 'white_queen':
                    screen.blit(white_queen, (centered_x, centered_y))
                elif piece == 'black_queen':
                    screen.blit(black_queen, (centered_x, centered_y))
                elif piece == 'white_king':
                    screen.blit(white_king, (centered_x, centered_y))
                elif piece == 'black_king':
                    screen.blit(black_king, (centered_x, centered_y))
            

    for row in range(8):
        for col in range(8):
            piece = chess_board[row][col]
            if piece:
                pass


    # Update the display with the new drawing
    pygame.display.flip()

# Closing Pygame and releasing resources
pygame.quit()
sys.exit()
