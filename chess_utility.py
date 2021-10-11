LocationKey = int


class Location:
    def __init__(self, key: LocationKey, boardSize=8):
        self.row = key // boardSize + 1
        self.col = key % boardSize + 1

    def to_key(self, boardSize=8) -> 'LocationKey':
        loc = (self.row - 1) * boardSize + self.col - 1
        return loc

    def inBoard(self, boardSize=8) -> bool:
        if self.row > boardSize or self.col > boardSize:
            return False
        if self.row < 1 or self.col < 1:
            return False
        return True

    def tile_color(self) -> bool:
        return (self.row + self.col) % 2 == 0

    @staticmethod
    def key_tile_color(loc: LocationKey) -> bool:
        return Location(loc).tile_color()
