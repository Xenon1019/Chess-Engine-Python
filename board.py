from piece import Piece, PieceType
from chess_utility import Location, LocationKey

default_size = 8


class Board:

    @staticmethod
    def default_pieces(size=default_size) -> dict[LocationKey, Piece]:
        pieces = {}
        for loc_key in range(size * size):
            loc = Location.key_to_location(loc_key, size)
            if not (2 < loc.row < size - 1):
                default_piece = Piece.getDefaultPiece(loc, size)
                pieces[loc_key] = default_piece
        return pieces

    @staticmethod
    def standard_board() -> 'Board':
        return Board(Board.default_pieces(default_size), True, default_size)

    @staticmethod
    def from_fen_string(fen_string: str) -> 'Board':
        size = 8
        fen_string = fen_string.strip()
        fen_string_tokens = fen_string.split(' ')
        fen_string_tokens = [token for token in fen_string_tokens if token]
        if fen_string_tokens[1].lower() == 'w':
            white_move = True
        elif fen_string_tokens[1].lower() == 'b':
            white_move = False
        else:
            raise Exception('Invalid FEN String')

        board_pieces = {}
        fen_placement = fen_string_tokens[0].split('/')
        if not len(fen_placement) == size:
            raise Exception('Invalid FEN String')
        for row_index in range(len(fen_placement)):
            col_index = 0

            if not fen_placement[row_index].isalnum():
                raise Exception('Invalid FEN String')
            for fen_index in range(len(fen_placement[row_index])):
                ch = fen_placement[row_index][fen_index]
                if ch.isdigit():
                    col_index += int(ch)
                else:
                    if ch.lower() not in [p_type.value for p_type in PieceType]:
                        raise Exception('Invalid FEN String')
                    else:
                        p_color = ch.isupper()
                        for p_type in PieceType:
                            if p_type.value == ch.lower():
                                board_pieces[Location(row_index + 1, col_index + 1).to_key()] = Piece(p_type, p_color)
                                col_index += 1
            if col_index != 8:
                raise Exception('Invalid FEN String')
        return Board(board_pieces, white_move, size)

    def __init__(self, pieces :dict[LocationKey, Piece], white_to_move: bool, size=default_size):
        self.b_size = size
        self.b_pieces = pieces
        self.white_to_move = white_to_move

    def hasPiece(self, loc: Location) -> bool:
        return loc.to_key() in self.b_pieces

    def movePiece(self, loc_from: Location, loc_to: Location) -> None:
        if not self.hasPiece(loc_from):
            raise Exception('No piece at the location.')
        self.b_pieces[loc_to.to_key()] = self.b_pieces[loc_from.to_key()]
        self.b_pieces.pop(loc_from.to_key())

    def to_move_toggle(self):
        self.white_to_move = not self.white_to_move

    def getPiece(self, loc: Location) -> Piece:
        if not self.hasPiece(loc):
            raise Exception('No Piece at this location')
        else:
            return self.b_pieces[loc.to_key()]
