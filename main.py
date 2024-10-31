import pygame
import sys
from constants import BOARD_SIZE,CELL_SIZE, BACKGROUND_COLOR, WIDTH, HEIGHT, MARGIN_SIDE,MARGIN_TOP
from board import Board
from draw import draw

    
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Block Blast")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 100)

    board = Board()
    frame_count = 0
    while True:
        x,y = pygame.mouse.get_pos()
        offset_x = CELL_SIZE//2 if board.even_width() else 0
        mouse_position = (x - offset_x,y - CELL_SIZE//2)
        board_position = ((x - offset_x - MARGIN_SIDE)//CELL_SIZE,(y - (MARGIN_TOP + CELL_SIZE))//CELL_SIZE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click event
                for i in range(3):
                    if x >= MARGIN_SIDE + (i * 3)*CELL_SIZE and x <= MARGIN_SIDE + (2 + i * 3)*CELL_SIZE and y >= MARGIN_TOP + BOARD_SIZE + 2*CELL_SIZE and y <= MARGIN_TOP + BOARD_SIZE + (2+2)*CELL_SIZE:
                        board.grab_block((x,y),i)
            elif event.type == pygame.MOUSEBUTTONUP:
                board.add_block(board_position)

        screen.fill(BACKGROUND_COLOR)
        draw(screen,board,board_position,mouse_position)

        score_text = font.render(f"{board.score}", True, (255, 255, 255))  # White color
        text_rect = score_text.get_rect(center=(WIDTH // 2, MARGIN_TOP // 2))
        screen.blit(score_text, text_rect)
        
        frame_count += 1
        if frame_count == 5:
            frame_count = 0 
            board.add_score()

        pygame.display.flip()
        clock.tick(60)
        

if __name__ == "__main__":
    main()
