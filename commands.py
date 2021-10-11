from chess_utility import Location
from board import Board
from piece import PieceType, Piece


class Command:
    commands_numArgs = {'move': 2, 'exit': 0, 'show': 1}

    @staticmethod
    def get_from_str(full_command: str) -> 'Command':
        tokens = full_command.strip().split(' ')
        tokens = [token for token in tokens if (not token.isspace() and token)]
        print(tokens)
        for token in tokens:
            if not token.isalnum():
                raise Exception('Invalid command. Command must be alphanumeric.')
        if tokens[0] not in Command.commands_numArgs:
            raise Exception('Invalid command entered')
        else:
            command_token = tokens[0]
            args = tokens[1:]
            if len(args) != Command.commands_numArgs[command_token]:
                raise Exception('Invalid arguments')
            return Command(command_token, args)

    @staticmethod
    def get_from_user() -> 'Command':
        inp = input('Enter a command : ').strip()
        return Command.get_from_str(inp)

    def __init__(self, command_token: str, args: list[str]):
        self.token = command_token
        self.args = args

    def exec_command(self, board: Board):
        pass
