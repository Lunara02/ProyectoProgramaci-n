import numpy as np
import os
from .num_matriz import GenNum
from .resource_manager import ResourceManager

class Nonograma:
    def __init__(self):
        self.player_board = None
        self.sol_board = None
        self.sol_matriz = None

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
                self.sol_matriz = GenNum(self.sol_board)
                self.sol_matriz.create_num()
                self.player_board = self.load_player_board(id_matriz)
                return

    def load_player_board(self, id_matriz):
        archivo_maestro = ResourceManager.level_path('index_saves.txt')
        with open(archivo_maestro, 'r') as f:
            lineas = f.readlines()
        carpeta_base = os.path.dirname(archivo_maestro)
        for linea in lineas:
            id_actual, archivo_save = linea.split()
            if int(id_actual) == id_matriz:
                ruta_archivo_save = os.path.join(carpeta_base, archivo_save)
                return np.loadtxt(ruta_archivo_save, dtype=int)

    def save_level(self, index):
        archivo_maestro = ResourceManager.level_path('index_saves.txt')
        with open(archivo_maestro, 'r') as f:
            lineas = f.readlines()
        carpeta_base = os.path.dirname(archivo_maestro)
        for linea in lineas:
            id_actual, archivo_save = linea.split()
            if int(id_actual) == index:
                ruta_archivo_save = os.path.join(carpeta_base, archivo_save)
                np.savetxt(ruta_archivo_save, self.player_board, fmt = "%d")
                return

    def wipe_saved(self, index):
        archivo_maestro = ResourceManager.level_path('index_saves.txt')
        with open(archivo_maestro, 'r') as f:
            lineas = f.readlines()
        carpeta_base = os.path.dirname(archivo_maestro)
        for linea in lineas:
            id_actual, archivo_save = linea.split()
            if int(id_actual) == index:
                ruta_archivo_save = os.path.join(carpeta_base, archivo_save)
                np.savetxt(ruta_archivo_save, np.zeros(self.sol_board.shape, dtype=int), fmt="%d")
                self.wipe()
                return