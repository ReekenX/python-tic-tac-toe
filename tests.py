from unittest import TestCase, main
from board import Board, HUMAN, COMPUTER, EMPTY


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board()
        pass

    def test_board(self):
        self.assertTrue(self.board.is_clear())
        board = [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]
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

        self.assertEqual(HUMAN, self.board.owner_of(0, 0))

    def test_next_player(self):
        self.board.player_starts(COMPUTER)
        self.assertEqual(HUMAN, self.board.next_player())
        self.assertEqual(COMPUTER, self.board.next_player())
        self.assertEqual(HUMAN, self.board.next_player())

    def test_walk(self):
        self.board.player_starts(COMPUTER)
        self.board.player_starts(HUMAN)
        self.assertEqual(HUMAN, self.board.player_turn())
        self.assertTrue(self.board.put(0, 0, HUMAN))
        self.assertEqual(COMPUTER, self.board.player_turn())

    def test_winner(self):
        board = [[HUMAN, EMPTY, EMPTY],
                 [EMPTY, HUMAN, EMPTY],
                 [EMPTY, EMPTY, HUMAN]]
        self.assertTrue(self.board.is_winner())
        self.assertEqual(HUMAN, self.board.get_winner())

        board = [[EMPTY, HUMAN, EMPTY],
                 [EMPTY, HUMAN, EMPTY],
                 [EMPTY, COMPUTER, HUMAN]]
        self.assertFalse(self.board.is_winner())
        self.assertEqual(None, self.board.get_winner())

        board = [[EMPTY, HUMAN, COMPUTER],
                 [HUMAN, COMPUTER, HUMAN],
                 [COMPUTER, COMPUTER, HUMAN]]
        self.assertTrue(self.board.is_winner())
        self.assertEqual(COMPUTER, self.board.get_winner())

    def test_evaluate_move(self):
        board = [[EMPTY, EMPTY, EMPTY],
                 [COMPUTER, HUMAN, EMPTY],
                 [COMPUTER, EMPTY, HUMAN]]
        self.board.board = board
        self.assertEqual(1, self.board.evaluate_move(0, 0, HUMAN))
        self.assertEqual(-1, self.board.evaluate_move(0, 1, HUMAN))

    def test_valid_moves(self):
        board = [[EMPTY, EMPTY, HUMAN],
                 [COMPUTER, HUMAN, HUMAN],
                 [COMPUTER, COMPUTER, HUMAN]]
        self.board.board = board
        valid = [[0, 0], [0, 1]]
        self.assertEqual(valid, self.board.valid_moves())

    def test_best_move(self):
        board = [[EMPTY, EMPTY, EMPTY],
                 [COMPUTER, HUMAN, EMPTY],
                 [COMPUTER, EMPTY, HUMAN]]
        self.board.board = board
        self.assertEqual([0, 0], self.board.get_best_move(HUMAN))
        self.assertEqual([0, 0], self.board.get_best_move(COMPUTER))


if __name__ == '__main__':
    main()
