from copy import deepcopy
from unittest import TestCase, main
from board import Board, HUMAN, COMPUTER, EMPTY


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board()

    def test_clear_board_on_start(self):
        self.assertTrue(self.board.is_clear())

    def test_clear_board(self):
        self.assertTrue(self.board.is_clear())
        self.board.put(0, 0, HUMAN)
        self.assertFalse(self.board.is_clear())
        self.board.clear()
        self.assertTrue(self.board.is_clear())

    def test_full_board(self):
        self.assertFalse(self.board.is_full())
        self.board.put(1, 1, HUMAN)
        self.assertFalse(self.board.is_full())
        self.board.board = [[COMPUTER, COMPUTER, COMPUTER],
                            [COMPUTER, HUMAN, COMPUTER],
                            [COMPUTER, COMPUTER, COMPUTER]]
        self.assertTrue(self.board.is_full())

    def test_can_put_on_board(self):
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

    def test_game_winner(self):
        self.board.board = [[HUMAN, EMPTY, EMPTY],
                            [EMPTY, HUMAN, EMPTY],
                            [EMPTY, EMPTY, HUMAN]]
        self.assertEqual(HUMAN, self.board.get_winner())

        self.board.board = [[HUMAN, EMPTY, COMPUTER],
                            [HUMAN, HUMAN, HUMAN],
                            [COMPUTER, COMPUTER, EMPTY]]
        self.assertEqual(HUMAN, self.board.get_winner())

        self.board.board = [[COMPUTER, HUMAN, COMPUTER],
                            [COMPUTER, HUMAN, COMPUTER],
                            [HUMAN, COMPUTER, HUMAN]]
        self.assertEqual(EMPTY, self.board.get_winner())

        self.board.board = [[EMPTY, HUMAN, COMPUTER],
                            [COMPUTER, HUMAN, COMPUTER],
                            [EMPTY, COMPUTER, HUMAN]]
        self.assertEqual(None, self.board.get_winner())

        self.board.board = [[EMPTY, HUMAN, COMPUTER],
                            [HUMAN, COMPUTER, HUMAN],
                            [COMPUTER, COMPUTER, HUMAN]]
        self.assertEqual(COMPUTER, self.board.get_winner())

        self.board.board = [[EMPTY, HUMAN, HUMAN],
                            [HUMAN, COMPUTER, HUMAN],
                            [COMPUTER, COMPUTER, COMPUTER]]
        self.assertEqual(COMPUTER, self.board.get_winner())

        self.board.board = [[EMPTY, HUMAN, HUMAN],
                            [HUMAN, COMPUTER, HUMAN],
                            [COMPUTER, COMPUTER, COMPUTER]]
        self.assertEqual(COMPUTER, self.board.get_winner())

        self.board.board = [[HUMAN, COMPUTER, HUMAN],
                            [HUMAN, COMPUTER, HUMAN],
                            [HUMAN, HUMAN, COMPUTER]]
        self.assertEqual(HUMAN, self.board.get_winner())

        self.board.board = [[HUMAN, COMPUTER, HUMAN],
                            [COMPUTER, COMPUTER, HUMAN],
                            [HUMAN, EMPTY, HUMAN]]
        self.assertEqual(HUMAN, self.board.get_winner())

    def test_evaluate_move(self):
        board = [[EMPTY, EMPTY, EMPTY],
                 [COMPUTER, HUMAN, EMPTY],
                 [COMPUTER, EMPTY, HUMAN]]
        self.board.board = deepcopy(board)
        self.assertEqual(1, self.board.evaluate_move(0, 0, HUMAN))
        self.assertEqual(1, self.board.evaluate_move(0, 0, COMPUTER))
        self.assertEqual(board, self.board.board)
        self.assertEqual(0, self.board.evaluate_move(0, 1, HUMAN))
        self.assertEqual(board, self.board.board)

    def test_valid_moves(self):
        board = [[EMPTY, EMPTY, HUMAN],
                 [COMPUTER, HUMAN, HUMAN],
                 [COMPUTER, COMPUTER, HUMAN]]
        self.board.board = board
        valid = [[0, 0], [0, 1]]
        self.assertEqual(valid, self.board.get_valid_moves())

    def test_best_move(self):
        board = [[EMPTY, EMPTY, EMPTY],
                 [COMPUTER, HUMAN, EMPTY],
                 [COMPUTER, EMPTY, HUMAN]]
        self.board.board = deepcopy(board)
        self.board.player_starts(HUMAN)
        self.assertEqual([0, 0], self.board.get_best_move(HUMAN))
        self.assertEqual(board, self.board.board)
        self.assertEqual(HUMAN, self.board.player_turn())

        self.board.board = deepcopy(board)
        self.board.player_starts(COMPUTER)
        self.assertEqual([0, 0], self.board.get_best_move(COMPUTER))
        self.assertEqual(board, self.board.board)
        self.assertEqual(COMPUTER, self.board.player_turn())

        board = [[EMPTY, EMPTY, HUMAN],
                 [COMPUTER, HUMAN, EMPTY],
                 [EMPTY, COMPUTER, EMPTY]]
        self.board.board = deepcopy(board)
        self.board.player_starts(COMPUTER)
        self.assertEqual([2, 0], self.board.get_best_move(COMPUTER))
        self.assertEqual(board, self.board.board)
        self.assertEqual(COMPUTER, self.board.player_turn())


if __name__ == '__main__':
    main()
