import numpy as np
import os
from .resource_manager import ResourceManager

class Nonograma:
    def __init__(self):
        self.player_board = None
        self.sol_board = None

    def get_sol(self):
        return self.sol_board

    def get_player(self):
        return self.player_board

    def set_sol(self, m_sol):
        self.sol_board = m_sol

    def set_player(self, save):
        self.player_board = save

    def win_condition(self):
        return np.array_equal(self.player_board, self.sol_board)

    def fill_box(self, i, j):
        self.player_board[i][j] = 1

    def empty_box(self, i, j):
        self.player_board[i][j] = 0

    def wipe(self):
        self.player_board = None

    def load_level(self, id_matriz):
        archivo_maestro = ResourceManager.level_path('index.txt')
        with open(archivo_maestro, 'r') as f:
            lineas = f.readlines()

        carpeta_base = os.path.dirname(archivo_maestro)
        for linea in lineas:
            id_actual, archivo_matriz = linea.split()
            if int(id_actual) == id_matriz:
                ruta_archivo_matriz = os.path.join(carpeta_base, archivo_matriz)
                self.sol_board = np.loadtxt(ruta_archivo_matriz, dtype=int)
                self.player_board = np.zeros(self.sol_board.shape, dtype=int)
                return

