from numpy.core.defchararray import center

from INTERFAZ.resource_manager import ResourceManager
from LOGICA.nonograma import Nonograma
from LOGICA.nonogramaCreator import NonogramaCreator
from block import Block
from button import Button
import Color
import input_event
import pygame
from  pause_menu import PauseMenu

import os

class GameEditor():
    def __init__(self):
        self.nonograma_creator = None
        self.nonograma=Nonograma()
        self.blocks = None
        self.n = None
        self.scroll_prop = 1
        self.blocks_size = None
        self.mouse_action = -1
        self.index = None
        self.exit = Button(1190, 640, 'back_button')
        self.mute_sfx = Button(1130, 10, 'mute_buttonST')
        self.mute_music = Button(1070, 10, 'mute_sounds_buttonST')
        self.sfx = 0
        self.music = 0
        self.save_button=Button(960,320,'save_button')
        self.move = [0, 0]
        self.last = [0, 0]
        self.initial = 0
        self.fondo1 = ResourceManager.image_load('fondo1.png')
        self.fondo2 = ResourceManager.image_load('fondo2.png')
        self.fondo_actual = None


    def set_size(self, n):
        self.nonograma_creator = NonogramaCreator(n)
        self.n = n
        self.blocks = []
        self.blocks_size = int(400 / self.n)
        for i in range(self.n):
            for j in range(self.n):
                self.blocks.append(Block(j, i, self.blocks_size))
                self.blocks[i * self.n + j].state = self.nonograma_creator.player_board[i][j]
    def draw_load(self, surface):
        if self.nonograma.Shop.is_item_purchased("New Wallpaper"):
            self.fondo_actual = self.fondo2
        else:
            self.fondo_actual = self.fondo1
        surface.blit(self.fondo_actual, self.fondo_actual.get_rect())
        dimensions = pygame.font.Font(None, 50)
        dim = dimensions.render('Loading. . .', True, Color.NEGRO)
        surface.blit(dim, (40, 50))

        self.exit.draw(surface)
        self.mute_music.draw(surface)
        self.mute_sfx.draw(surface)
        surface.blit(dim, (40, 50))

    def draw(self, surface):
        if self.nonograma.Shop.is_item_purchased("New Wallpaper"):
            self.fondo_actual = self.fondo2
        else:
            self.fondo_actual = self.fondo1
        surface.blit(self.fondo_actual, self.fondo_actual.get_rect())
        dimensions = pygame.font.Font(None, 50)
        dim = dimensions.render(str(self.n) + ' x ' + str(self.n), True, Color.NEGRO)

        for i in range(self.n):
            for j in range(self.n):
                self.blocks[i * self.n + j].draw(surface, self.scroll_prop,self.move)


        self.mute_music.draw(surface)
        self.mute_sfx.draw(surface)
        self.exit.draw(surface)
        self.save_button.draw(surface)
        surface.blit(dim, (40, 50))

    def handle_events(self,events):
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
                ResourceManager.music_load('main.wav')
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
            self.move[0] = 0
            self.move[1] = 0

        if self.exit.click_event(events):
            if self.music == 1:
                self.music = 0
                self.mute_music = Button(1070, 10, 'mute_sounds_buttonST')
                ResourceManager.stop_music()
                ResourceManager.music_load("main.wav")
            return 'editor_size_board'

        if self.save_button.click_event(events):
            if not self.nonograma_creator.save_new_level():
                if self.music == 1:
                    self.music = 0
                    self.mute_music = Button(1070, 10, 'mute_sounds_buttonST')
                    ResourceManager.stop_music()
                    ResourceManager.music_load("main.wav")
                return
            if self.music == 1:
                self.music = 0
                self.mute_music = Button(1070, 10, 'mute_sounds_buttonST')
                ResourceManager.stop_music()
                ResourceManager.music_load("main.wav")
            return 'editor_levels'


        if not input_event.shift_pressed():
            for i in range(self.n):
                for j in range(self.n):
                    if self.blocks[i * self.n + j].collide():
                        if self.blocks[i * self.n + j].state == 0 and self.mouse_action != 0:
                            self.blocks[i * self.n + j].state = 3
                        if input_event.left_click(events):
                            if self.nonograma_creator.player_board[i][j] == 1:
                                self.mouse_action = 0
                            else:
                                self.mouse_action = 1
                        if input_event.left_hold() and not self.mouse_action == -1:
                            self.nonograma_creator.set_box_value(i, j, self.mouse_action)
                            self.blocks[i * self.n + j].state_change(self.nonograma_creator.player_board[i][j], self.sfx)
                        else:
                            self.mouse_action = -1
                    else:
                        if self.blocks[i * self.n + j].state == 3:
                            self.blocks[i * self.n + j].state = 0