from Xlib.Xcursorfont import mouse

from INTERFAZ.resource_manager import ResourceManager
from LOGICA.nonograma import Nonograma
from block import Block
from button import Button
import Color
import input_event
import pygame
from  pause_menu import PauseMenu

class GameScreen():
    def __init__(self):
        self.nonograma = Nonograma()
        self.blocks = None
        self.n = None
        self.num_filas = None
        self.num_columnas = None
        self.blocks_size = None
        self.mouse_action = 0
        self.index = None
        self.pause_menu = PauseMenu(500, 170, self.nonograma)

    def def_level(self, index):
        self.blocks = []
        self.index = index
        self.nonograma.load_level(index)
        self.num_filas = self.nonograma.sol_matriz.num_filas
        self.num_columnas = self.nonograma.sol_matriz.num_columnas
        self.n = len(self.nonograma.sol_board)
        self.blocks_size = int(500 / self.n)
        for i in range(len(self.nonograma.sol_board)):
            for j in range(len(self.nonograma.sol_board)):
                self.blocks.append(Block(640 + (self.blocks_size - 1) * j - int(self.blocks_size * self.n / 2 - 1 * (self.n - 1)), 360 + i * (self.blocks_size - 1) - int(self.blocks_size * self.n/2 - 1 * (self.n - 1)), int(500 / self.n)))
                self.blocks[i * self.n + j].state = self.nonograma.player_board[i][j]
        print(self.num_filas)

    def draw(self, surface):
        surface.fill((255, 255, 255))
        xprop = surface.get_size()[0] / 1280
        yprop = surface.get_size()[1] / 720
        if xprop > yprop:
            font = pygame.font.Font(None, int(self.blocks_size * yprop - 7))
        else:
            font = pygame.font.Font(None, int(self.blocks_size * xprop - 7))

        dimensions = pygame.font.Font(None, 50)
        dim = dimensions.render(str(self.n) + ' x ' + str(self.n), True, Color.NEGRO)
        surface.blit(dim, (200, 50))

        for i in range(self.n):
            for fila in range(len(self.num_filas[i])):
                text_surface = font.render(str((self.num_filas[i][::-1][fila])), True, Color.NEGRO)
                surface.blit(text_surface, (int((600 - 25 * fila - int(self.blocks_size * self.n / 2 - 1 * (self.n - 1))) * xprop), int(374 + i * (self.blocks_size - 1) - int(self.blocks_size * self.n/2 - 1 * (self.n - 1))) * yprop))
            for j in range(self.n):
                for col in range(len(self.num_columnas[j])):
                    text_surface = font.render(str(self.num_columnas[j][::-1][col]), True, Color.NEGRO)
                    surface.blit(text_surface, (int((654 + (self.blocks_size - 1) * j - int(self.blocks_size * self.n / 2 - 1 * (self.n - 1))) * xprop), int(330 - 20 * col - int(self.blocks_size * self.n/2 - 1 * (self.n - 1))) * yprop))
                self.blocks[i * self.n + j].draw(surface)

        if self.pause_menu.state == 1:
            self.pause_menu.draw(surface)

        pygame.display.flip()

    def handle_events(self, events):
        if input_event.esc_press(events):
            self.pause_menu.set_state()

        if self.pause_menu.state == 0:
            for i in range(self.n):
                for j in range(self.n):
                    if input_event.left_click(events) and self.blocks[i * self.n + j].collide():
                        if self.nonograma.player_board[i][j] == 1:
                            self.mouse_action = 0
                        else:
                            self.mouse_action = 1
                    if input_event.right_click(events) and self.blocks[i * self.n + j].collide():
                        if self.nonograma.player_board[i][j] == 2:
                            self.mouse_action = 0
                        else:
                            self.mouse_action = 2
                    if input_event.left_hold() and self.blocks[i * self.n + j].collide():
                        self.nonograma.set_box_value(i, j, self.mouse_action)
                        self.blocks[i * self.n + j].state_change(self.nonograma.player_board[i][j])
                    if input_event.right_hold() and self.blocks[i * self.n + j].collide():
                        self.nonograma.set_box_value(i, j, self.mouse_action)
                        self.blocks[i * self.n + j].state_change(self.nonograma.player_board[i][j])
        else:
            result = self.pause_menu.handle_events(events, self.index)
            if result:
                self.pause_menu.state = 0
                return result

        if self.nonograma.win_condition():
            self.blocks = None
            self.nonograma.wipe()
            self.nonograma.wipe_saved(self.index)
            return 'levels'
