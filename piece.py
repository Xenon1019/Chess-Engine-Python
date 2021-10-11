from enum import Enum
from chess_utility import LocationKey, Location


class PieceType(Enum):
    KING = 1
    QUEEN = 2
    ROOK = 3
    BISHOP = 4
    KNIGHT = 5
    PAWN = 6


class Piece:
    @staticmethod
    def getDefaultPiece(loc: Location, b_size) -> 'Piece':
        if 2 < loc.row < b_size - 1:
            raise Exception('No Piece in this Location')
        else:
            piece_color = (loc.row == b_size - 1 or loc.row == b_size)
            if loc.row == 2 or loc.row == 7:
                piece_type = PieceType.PAWN
            else:
                p_types = (PieceType.ROOK, PieceType.KNIGHT, PieceType.BISHOP, PieceType.QUEEN, PieceType.KING, PieceType.BISHOP, PieceType.KNIGHT, PieceType.ROOK)
                piece_type = p_types[loc.col - 1]
            return Piece(piece_type, piece_color)

    def __init__(self, piece_type: PieceType, piece_color: bool):
        self.p_type = piece_type
        self.p_color = piece_color