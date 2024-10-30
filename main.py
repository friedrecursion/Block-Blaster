import pygame
import sys
from constants import CELL_SIZE, BACKGROUND_COLOR, WIDTH, HEIGHT, MARGIN_SIDE,MARGIN_TOP
from board import Board
from draw import draw

    
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Block Blast")
    clock = pygame.time.Clock()

    board = Board()
    
    while True:
        x,y = pygame.mouse.get_pos()
        mouse_position = (x,y)
        board_position = ((x-MARGIN_SIDE)//CELL_SIZE,(y-(MARGIN_TOP + CELL_SIZE))//CELL_SIZE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click event
                board.add_block(board_position)
           
        screen.fill(BACKGROUND_COLOR)
        draw(screen,board,board_position,mouse_position)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
