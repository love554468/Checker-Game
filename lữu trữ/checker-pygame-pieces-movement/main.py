import pygame
from checkers.board import Board
from checkers.constants import HEIGHT, SQUARE_SIZE, WHITE, WIDTH, MOUSEBUTTONDOWN, QUIT
from checkers.piece import Piece


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('checkers')

def get_row_col_from(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    board = Board()
    run = True
    clock = pygame.time.Clock()

    # piece = board.get_piece(1, 0)
    # board.move(piece, 4, 3)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from(pos)
                board.move(board.get_piece(row, col), 4, 3)

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()