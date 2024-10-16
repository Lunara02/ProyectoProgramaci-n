import unittest
import numpy as np
from ProyectoProgramacion.LOGICA.nonograma import Nonograma


class TestNon(unittest.TestCase):

    def setUp(self):
        self.game = Nonograma(5)
        self.test_board = np.array([
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1]
        ])

    def test_get_sol(self):
        self.assertTrue(np.array_equal(self.game.get_sol(), self.game.sol_board))

    def test_get_player(self):
        self.assertTrue(np.array_equal(self.game.get_player(), self.game.player_board))

    def test_set_sol(self):
        self.game.set_sol(self.test_board)
        self.assertTrue(np.array_equal(self.test_board, self.game.sol_board))

    def test_set_player(self):
        self.game.set_player(self.test_board)
        self.assertTrue(np.array_equal(self.test_board, self.game.player_board))

    def test_win_condition(self):
        self.game.player_board = self.game.sol_board
        self.assertEqual(self.game.win_condition(), True)

    def test_fill_box(self):
        self.game.fill_box(1, 1)
        self.assertEqual(self.game.player_board[1][1], 1)

    def test_empty_box(self):
        self.game.empty_box(0, 0)
        self.assertEqual(self.game.player_board[0][0], 0)

    def test_load_level(self):
        self.assertEqual(self.game.load_level(1), self.game.sol_board)


if __name__ == '__main__':
    unittest.main()
