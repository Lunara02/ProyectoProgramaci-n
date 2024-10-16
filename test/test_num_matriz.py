import unittest
from LOGICA.num_matriz import GenNum


class TestNumMatriz(unittest.TestCase):

    def test_get_num(self):
        self.genNum = GenNum([])
        self.assertEqual(self.genNum.get_num([0, 1, 1, 1, 0]), [3])
        self.assertEqual(self.genNum.get_num([1, 1, 1, 1, 1]), [5])
        self.assertEqual(self.genNum.get_num([1, 0, 1, 0, 1]), [1, 1, 1])
        self.assertEqual(self.genNum.get_num([0, 1, 1, 1, 0]), [3])
        self.assertEqual(self.genNum.get_num([0, 0, 1, 0, 0]), [1])

    def test_create_num(self):
        matriz = [
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0]
        ]
        self.genNum = GenNum(matriz)
        self.genNum.create_num()

        self.assertEqual(self.genNum.num_filas, [[3], [5], [1,1,1], [3], [1]])
        self.assertEqual(self.genNum.num_columnas, [[2], [2,1], [5], [2,1], [2]])