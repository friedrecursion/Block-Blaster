import pygame
import sys
from constants import CELL_SIZE, BACKGROUND_COLOR, WIDTH, HEIGHT
from board import Board
from draw import draw

    
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Block Blast")
    clock = pygame.time.Clock()

    board = Board()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click event
                x, y = event.pos  # Get the mouse click coordinates
                board.add_block((x // CELL_SIZE, y // CELL_SIZE))
           
        screen.fill(BACKGROUND_COLOR)
        draw(screen,board)

        pygame.display.flip()
        clock.tick(15)

if __name__ == "__main__":
    main()
