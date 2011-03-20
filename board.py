EMPTY = 0
HUMAN = 1
COMPUTER = 2


class Board(object):
    whos_turn = HUMAN
    board = []
    max_width = 3
    max_height = 3

    def __init__(self):
        self.clear()

    def clear(self):
        self.board = [[EMPTY] * 3] * 3

    def is_clear(self):
        """
        Returns True if all coords are clear.
        """
        for x in range(self.max_width):
            for y in range(self.max_height):
                if self.board[x][y] != EMPTY:
                    return False
        return True

    def can_put(self, x, y):
        return self.board[x][y] == EMPTY

    def put(self, x, y, player):
        if self.can_put(x, y):
            self.board[x][y] = player
            self.next_player()
            return True
        return False

    def next_player(self):
        if self.whos_turn == HUMAN:
            self.whos_turn = COMPUTER
        else:
            self.whos_turn = HUMAN
        return self.whos_turn

    def owner_of(self, x, y):
        """
        Returns who's reserved coordinate in board.
        """
        return self.board[x][y]

    def player_starts(self, player):
        """
        Set's player who's turn is now.
        """
        if player != self.player_turn():
            self.whos_turn = player

    def player_turn(self):
        """
        Returns player who's turn is now.
        """
        return self.whos_turn

    def get_winner(self):
        """
        Returns None if board has no winner yet or returns HUMAN or COMPUTER
        if winner exists.
        """
        for x in range(self.max_width):
            if self.board[x][0] == self.board[x][1] == self.board[x][2]:
                return self.board[x][0]

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None

    def evaluate_move(self, x, y, player):
        """
        Returns 1 if player with movement to this (x, y) position
        wins the game, 0 if nothing will happen with this movement,
        -1 if player will lose the game putting here.
        """
        pass

    def valid_moves(self):
        """
        Returns list of all available x and y coords.
        """
        valid_moves = []
        for x in range(self.max_width):
            for y in range(self.max_height):
                if self.board[x][y] == EMPTY:
                    valid_moves.append([x, y])
        return valid_moves

    def get_best_move(self, player=None):
        """
        Returns the best movement coords. If `player` is None, then
        `whos_turn` player will be simulated.
        """
        pass
