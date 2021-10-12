from board import Board
from display import Display
from commands import Command

fen_string = '2kr3r/ppp2p1p/6p1/1BPb4/1n3P2/2N1BnP1/P4NKq/Q4R2 w - - 0 3'
board = Board.from_fen_string(fen_string)

display = Display(board)
while True:
    display.update(board)
