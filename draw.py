import pygame

from constants import RGB_COLORS,EMPTY,OUT_OF_BOUND,BLEND_ALPHA, WIDTH, HEIGHT, CELL_SIZE, LINE_COLOR, LINE_THICKNESS, BOARD_SIZE, MARGIN_TOP, MARGIN_SIDE
from board import Board

def draw(screen,board,board_position, mouse_position):
    # Draw the Grid
    for i in range(board.n + 1):
        # Draw vertical lines
        pygame.draw.line(screen, LINE_COLOR, (MARGIN_SIDE + i * CELL_SIZE, MARGIN_TOP), (MARGIN_SIDE + i * CELL_SIZE, MARGIN_TOP + BOARD_SIZE), LINE_THICKNESS)
        # Draw horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (MARGIN_SIDE, MARGIN_TOP + i * CELL_SIZE), (MARGIN_SIDE + BOARD_SIZE, MARGIN_TOP + i * CELL_SIZE), LINE_THICKNESS)
    
     # Draw Blocks in the Grid
    for row, board_row in enumerate(board.board):
        for col, color in enumerate(board_row): 
            position = (col,row)
            draw_square_board(screen,position,RGB_COLORS[color])
    
    if board.block_held:
        # Draw Preview of next Block in the Grid
        if board.can_add_block(board_position):
            col,row = board_position
            for shape_col, shape_row in board.shape:
                position = (col + shape_col,row + shape_row)
                blend = tuple([int(((255 - BLEND_ALPHA)/255)*RGB_COLORS[EMPTY][i]) + int(BLEND_ALPHA*RGB_COLORS[board.color][i]/255) for i in range(3)])
                draw_square_board(screen,position,blend)
    
        # Draw Hovering next Block
        mouseX,mouseY = mouse_position
        for shape_col, shape_row in board.shape:
            position = (mouseX + shape_col*CELL_SIZE - CELL_SIZE//2,mouseY + shape_row*CELL_SIZE - CELL_SIZE)
            col,row = board_position
            draw_square_mouse(screen,position,RGB_COLORS[board.color])
    else:
        # Draw next Block below the Grid
        for i in range(3):
            offset_x = 0
            if not board.even_width():
                offset_x = 0.5

            offset_y = (board.height() - 2)/2

            for col,row in board.shape:

                draw_little_square(screen,(col + offset_x,row + offset_y),RGB_COLORS[board.color],i)
    
    # draw debug grids:
    for i in range(5):
        # Draw vertical lines
        pygame.draw.line(screen, LINE_COLOR, (MARGIN_SIDE + i * CELL_SIZE//2, MARGIN_TOP + BOARD_SIZE + 2 * CELL_SIZE), (MARGIN_SIDE + i * CELL_SIZE//2, MARGIN_TOP + BOARD_SIZE + (2 + 2) * CELL_SIZE), LINE_THICKNESS)
        # Draw horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (MARGIN_SIDE, MARGIN_TOP + BOARD_SIZE + 2*CELL_SIZE + i * CELL_SIZE//2 ), (MARGIN_SIDE + 2*CELL_SIZE, MARGIN_TOP + BOARD_SIZE + 2 * CELL_SIZE+ i * CELL_SIZE//2), LINE_THICKNESS)

    # draw debug grids:
    for i in range(5):
        # Draw vertical lines
        pygame.draw.line(screen, LINE_COLOR, (MARGIN_SIDE + 3 * CELL_SIZE + i * CELL_SIZE//2, MARGIN_TOP + BOARD_SIZE + 2 * CELL_SIZE), (MARGIN_SIDE + 3 * CELL_SIZE + i * CELL_SIZE//2, MARGIN_TOP + BOARD_SIZE + (2 + 2) * CELL_SIZE), LINE_THICKNESS)
        # Draw horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (MARGIN_SIDE + 3 * CELL_SIZE, MARGIN_TOP + BOARD_SIZE + 2*CELL_SIZE + i * CELL_SIZE//2 ), (MARGIN_SIDE + 3 * CELL_SIZE + 2*CELL_SIZE, MARGIN_TOP + BOARD_SIZE + 2 * CELL_SIZE+ i * CELL_SIZE//2), LINE_THICKNESS)

    # draw debug grids:
    for i in range(5):
        # Draw vertical lines
        pygame.draw.line(screen, LINE_COLOR, (MARGIN_SIDE + 6 * CELL_SIZE + i * CELL_SIZE//2, MARGIN_TOP + BOARD_SIZE + 2 * CELL_SIZE), (MARGIN_SIDE + 6 * CELL_SIZE + i * CELL_SIZE//2, MARGIN_TOP + BOARD_SIZE + (2 + 2) * CELL_SIZE), LINE_THICKNESS)
        # Draw horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (MARGIN_SIDE + 6 * CELL_SIZE, MARGIN_TOP + BOARD_SIZE + 2*CELL_SIZE + i * CELL_SIZE//2 ), (MARGIN_SIDE + 6 * CELL_SIZE + 2*CELL_SIZE, MARGIN_TOP + BOARD_SIZE + 2 * CELL_SIZE+ i * CELL_SIZE//2), LINE_THICKNESS)

def draw_little_square(screen,board_position,color,index):
    col,row = board_position
    square = pygame.Rect(1 + MARGIN_SIDE + (0.5 + 3*index) * CELL_SIZE + col*CELL_SIZE//2 + LINE_THICKNESS//2,1 + MARGIN_TOP + BOARD_SIZE + 3 * CELL_SIZE + row*CELL_SIZE//2 + + LINE_THICKNESS//2, CELL_SIZE//2 - LINE_THICKNESS, CELL_SIZE//2 - LINE_THICKNESS)
    pygame.draw.rect(screen, color, square)

def draw_square_mouse(screen,mouse_position,color):
    mouseX,mouseY = mouse_position
    square = pygame.Rect(mouseX,mouseY, CELL_SIZE - LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS)
    pygame.draw.rect(screen, color, square)

def draw_square_board(screen,board_position,color):
    col,row = board_position
    square = pygame.Rect(MARGIN_SIDE + 1 + col * CELL_SIZE + LINE_THICKNESS//2,MARGIN_TOP + 1 + row * CELL_SIZE + LINE_THICKNESS//2, CELL_SIZE - LINE_THICKNESS, CELL_SIZE - LINE_THICKNESS)
    pygame.draw.rect(screen, color, square)
