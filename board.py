HUMAN = 1
COMPUTER = 2


class Board(object):
    whos_turn = HUMAN
    board = []

    def __init__(self):
        pass

    def is_clear(self):
        """
        Returns True if all coords are clear.
        """
        pass

    def can_put(self, x, y):
        pass

    def put(self, x, y, player):
        pass

    def owner_of(self, x, y):
        pass

    def player_starts(self, player):
        pass

    def player_turn(self):
        pass

    def is_winner(self):
        pass

    def get_winner(self):
        pass

    def evaluate_move(self, x, y, player):
        """
        Returns 1 if player with movement to this (x, y) position
        wins the game, 0 if nothing will happen with this movement,
        -1 if player will lose the game putting here.
        """
        pass

    def valid_moves(self, x, y):
        """
        Returns list of all available x and y coords.
        """
        pass

    def get_best_move(self, player=None):
        """
        Returns the best movement coords. If `player` is None, then
        `whos_turn` player will be simulated.
        """
        pass
