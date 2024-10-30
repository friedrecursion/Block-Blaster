import pygame

from constants import RGB_COLORS,OUT_OF_BOUND,HOVER_ALPHA, CELL_SIZE, LINE_COLOR, LINE_THICKNESS, BOARD_SIZE, MARGIN_TOP, MARGIN_SIDE
from board import Board

def draw(screen,board,mouse_position):

    # Draw the Grid
    for i in range(board.n + 1):
        # Draw vertical lines
        pygame.draw.line(screen, LINE_COLOR, (MARGIN_SIDE + i * CELL_SIZE, MARGIN_TOP), (MARGIN_SIDE + i * CELL_SIZE, MARGIN_TOP + BOARD_SIZE), LINE_THICKNESS)
        # Draw horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (MARGIN_SIDE, MARGIN_TOP + i * CELL_SIZE), (MARGIN_SIDE + BOARD_SIZE, MARGIN_TOP + i * CELL_SIZE), LINE_THICKNESS)
    
     # Draw Blocks
    for row, board_row in enumerate(board.board):
        for col, color in enumerate(board_row): 
            position = (col,row)
            draw_square(screen,position,RGB_COLORS[color])

    # Draw Hover overlay of next Block
    if board.can_add_block(mouse_position):
        col,row = mouse_position
        for shape_col, shape_row in board.shape:
            position = (col + shape_col,row + shape_row)
            block = board.get_block(position)
            # if board.get_block(position) != OUT_OF_BOUND:
            hover = tuple([int(((255 - HOVER_ALPHA)/255)*RGB_COLORS[block][i]) + int(HOVER_ALPHA*RGB_COLORS[board.color][i]/255) for i in range(3)])
            draw_square(screen,position,hover)
            

def draw_square(screen,position,color):
    col,row = position
    square = pygame.Rect(MARGIN_SIDE + 1 + col * CELL_SIZE + LINE_THICKNESS//2,MARGIN_TOP + 1 + row * CELL_SIZE + LINE_THICKNESS//2, CELL_SIZE - LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS)
    pygame.draw.rect(screen, color, square)
