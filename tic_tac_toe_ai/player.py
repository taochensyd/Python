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


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:  # first move, random choice one of the 9 spots
            square = random.choice(game.available_moves())
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    # recursion function
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'o' if self.letter == 'x' else 'x'

        #Base Case
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_square() + 1) if other_player == max_player else -1*(state.num_empty_square() + 1)}

        elif not state.empty_square():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            #1. make a move, try that spot
            state.make_move(possible_move, player)

            # 2. resurse using minimax to simukate a gama after making that move
            sim_score = self.minimax(state, other_player)

            #3. undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move #otherwise this will get messed upp from the recursion part

            #4. update the dictionary if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score #replace the best with the new best
                else: # minimize the other player
                    if sim_score['score'] < best['score']:
                        best = sim_score # replace best

        return best