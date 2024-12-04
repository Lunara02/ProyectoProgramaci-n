import numpy as np
import os
from INTERFAZ.resource_manager import ResourceManager
from LOGICA.nonograma import Nonograma


def num_levels():
    archivo_maestro = ResourceManager.level_path('index_my_levels.txt')
    with open(archivo_maestro, 'r') as f:
        return sum(1 for _ in f)



class NonogramaCreator():
    def __init__(self, n):
        self.n = n
        self.num=None
        self.player_board = np.zeros((self.n, self.n), dtype=int)

    def set_box_value(self, i, j, mouse_action):
        self.player_board[i][j] = mouse_action

    def save_new_level(self):
        if np.array_equal(self.player_board, np.zeros((self.n, self.n), dtype=int)):
            return False
        self.num = num_levels()+1
        archivo_maestro = ResourceManager.level_path('index_my_levels.txt')
        print(archivo_maestro)
        nombre_archivo = f'my_level_{self.num}.txt'

        with open(archivo_maestro, 'a') as f:
            f.write(f"{self.num} {nombre_archivo}\n")
        nuevo_nivel = ResourceManager.level_path(f'my_level_{self.num}.txt')
        np.savetxt(nuevo_nivel, self.player_board, fmt = "%d")
        archivo_maestro2=ResourceManager.level_path('index_my_saves.txt')
        nombre_save = f'my_save_{self.num}.txt'
        with open(archivo_maestro2, 'a') as f:
            f.write(f"{self.num} {nombre_save}\n")

        nuevo_save = ResourceManager.level_path(f'my_save_{self.num}.txt')
        np.savetxt(nuevo_save, np.zeros(self.player_board.shape, dtype=int), fmt="%d")
        return True


