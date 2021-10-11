Location = tuple[int, int]


class LocationKey:
    @staticmethod
    def to_key(location: Location, boardSize=8) -> 'LocationKey':
        loc = (location[0] - 1) * boardSize + location[1] - 1
        return LocationKey(loc)

    @staticmethod
    def inBoard(location: Location, boardSize=8) -> bool:
        if location[0] > boardSize or location[1] > boardSize:
            return False
        if location[0] < 1 or location[1] < 1:
            return False
        return True

    @staticmethod
    def tile_color(loc: Location) -> bool:
        return loc[0] + loc[1] % 2 == 0

    def tile_color(self, board_size=8):
        return LocationKey.tile_color(self.to_location(board_size))

    def __init__(self, key_location: int):
        self.l_key = key_location

    def to_location(self, boardSize=8) -> Location:
        row = self.l_key // boardSize + 1
        column = self.l_key % boardSize + 1
        return row, column
