LocationKey = int


class Location:
    @staticmethod
    def key_to_location(key: LocationKey, boardSize=8) -> 'Location':
        row = key // boardSize + 1
        col = key % boardSize + 1
        return Location(row, col)

    def __init__(self, row: int, col: int):
        self.row, self.col = row, col

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

    def reverse(self) -> 'Location':
        return Location(self.col, self.row)

    def print_coord(self):
        print(f'({self.col}, {self.row})')

    @staticmethod
    def str_to_loc(loc: str, board_size=8) -> 'Location':
        loc = loc.rstrip().lstrip()
        if not (loc.isalnum() and len(loc) == 2):
            raise Exception('Invalid location argument given')
        rank = int(loc[1])
        rank = board_size - rank + 1
        file = loc[0].lower()
        file = ord(file) - ord('a') + 1
        return Location(rank, file)

    @staticmethod
    def key_tile_color(loc: LocationKey) -> bool:
        return Location.key_to_location(loc).tile_color()
        #To improve so it doesn't create an anonymous object
