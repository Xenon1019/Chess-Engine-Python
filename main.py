from board import Board
from display import Display
import pygame
board = Board()
display = Display(board)
while True:
    display.update(board)
