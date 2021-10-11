from chess_utility import Location
from board import Board
from display import Display
import pygame
board = Board()
display = Display(board)
command_tokens = ['move', 'exit']
args_required = [2, 0]
while True:
    display.update(board)
    inp = input('Enter a command : ').rstrip().split(' ')
    if inp[0] not in command_tokens:
        raise Exception('Invalid command entered')
    else:
        command_index = command_tokens.index(inp[0])
        args = inp[1:]
        if len(args) != args_required[command_index]:
            raise Exception('Invalid arguments')
        if command_index == 1:
            break
        elif command_index == 0:
            loc_from, loc_to = [Location.str_to_loc(loc) for loc in args]
            board.movePiece(loc_from, loc_to)