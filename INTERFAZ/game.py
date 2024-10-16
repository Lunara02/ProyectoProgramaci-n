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

    def def_level(self, index):
        self.blocks = []
        self.game = Nonograma()
        self.game.load_level(index)
        self.game.set_player_board()
        self.n = len(self.game.sol_board)
        blocks_size = int(500 / self.n)
        for i in range(len(self.game.sol_board)):
            for j in range(len(self.game.sol_board)):
                self.blocks.append(Block(640 + (blocks_size - 1) * j - int(blocks_size * self.n / 2 - 1 * (self.n - 1)), 360 + i * (blocks_size - 1) - int(blocks_size * self.n/2 - 1 * (self.n - 1)), int(500 / self.n)))

    def draw(self, surface):
        surface.fill((255, 255, 255))
        for i in range(self.n):
            for j in range(self.n):
                self.blocks[i * self.n + j].draw(surface)

        pygame.display.flip()