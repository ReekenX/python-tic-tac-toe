from unittest import TestCase, main
from board import Board, HUMAN, COMPUTER


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board()
        pass

    def test_board(self):
        self.assertTrue(self.board.is_clear())
        board = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
        self.assertEqual(board, self.board.board)

    def test_clear(self):
        self.assertTrue(self.board.is_clear())
        self.board.put(0, 0, HUMAN)
        self.assertFalse(self.board.is_clear())
        self.board.clear()
        self.assertTrue(self.board.is_clear())

    def test_put(self):
        self.assertTrue(self.board.can_put(0, 0))
        self.assertTrue(self.board.put(0, 0, HUMAN))

        self.assertFalse(self.board.can_put(0, 0))
        self.assertTrue(self.board.can_put(0, 1))
        self.assertTrue(self.board.can_put(1, 1))
        self.assertFalse(self.board.put(0, 0, HUMAN))

        self.assertEqual(PLAYER, self.board.owner_of(0, 0))

    def test_walk(self):
        self.board.player_starts(COMPUTER)
        self.board.player_starts(HUMAN)
        self.assertEqual(HUMAN, self.board.player_turn())
        self.assertTrue(self.board.put(0, 0, HUMAN))
        self.assertEqual(COMPUTER, self.board.player_turn())

    def test_winner(self):
        board = [[HUMAN, 0, 0],
                 [0, HUMAN, 0],
                 [0, 0, HUMAN]]
        self.assertTrue(self.board.is_winner())
        self.assertEqual(HUMAN, self.board.get_winner())

        board = [[0, HUMAN, 0],
                 [0, HUMAN, 0],
                 [0, COMPUTER, HUMAN]]
        self.assertFalse(self.board.is_winner())
        self.assertEqual(None, self.board.get_winner())

        board = [[0, HUMAN, COMPUTER],
                 [HUMAN, COMPUTER, HUMAN],
                 [COMPUTER, COMPUTER, HUMAN]]
        self.assertTrue(self.board.is_winner())
        self.assertEqual(COMPUTER, self.board.get_winner())

    def test_evaluate_move(self):
        board = [[0, 0, 0],
                 [COMPUTER, HUMAN, 0],
                 [COMPUTER, 0, HUMAN]]
        self.board.board = board
        self.assertEqual(1, self.board.evaluate_move(0, 0, HUMAN))
        self.assertEqual(-1, self.board.evaluate_move(0, 1, HUMAN))

    def test_valid_moves(self):
        board = [[0, 0, 0],
                 [COMPUTER, HUMAN, 0],
                 [COMPUTER, 0, HUMAN]]
        self.board.board = board
        valid = [[0, 0], [0, 1]]
        self.assertEqual(valid, self.board.valid_moves())

    def test_best_move(self):
        pass


if __name__ == '__main__':
    main()
