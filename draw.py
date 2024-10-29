import pygame

from constants import RGB_COLORS,OUT_OF_BOUND,WHITE,HOVER_ALPHA, CELL_SIZE, LINE_COLOR, LINE_THICKNESS, HEIGHT, WIDTH
from board import Board

def draw(screen,board):
    for i in range(board.n + 1):
        # Draw vertical lines
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_THICKNESS)
        # Draw horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_THICKNESS)
    
    for row, board_row in enumerate(board.board):
        for col, color in enumerate(board_row): 
            position = (col,row)
            draw_square(screen,position,RGB_COLORS[color])

    x, y = pygame.mouse.get_pos()
    col,row = (x // CELL_SIZE,y // CELL_SIZE)
    hover_color = board.color
    if not board.can_add_block((col,row)):
        hover_color = WHITE
    for shape_col,shape_row in board.shape:
        position = (col+shape_col,row+shape_row)
        block = board.get_block(position)
        
        if block != OUT_OF_BOUND:
            color = RGB_COLORS[block]
            hover = tuple([int(((255 - HOVER_ALPHA)/255)*color[i]) + int(HOVER_ALPHA*RGB_COLORS[hover_color][i]/255) for i in range(3)])

        draw_square(screen,position,hover)


def draw_square(screen,position,color):
    col,row = position
    square = pygame.Rect(1 + col * CELL_SIZE + LINE_THICKNESS//2,1 + row * CELL_SIZE + LINE_THICKNESS//2, CELL_SIZE - LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS)
    pygame.draw.rect(screen, color, square)
