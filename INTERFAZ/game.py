from LOGICA.nonograma import Nonograma
from block import Block
from button import Button
import Color
import pygame

class GameScreen():
    def __init__(self):
        self.game = None
        self.blocks = None
        self.cell_size = 50
        self.n = None
        self.num_filas = None
        self.num_columnas = None
        self.blocks_size = None
        self.index = None

    def def_level(self, index):
        self.blocks = []
        self.game = Nonograma()
        self.index = index
        self.game.load_level(self.index)
        self.num_filas = self.game.sol_matriz.num_filas
        self.num_columnas = self.game.sol_matriz.num_columnas
        self.n = len(self.game.sol_board)
        self.blocks_size = int(500 / self.n)
        for i in range(len(self.game.sol_board)):
            for j in range(len(self.game.sol_board)):
                self.blocks.append(Block(640 + (self.blocks_size - 1) * j - int(self.blocks_size * self.n / 2 - 1 * (self.n - 1)), 360 + i * (self.blocks_size - 1) - int(self.blocks_size * self.n/2 - 1 * (self.n - 1)), int(500 / self.n)))
                if self.game.player_board[i][j]==1:
                    self.blocks[i * self.n + j].state=1

    def draw(self, surface):
        surface.fill((255, 255, 255))
        for i in range(self.n):
            for j in range(self.n):
                self.blocks[i * self.n + j].draw(surface)

        font = pygame.font.Font(None, 36)

        for filas in range(len(self.num_filas)):
            for u in range(len(self.num_filas[filas])):
                text_surface = font.render(str((self.num_filas[filas][::-1])[u]), True, Color.NEGRO)
                text_rect = text_surface.get_rect()
                text_rect.center = (u*-25+80,filas*56+130)
                surface.blit(text_surface, text_rect)

        for columnas in range(len(self.num_columnas)):
            for v in range(len(self.num_columnas[columnas])):
                text_surface = font.render(str((self.num_columnas[columnas][::-1])[v]), True, Color.NEGRO)
                text_rect = text_surface.get_rect()
                text_rect.center = (columnas*self.blocks_size+130,v*-25+80)
                surface.blit(text_surface, text_rect)

        pygame.display.flip()

    def handle_events(self, events):
        for i in range(self.n):
            for j in range(self.n):
                if self.blocks[i * self.n + j].handle_event(events) == 1:
                    self.game.fill_box(i, j)
                if self.blocks[i * self.n + j].handle_event(events) == 0:
                    self.game.empty_box(i, j)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.game.save_level(self.index)
                if event.key == pygame.K_d:
                    self.game.wipe_saved(self.index)


        if self.game.win_condition():
            self.blocks = None
            self.game.wipe()
            return 'levels'