from piece import Piece, PieceType
from chess_utility import Location, LocationKey
default_size = 8


class Board:

    @staticmethod
    def default_pieces(size=8) -> dict[LocationKey, Piece]:
        pieces = {}
        for location_key in range(size * size):
            loc_key = LocationKey(location_key)
            if not (2 < loc_key.to_location(size)[0] < size - 1):
                default_piece = Piece.getDefaultPiece(loc_key.to_location(size), size)
                pieces[loc_key] = default_piece
        return pieces

    def __init__(self, size=default_size):
        self.b_size = size
        self.b_pieces = Board.default_pieces(self.b_size)
