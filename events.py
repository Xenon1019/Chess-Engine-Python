from commands import Command
import sys
import pygame
from chess_utility import Location


class EventHandler:
    def __init__(self, display: 'Display'):
        self.display = display

    def handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click_loc = pygame.mouse.get_pos()
                for tile in self.display.tiles:
                    if tile.rect.collidepoint(mouse_click_loc):
                        if self.display.loc_highlighted is not None:
                            if tile.loc.to_key(self.display.board.b_size) == self.display.loc_highlighted:
                                tile.highlight_toggle()
                                self.display.loc_highlighted = None
                            else:
                                loc_from = Location.key_to_location(self.display.loc_highlighted, self.display.board.b_size)
                                loc_to = tile.loc
                                arg1 = loc_from.to_str(self.display.board.b_size)
                                arg2 = loc_to.to_str(self.display.board.b_size)
                                command_str = f'move {arg1} {arg2}'
                                changed_locs = Command.get_from_str(command_str).exec_command(self.display.board)

                                self.display.changed_at(changed_locs)

                                self.display.tiles[self.display.loc_highlighted].highlight_toggle()
                                self.display.loc_highlighted = tile.loc.to_key(self.display.board.b_size)
                                self.display.tiles[self.display.loc_highlighted].highlight_toggle()
                        else:
                            tile.highlight_toggle()
                            self.display.loc_highlighted = tile.loc.to_key(self.display.board.b_size)
            else:
                pygame.event.pump()
