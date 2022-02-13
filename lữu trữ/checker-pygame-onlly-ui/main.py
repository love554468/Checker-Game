import pygame
from pygame.constants import MOUSEBUTTONDOWN, QUIT
from checkers.board import Board
from checkers.constants import HEIGHT, WIDTH


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('checkers')

def main():
    board = Board()
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw(WIN)
        pygame.display.update()
    pygame.quit()

main()