import pygame
from chess_utility import Location
from board import Board
import events as ev

IMAGE_PATH = './Assets/piece_imgs_png/'
LIGHT_SQUARES = ((200, 255, 200), (255, 215, 0))
DARK_SQUARES = ((50, 150, 50), (255, 223, 0))
BOARD_BORDER_COLOR = (210, 210, 210)

TILE_SIZE = 80
BOARD_OFFSET = 40


class Tile:
    tile_size = (TILE_SIZE, TILE_SIZE)

    def __init__(self, loc: Location, display: 'Display'):
        self.loc = loc
        self.color = LIGHT_SQUARES if loc.tile_color() else DARK_SQUARES
        board_offsets = display.board_offsets
        self.offsets = (board_offsets[0] + TILE_SIZE * (loc.col - 1), board_offsets[1] + TILE_SIZE * (loc.row - 1))
        self.rect = pygame.Rect(self.offsets, (TILE_SIZE, TILE_SIZE))
        self.changed = True
        self.highlighted = False
        self.draw(display)

    def draw(self, display: 'Display'):
        if self.changed:
            color_flag = 1 if self.highlighted else 0
            if not display.board.hasPiece(self.loc):
                pygame.draw.rect(display.window, self.color[color_flag], self.rect)
            else:
                pygame.draw.rect(display.window, self.color[color_flag], self.rect)
                piece_img_str = display.board.getPiece(self.loc).get_image_file_string()
                piece_img = pygame.image.load(IMAGE_PATH + piece_img_str)
                piece_img = pygame.transform.scale(piece_img, self.tile_size)
                display.window.blit(piece_img, self.offsets)
            self.changed = False

    def has_changed(self):
        self.changed = True

    def highlight_toggle(self):

        self.highlighted = not self.highlighted
        self.changed = True
        return True if self.highlighted else False

    def get_offsets(self):
        return self.offsets


class Display:
    def __init__(self, board: Board):
        board_width = board_height = board.b_size * TILE_SIZE
        self.board_size = (board_width, board_height)
        self.board_offsets = (BOARD_OFFSET // 2, BOARD_OFFSET // 2)
        window_size = (self.board_size[0] + BOARD_OFFSET, self.board_size[1] + BOARD_OFFSET)
        self.window = pygame.display.set_mode(window_size)
        self.board = board
        self.board_rect = pygame.Rect(self.board_offsets[0], self.board_offsets[1], self.board_size[0], self.board_size[1])
        # pygame.draw.rect(self.window, BOARD_BORDER_COLOR, self.board)
        self.tiles = []
        self.loc_highlighted = None
        self.handler = ev.EventHandler(self)

        for key in range(board.b_size ** 2):
            self.tiles.append(Tile(Location.key_to_location(key, board.b_size), self))

    def redraw(self):
        for tile in self.tiles:
            tile.draw(self)

    def changed_at(self, locs: list[Location]):
        for loc in locs:
            self.tiles[loc.to_key()].has_changed()

    def handle(self):
        if self.handler is None:
            raise Exception('Board does not have a event handler.')
        else:
            self.handler.handle()

    def highlight_at(self, loc: Location):
        self.tiles[loc.to_key()].highlight_toggle()

    def update(self):
        self.handle()
        for tile in self.tiles:
            tile.draw(self)
        pygame.display.flip()
