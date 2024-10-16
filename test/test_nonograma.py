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
        self.assertEqual(self.test_board, self.game.sol_board)

    def test_set_player(self):

        self.game.set_player(self.test_board)
        self.assertEqual(self.test_board, self.game.player_board)

    def test_win_condition(self):
        self.game.player_board = self.game.sol_board
        self.assertEqual(self.game.win_condition(), True)

    def test_load_level(self):
        self.game.sol_board = self.test_board
        self.assertEqual(self.game.sol_board, self.game.load_level(self.test_board))


if __name__ == '__main__':
    unittest.main()
