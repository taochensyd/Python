import math
import random

from pandas import value_counts


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # all players get their next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for next move
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8)')
            try:
                val = int(square)
                if val in game.available_moves():
                    raise ValueError
            except ValueError:
                print('Invalid move. Try again.')

        return val
