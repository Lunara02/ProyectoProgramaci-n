import numpy as np
import os
from .num_matriz import GenNum
from INTERFAZ.resource_manager import ResourceManager
from LOGICA.shop import Shop


class Nonograma:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Nonograma, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.player_board = None
            self.sol_board = None
            self.sol_matriz = None
            self.Shop = Shop()
            self.completado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.load_completado()
            self.initialized = True

    def get_sol(self):
        return self.sol_board

    def get_player(self):
        return self.player_board

    def set_sol(self, m_sol):
        self.sol_board = m_sol

    def set_player(self, save):
        self.player_board = save

    def win_condition(self):
        mask = np.where(
            (self.player_board == 2) | (self.player_board == 5),
            0,
            np.where(self.player_board == 4, 1, self.player_board)
        )
        return np.array_equal(mask, self.sol_board)

    def set_box_value(self, i, j, mouse_action):
        self.player_board[i][j] = mouse_action

    def wipe(self):
        self.player_board = None

    def load_level(self, id_matriz, mode):
        if mode=='level':
            archivo_maestro = ResourceManager.level_path('index.txt')
        elif mode=='my_level':
            archivo_maestro = ResourceManager.level_path('index_my_levels.txt')

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
                self.player_board = self.load_player_board(id_matriz,mode)
                return

    def load_player_board(self, id_matriz, mode):
        if mode == 'level':
            archivo_maestro = ResourceManager.level_path('index_saves.txt')
        if mode == 'my_level':
            archivo_maestro = ResourceManager.level_path('index_my_saves.txt')
        with open(archivo_maestro, 'r') as f:
            lineas = f.readlines()
        carpeta_base = os.path.dirname(archivo_maestro)
        for linea in lineas:
            id_actual, archivo_save = linea.split()
            if int(id_actual) == id_matriz:
                ruta_archivo_save = os.path.join(carpeta_base, archivo_save)
                return np.loadtxt(ruta_archivo_save, dtype=int)

    def save_level(self, index, mode):
        if mode == 'level':
            archivo_maestro = ResourceManager.level_path('index_saves.txt')
        if mode == 'my_level':
            archivo_maestro = ResourceManager.level_path('index_my_saves.txt')
        with open(archivo_maestro, 'r') as f:
            lineas = f.readlines()
        carpeta_base = os.path.dirname(archivo_maestro)
        for linea in lineas:
            id_actual, archivo_save = linea.split()
            if int(id_actual) == index:
                ruta_archivo_save = os.path.join(carpeta_base, archivo_save)
                np.savetxt(ruta_archivo_save, self.player_board, fmt="%d")
                return

    def wipe_saved(self, index, mode):
        if mode == 'level':
            archivo_maestro = ResourceManager.level_path('index_saves.txt')
        if mode == 'my_level':
            archivo_maestro = ResourceManager.level_path('index_my_saves.txt')
        with open(archivo_maestro, 'r') as f:
            lineas = f.readlines()
        carpeta_base = os.path.dirname(archivo_maestro)
        for linea in lineas:
            id_actual, archivo_save = linea.split()
            if int(id_actual) == index:
                ruta_archivo_save = os.path.join(carpeta_base, archivo_save)
                np.savetxt(ruta_archivo_save, np.zeros(self.sol_board.shape, dtype=int), fmt="%d")
                return

    def set_completed(self, index, mode):
        if mode=='level':
            if self.completado[index - 1] == 0:
                self.completado[index - 1] = 1
                self.Shop.addMoney(500)
                self.save_completado()

    def load_completado(self):
        try:
            with open("player.txt", "r") as file:
                lines = file.readlines()
                self.completado = list(map(int, lines[0].strip().split(',')))
        except FileNotFoundError:
            pass

    def save_completado(self):
        try:
            with open("player.txt", "w") as file:
                file.write(','.join(map(str, self.completado)))
        except Exception as e:
            pass



