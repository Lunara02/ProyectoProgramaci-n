from LOGICA.nonograma import Nonograma
from block import Block
from button import Button
import pygame

class GameScreen():
    def __init__(self):
        self.game = None
        self.blocks = None
        self.cell_size = 50
        self.n = None