from piece import Piece, PieceType
from chess_utility import Location, LocationKey
default_size = 8


class Board:

    @staticmethod
    def default_pieces(size=default_size) -> dict[LocationKey, Piece]:
        pieces = {}
        for loc_key in range(size * size):
            loc = Location(loc_key, size)
            if not (2 < loc.row < size - 1):
                default_piece = Piece.getDefaultPiece(loc, size)
                pieces[loc_key] = default_piece
        return pieces

    def __init__(self, size=default_size):
        self.b_size = size
        self.b_pieces = Board.default_pieces(self.b_size)
