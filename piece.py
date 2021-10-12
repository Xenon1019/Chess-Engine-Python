from enum import Enum
from chess_utility import LocationKey, Location


class PieceType(Enum):
    KING = 'k'
    QUEEN = 'q'
    ROOK = 'r'
    BISHOP = 'b'
    KNIGHT = 'n'
    PAWN = 'p'


class Piece:
    default_types_by_column = (
        PieceType.ROOK, PieceType.KNIGHT, PieceType.BISHOP, PieceType.QUEEN, PieceType.KING, PieceType.BISHOP,
        PieceType.KNIGHT, PieceType.ROOK)

    @staticmethod
    def all_pieces() -> list['Piece']:
        pieces = []
        for piece_type in PieceType:
            for piece_color in [True, False]:
                pieces.append(Piece(piece_type, piece_color))
        return pieces

    @staticmethod
    def getDefaultPiece(loc: Location, b_size) -> 'Piece':
        if 2 < loc.row < b_size - 1:
            raise Exception('No Piece in this Location')
        else:
            piece_color = (loc.row == b_size - 1 or loc.row == b_size)
            if loc.row == 2 or loc.row == 7:
                piece_type = PieceType.PAWN
            else:
                piece_type = Piece.default_types_by_column[loc.col - 1]
            return Piece(piece_type, piece_color)

    def __init__(self, piece_type: PieceType, piece_color: bool):
        self.p_type = piece_type
        self.p_color = piece_color

    def get_letter(self) -> str:
        letter = self.p_type.value
        if self.p_color:
            letter.upper()
        return letter

    def get_image_file_string(self):
        letter = self.get_letter().upper() + '-' + ('W' if self.p_color else 'B') + '.png'
        return letter
