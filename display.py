import sys
import pygame
from chess_utility import Location, LocationKey
from board import Board
LIGHT_SQUARES = (255, 255, 255)
BOARD_BORDER = (210, 210, 210)
DARK_SQUARES = (0, 0, 0)
TILE_SIZE = 80
BOARD_OFFSET = 40


class Display:
    def __init__(self, board: Board):
        board_width = board_height = board.b_size * TILE_SIZE
        self.board_size = (board_width, board_height)
        self.board_offset = BOARD_OFFSET
        window_size = (self.board_size[0] + self.board_offset, self.board_size[1] + self.board_offset)
        self.window = pygame.display.set_mode(window_size)
        self.board = pygame.Rect(self.board_offset//2, self.board_offset//2, self.board_size[0], self.board_size[1])
        pygame.draw.rect(self.window, BOARD_BORDER, self.board, 2)

    def update(self, board: Board):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
