from chess_utility import Location
from board import Board
from display import Display
from commands import Command

board = Board()

display = Display(board)
while True:
    display.update(board)
    Command.get_from_user()