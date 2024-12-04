from INTERFAZ.resource_manager import ResourceManager
from LOGICA.nonograma import Nonograma
from block import Block
from button import Button
import Color
import input_event
import pygame
from pause_menu import PauseMenu
from random import randint

import os


class GameScreen():
    def __init__(self):
        self.nonograma = Nonograma()
        self.blocks = None
        self.mode = None
        self.n = None
        self.scroll_prop = 1
        self.mult = 1
        self.num_filas = None
        self.num_columnas = None
        self.blocks_size = None
        self.mouse_action = -1
        self.index = None
        self.pause_menu = PauseMenu(500, 170, self.nonograma)
        self.pause_button = Button(1190, 10, 'pause_button')
        self.mute_sfx = Button(1130, 10, 'mute_buttonST')
        self.mute_music = Button(1070, 10, 'mute_sounds_buttonST')
        self.pista = Button(1010, 10, 'clue_button')
        self.sol_image = 0
        self.sfx = 0
        self.music = 0
        self.win = ResourceManager.sound_load('win.wav')
        self.completed = None
        self.reset_button = Button(1190, 650, 'reset_level_button')
        self.fondo1 = ResourceManager.image_load('fondo1.png')
        self.fondo2 = ResourceManager.image_load('fondo2.png')
        self.fondo_actual = None
        self.fondo_pista = ResourceManager.image_load('pista_back.png')
        self.time = 0
        self.paused_time = 0
        self.move = [0, 0]
        self.last = [0, 0]
        self.initial = 0
        self.alpha = 0
        self.blocks_pos_change = 0

    def def_level(self, index, mode):
        self.blocks = []
        self.index = index
        self.mode = mode
        self.nonograma.load_level(index, self.mode)
        self.time = pygame.time.get_ticks()
        self.num_filas = self.nonograma.sol_matriz.num_filas
        if self.mode == 'level':
            self.sol_image = ResourceManager.image_load('level' + f'{self.index}' + '.png').convert_alpha()
        self.num_columnas = self.nonograma.sol_matriz.num_columnas
        self.n = len(self.nonograma.sol_board)
        self.completed = 0
        self.blocks_size = int(400 / self.n)
        for i in range(len(self.nonograma.sol_board)):
            for j in range(len(self.nonograma.sol_board)):
                self.blocks.append(Block(j, i, self.blocks_size))
                self.blocks[i * self.n + j].state = self.nonograma.player_board[i][j]
        print(self.num_filas)

    def draw_load(self, surface):
        if self.nonograma.Shop.is_item_purchased("New Wallpaper"):
            self.fondo_actual = self.fondo2
        else:
            self.fondo_actual = self.fondo1
        surface.blit(self.fondo_actual, self.fondo_actual.get_rect())
        dimensions = pygame.font.Font(None, 50)
        dim = dimensions.render('Loading. . .', True, Color.NEGRO)
        surface.blit(dim, (40, 50))
        fuentes = pygame.font.SysFont("Arial", 30)
        minutes = (self.time // 60000)
        seconds = (self.time % 60000) // 1000
        time_string = f"{minutes:02}:{seconds:02}"
        time_text = fuentes.render(f"{time_string}", True, (0, 0, 0))
        surface.blit(time_text, (20, 680))
        self.pause_button.draw(surface)
        self.reset_button.draw(surface)
        self.mute_music.draw(surface)
        self.mute_sfx.draw(surface)
        self.pista.draw(surface)
        surface.blit(dim, (40, 50))



    def draw(self, surface):
        if self.nonograma.Shop.is_item_purchased("New Wallpaper"):
            self.fondo_actual = self.fondo2
        else:
            self.fondo_actual = self.fondo1
        surface.blit(self.fondo_actual, self.fondo_actual.get_rect())
        font = pygame.font.Font(None, int(self.blocks[0].rect_size * 0.9 * self.scroll_prop))
        dimensions = pygame.font.Font(None, 50)
        dim = dimensions.render(str(self.n) + ' x ' + str(self.n), True, Color.NEGRO)
        surface.blit(dim, (40, 50))

        for i in range(self.n):
            for fila in range(len(self.num_filas[i])):
                text_surface = font.render(str((self.num_filas[i][::-1][fila])), True, Color.NEGRO)
                if self.num_filas[i][::-1][fila] >= 10:
                    prop = 0.8
                else:
                    prop = 0.4
                center = text_surface.get_rect(center=self.blocks[i * self.n].rect.center)
                surface.blit(pygame.transform.scale(self.fondo_pista, (int(self.blocks[0].rect_size  * prop * self.scroll_prop), int(self.blocks[0].rect_size * 0.6 * self.scroll_prop))), (
                    center.topleft[0] - int(self.blocks[0].rect_size * self.scroll_prop) - int(
                        self.blocks[0].rect_size * 0.7 * self.scroll_prop) * fila, center.topleft[1]))
                surface.blit(text_surface, (center.topleft[0] - int(self.blocks[0].rect_size * self.scroll_prop) - int(
                    self.blocks[0].rect_size * 0.7 * self.scroll_prop) * fila, center.topleft[1]))

            for j in range(self.n):
                for col in range(len(self.num_columnas[j])):
                    text_surface = font.render(str(self.num_columnas[j][::-1][col]), True, Color.NEGRO)
                    if self.num_columnas[j][::-1][col] >= 10:
                        prop = 0.7
                    else:
                        prop = 0.4
                    center = text_surface.get_rect(center=self.blocks[j].rect.center)
                    surface.blit(pygame.transform.scale(self.fondo_pista, (
                    int(self.blocks[0].rect_size * prop * self.scroll_prop),
                    int(self.blocks[0].rect_size * 0.6 * self.scroll_prop))), (center.topleft[0], center.topleft[1] - int(
                        self.blocks[0].rect_size * self.scroll_prop) - int(
                        self.blocks[0].rect_size * 0.7 * self.scroll_prop) * col))
                    surface.blit(text_surface, (center.topleft[0], center.topleft[1] - int(
                        self.blocks[0].rect_size * self.scroll_prop) - int(
                        self.blocks[0].rect_size * 0.7 * self.scroll_prop) * col))
                self.blocks[i * self.n + j].draw(surface, self.scroll_prop, self.move)

        fuentes = pygame.font.SysFont("Arial", 30)
        if self.pause_menu.state != 1 and self.completed != 1:
            self.paused_time = pygame.time.get_ticks() - self.time
        else:
            self.time += pygame.time.get_ticks() - (self.time + self.paused_time)
        elapsed_time = pygame.time.get_ticks() - self.time
        minutes = (elapsed_time // 60000)
        seconds = (elapsed_time % 60000) // 1000
        time_string = f"{minutes:02}:{seconds:02}"
        time_text = fuentes.render(f"{time_string}", True, (0, 0, 0))

        if self.completed == 1 and self.mode == 'level':
            if self.alpha < 255:
                self.alpha += 10
                if self.alpha > 255:
                    self.alpha = 255

            self.sol_image.set_alpha(self.alpha)
            surface.blit(pygame.transform.scale(self.sol_image, (
            self.blocks[self.n - 1].rect.x - self.blocks[0].rect.x + int(self.blocks_size * self.scroll_prop),
            self.blocks[self.n * self.n - 1].rect.y - self.blocks[0].rect.y + int(
                self.blocks_size * self.scroll_prop))),
                         (self.blocks[0].rect.x, self.blocks[0].rect.y))

        surface.blit(time_text, (20, 680))
        self.pause_button.draw(surface)
        self.reset_button.draw(surface)
        self.mute_music.draw(surface)
        self.mute_sfx.draw(surface)
        self.pista.draw(surface)
        surface.blit(dim, (40, 50))

        if self.pause_menu.state == 1:
            self.pause_menu.draw(surface)

    def handle_events(self, events):
        if self.nonograma.win_condition() and self.completed == 0:
            self.win.play()
            self.nonograma.set_completed(self.index, self.mode)
            self.alpha = 0
            self.completed = 1

        if self.reset_button.click_event(events):
            for i in range(self.n):
                for j in range(self.n):
                    self.nonograma.set_box_value(i, j, 0)
                    self.blocks[i * self.n + j].state_change(0, self.sfx)
            self.nonograma.wipe_saved(self.index, self.mode)
            self.time = pygame.time.get_ticks()
            self.alpha = 0
            self.completed = 0

        if self.pista.click_event(events) and self.completed == 0:
            while True:
                x = randint(0, self.n - 1)
                y = randint(0, self.n - 1)
                if (self.nonograma.player_board[y][x] == 0 or self.nonograma.player_board[y][x] == 2) and \
                        self.nonograma.sol_board[y][x] == 1:
                    self.nonograma.player_board[y][x] = 4
                    self.blocks[y * self.n + x].state_change(self.nonograma.player_board[y][x], 1)
                    break
                if self.nonograma.player_board[y][x] == 1 and self.nonograma.sol_board[y][x] == 0:
                    self.nonograma.player_board[y][x] = 5
                    self.blocks[y * self.n + x].state_change(self.nonograma.player_board[y][x], 1)
                    break

        if input_event.esc_press(events):
            self.pause_menu.set_state()

        if self.pause_button.click_event(events) and self.pause_menu.state == 0:
            self.pause_menu.set_state()

        if self.pause_menu.state == 0:
            if input_event.scroll_up(events):
                if input_event.shift_pressed():
                    self.scroll_prop += 0.1
            if input_event.scroll_down(events):
                if input_event.shift_pressed() and self.scroll_prop > 0.5:
                    self.scroll_prop -= 0.1
                    self.scroll_prop = max(self.scroll_prop, 0)

            if self.mute_sfx.click_event(events):
                if self.sfx == 0:
                    self.sfx = 1
                else:
                    self.sfx = 0

            if self.mute_music.click_event(events):
                if self.music == 0:
                    ResourceManager.stop_music()
                    self.music = 1
                else:
                    if self.nonograma.Shop.is_item_purchased("New Music"):
                        ResourceManager.music_load("game2.wav")
                    else:
                        ResourceManager.music_load("game.wav")
                    self.music = 0

            if input_event.shift_pressed():
                if input_event.left_click(events):
                    self.initial = pygame.mouse.get_pos()
                if input_event.left_hold():
                    self.move[0] = self.last[0] - self.initial[0] + pygame.mouse.get_pos()[0]
                    self.move[1] = self.last[1] - self.initial[1] + pygame.mouse.get_pos()[1]
                else:
                    self.last[0] = self.move[0]
                    self.last[1] = self.move[1]
            else:
                self.last[0] = self.move[0]
                self.last[1] = self.move[1]

            if input_event.r_press(events):
                self.scroll_prop = 1
                self.scroll_y = 0
                self.move[0] = 0
                self.move[1] = 0

            if self.completed == 0 and not input_event.shift_pressed() :
                for i in range(self.n):
                    for j in range(self.n):
                        if self.blocks[i * self.n + j].collide() and self.blocks[i * self.n + j].state != 4 and \
                                self.blocks[i * self.n + j].state != 5:
                            if self.blocks[i * self.n + j].state == 0 and self.mouse_action != 0:
                                self.blocks[i * self.n + j].state = 3
                            if input_event.left_click(events):
                                if self.nonograma.player_board[i][j] == 1:
                                    self.mouse_action = 0
                                else:
                                    self.mouse_action = 1
                            if input_event.right_click(events):
                                if self.nonograma.player_board[i][j] == 2:
                                    self.mouse_action = 0
                                else:
                                    self.mouse_action = 2
                            if input_event.left_hold() and not self.mouse_action == -1:
                                self.nonograma.set_box_value(i, j, self.mouse_action)
                                self.blocks[i * self.n + j].state_change(self.nonograma.player_board[i][j], self.sfx)
                            elif input_event.right_hold() and not self.mouse_action == -1:
                                self.nonograma.set_box_value(i, j, self.mouse_action)
                                self.blocks[i * self.n + j].state_change(self.nonograma.player_board[i][j], self.sfx)
                            else:
                                self.mouse_action = -1
                        else:
                            if self.blocks[i * self.n + j].state == 3:
                                self.blocks[i * self.n + j].state = 0
        else:
            self.mouse_action = -1
            result = self.pause_menu.handle_events(events, self.index, self.mode)
            if result:
                self.move[0] = 0
                self.move[1] = 0
                self.win.stop()
                self.mute_music = Button(1070, 10, 'mute_sounds_buttonST')
                self.music = 0
                self.time = 0
                self.blocks = None
                self.scroll_prop = 1
                self.pause_menu.state = 0
                return result

    def change_wallpaper(self):
        ResourceManager.image_load('fondo2.png')
