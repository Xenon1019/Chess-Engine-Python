import sys
import pygame
from chess_utility import Location, LocationKey
from board import Board
IMAGE_PATH = './Assets/piece_imgs_png/'
LIGHT_SQUARES = (255, 255, 255)
BOARD_BORDER_COLOR = (210, 210, 210)
DARK_SQUARES = (50, 50, 50)
TILE_SIZE = 80
BOARD_OFFSET = 40


class Tile:
    tile_size = (TILE_SIZE, TILE_SIZE)

    def __init__(self, loc: Location, board: Board, display: 'Display'):
        self.loc = loc
        self.color = LIGHT_SQUARES if loc.tile_color() else DARK_SQUARES
        board_offsets = display.board_offsets
        self.offsets = (board_offsets[0] + TILE_SIZE * (loc.col - 1), board_offsets[1] + TILE_SIZE * (loc.row - 1))
        self.bg_rect = pygame.Rect(self.offsets, (TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(display.window, self.color, self.bg_rect)
        self.if_changed = False
        if board.hasPiece(loc):
            piece_img_str = board.getPiece(loc).get_image_file_string()
            piece_img = pygame.image.load(IMAGE_PATH + piece_img_str)
            piece_img = pygame.transform.scale(piece_img, self.tile_size)
            display.window.blit(piece_img, self.offsets)

    def draw(self, board: Board, display: 'Display'):
        if self.changed:
            if not board.hasPiece(self.loc):
                pygame.draw.rect(display.window, self.color, self.bg_rect)
            else:
                pygame.draw.rect(display.window, self.color, self.bg_rect)
                piece_img_str = board.getPiece(self.loc).get_image_file_string()
                piece_img = pygame.image.load(IMAGE_PATH + piece_img_str)
                piece_img = pygame.transform.scale(piece_img, self.tile_size)
                piece_rect = display.window.blit(piece_img, self.offsets)

    def changed(self):
        self.if_changed = True

    def get_offsets(self):
        return self.offsets


class Display:
    def __init__(self, board: Board):
        board_width = board_height = board.b_size * TILE_SIZE
        self.board_size = (board_width, board_height)
        self.board_offsets = (BOARD_OFFSET // 2, BOARD_OFFSET // 2)
        window_size = (self.board_size[0] + BOARD_OFFSET, self.board_size[1] + BOARD_OFFSET)
        self.window = pygame.display.set_mode(window_size)
        self.board = pygame.Rect(self.board_offsets[0], self.board_offsets[1], self.board_size[0], self.board_size[1])
        pygame.draw.rect(self.window, BOARD_BORDER_COLOR, self.board)
        self.tiles = []

        for key in range(board.b_size**2):
            self.tiles.append(Tile(Location.key_to_location(key, board.b_size), board, self))

    def changed_at(self, locs: list[Location]):
        for loc in locs:
            self.tiles[loc.to_key()].changed()

    def update(self, board: Board):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for tile in self.tiles:
            tile.draw(board, self)
        pygame.display.flip()
