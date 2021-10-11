import sys
import pygame
from chess_utility import Location, LocationKey
from board import Board
LIGHT_SQUARES = (255, 255, 255)
BOARD_BORDER = (210, 210, 210)
DARK_SQUARES = (50, 50, 50)
TILE_SIZE = 80
BOARD_OFFSET = 40


class Display:
    def __init__(self, board: Board):
        board_width = board_height = board.b_size * TILE_SIZE
        self.board_size = (board_width, board_height)
        self.board_offsets = (BOARD_OFFSET // 2, BOARD_OFFSET // 2)
        window_size = (self.board_size[0] + BOARD_OFFSET, self.board_size[1] + BOARD_OFFSET)
        self.window = pygame.display.set_mode(window_size)
        self.board = pygame.Rect(self.board_offsets[0], self.board_offsets[1], self.board_size[0], self.board_size[1])
        pygame.draw.rect(self.window, BOARD_BORDER, self.board)

        for key in range(board.b_size**2):
            self.drawTile(Location(key))

    def drawTile(self, loc: Location):
        tile_offsets = (self.board_offsets[0] + TILE_SIZE * (loc.row - 1), self.board_offsets[1] + TILE_SIZE * (loc.col - 1))
        tile = pygame.Rect(tile_offsets[0], tile_offsets[1], TILE_SIZE, TILE_SIZE)
        tile_color = LIGHT_SQUARES if loc.tile_color() else DARK_SQUARES
        pygame.draw.rect(self.window, tile_color, tile)

    def update(self, board: Board):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
