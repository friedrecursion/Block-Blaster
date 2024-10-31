import pygame

from constants import RGB_COLORS,EMPTY,OUT_OF_BOUND,BLEND_ALPHA, WIDTH, HEIGHT, CELL_SIZE, LINE_COLOR, BOARD_SIZE, MARGIN_TOP, MARGIN_SIDE
from board import Board

def draw(screen,board,board_position, mouse_position):
    # Draw Blocks in the Grid
    for row, board_row in enumerate(board.board):
        for col, color in enumerate(board_row): 
            position = (col,row)
            if color == EMPTY:
                draw_empty_board(screen,position,RGB_COLORS[color])
            else:
                draw_square_board(screen,position,RGB_COLORS[color])

    
    if board.block_held != None:
        # Draw Preview of next Block in the Grid
        if board.can_add_block(board_position):
            col,row = board_position
            for shape_col, shape_row in board.shape:
                position = (col + shape_col,row + shape_row)
                blend = tuple([int(((255 - BLEND_ALPHA)/255)*RGB_COLORS[EMPTY][i]) + int(BLEND_ALPHA*RGB_COLORS[board.color][i]/255) for i in range(3)])
                draw_square_board(screen,position,blend)

            # color the lines that are completed by shape
            color_lines = lines(board,board_position)
            for square in color_lines:
                draw_square_board(screen,square,RGB_COLORS[board.color])


        # Draw Hovering next Block
        mouseX,mouseY = mouse_position
        for shape_col, shape_row in board.shape:
            position = (mouseX + shape_col*CELL_SIZE - CELL_SIZE//2,mouseY + shape_row*CELL_SIZE - CELL_SIZE)
            col,row = board_position
            draw_square_mouse(screen,position,RGB_COLORS[board.color])
    
    # Draw next three Blocks below the Grid
    for i,shape in enumerate(board.shapes):
        if shape != None:
            offset_x = 0
            if not board.even_width(i):
                offset_x = 0.5
            offset_y = (board.height(i) - 2)/2
            for col,row in shape:
                draw_little_square(screen,(col + offset_x,row + offset_y),RGB_COLORS[board.colors[i]],i)

def lines(board,board_position):
    lines = []
    col, row = board_position
    placed_shape = {(col + shape_col, row + shape_row) for shape_col, shape_row in board.shape}
    for i, row_data in enumerate(board.board):
        if all((x != EMPTY or (j, i) in placed_shape) for j, x in enumerate(row_data)):
            lines.extend((x, i) for x in range(board.n))
    for j in range(board.n):
        if all((board.board[i][j] != EMPTY or (j, i) in placed_shape) for i in range(board.n)):
            lines.extend((j, i) for i in range(board.n))
    return lines

def draw_little_square(screen,board_position,color,index):
    col,row = board_position
    draw_block(screen,color,1 + MARGIN_SIDE + (0.5 + 3*index) * CELL_SIZE + col*CELL_SIZE//2,1 + MARGIN_TOP + BOARD_SIZE + 3 * CELL_SIZE + row*CELL_SIZE//2, CELL_SIZE//2)

def draw_square_mouse(screen,mouse_position,color):
    mouseX,mouseY = mouse_position
    draw_block(screen,color,mouseX,mouseY, CELL_SIZE)

def draw_square_board(screen,board_position,color):
    col,row = board_position
    draw_block(screen,color,MARGIN_SIDE + 1 + col * CELL_SIZE ,MARGIN_TOP + 1 + row * CELL_SIZE , CELL_SIZE)

def draw_empty_board(screen,board_position,color):
    col,row = board_position
    draw_square(screen,color,MARGIN_SIDE + 1 + col * CELL_SIZE,MARGIN_TOP + 1 + row * CELL_SIZE, CELL_SIZE)

def draw_square(screen,color,x,y,size):
    pygame.draw.rect(screen,color,pygame.Rect(x,y,size,size))
    width = CELL_SIZE//15
    pygame.draw.line(screen,LINE_COLOR, (x,y),(x+size,y),width)
    pygame.draw.line(screen,LINE_COLOR,(x+size,y),(x+size,y+size),width)
    pygame.draw.line(screen,LINE_COLOR,(x,y),(x,y+size),width)
    pygame.draw.line(screen,LINE_COLOR,(x,y+size),(x+size,y+size),width)

def draw_block(screen,color,x,y,size):
    pygame.draw.rect(screen,color,pygame.Rect(x,y,size,size))
    n = 8
    # top
    pygame.draw.polygon(screen,adjust_brightness(color,1.4),[(x,y),(x+size/n,y+size/n),(x + (n-1)*size/n ,y+size/n),(x+size,y)])
    # left
    pygame.draw.polygon(screen,adjust_brightness(color,1.2),[(x,y),(x+size/n,y+size/n),(x + size/n ,y+ (n-1)*size/n),(x, y + size)])
    # right
    pygame.draw.polygon(screen,adjust_brightness(color,0.8),[(x+size,y),(x+(n-1)*size/n,y+size/n),(x + (n-1)*size/n ,y+(n-1)*size/n),(x+size,y+size)])
    # bottom
    pygame.draw.polygon(screen,adjust_brightness(color,0.6),[(x,y+size),(x+size/n,y+(n-1)*size/n),(x + (n-1)*size/n ,y+(n-1)*size/n),(x+size,y+size)])

def adjust_brightness(rgb, brightness):
    brightness = max(0, brightness)
    new_rgb = tuple(min(int(c * brightness), 255) for c in rgb)
    return new_rgb
