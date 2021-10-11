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

    def hasPiece(self, loc: Location) -> bool:
        return loc.to_key() in self.b_pieces

    def movePiece(self, loc_from: Location, loc_to: Location) -> None:
        if not self.hasPiece(loc_from):
            raise Exception('No piece at the location.')
        self.b_pieces[loc_to.to_key()] = self.b_pieces[loc_from.to_key()]
        self.b_pieces.pop(loc_from.to_key())

    def getPiece(self, loc: Location) -> Piece:
        if not self.hasPiece(loc):
            raise Exception('No Piece at this location')
        else:
            return self.b_pieces[loc.to_key()]