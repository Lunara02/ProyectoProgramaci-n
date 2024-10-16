import unittest
from LOGICA import num_matriz

class TestNumMatriz(unittest.TestCase):
    def test_get_num(self):
        self.assertEqual(self.genNum.get_num([0, 1, 1, 1, 0]), [3])
        self.assertEqual(self.genNum.get_num([1, 1, 1, 1, 1]), [5])
        self.assertEqual(self.genNum.get_num([1, 0, 1, 0, 1]), [1, 1, 1])
        self.assertEqual(self.genNum.get_num([0, 1, 1, 1, 0]), [3])
        self.assertEqual(self.genNum.get_num([0, 0, 1, 0, 0]), [1])