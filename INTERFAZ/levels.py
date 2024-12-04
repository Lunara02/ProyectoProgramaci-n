import pygame

from INTERFAZ.resource_manager import ResourceManager
from LOGICA.nonograma import Nonograma
from LOGICA.item import Item
from button import Button
import Color
import math
import input_event


class Levels():
    def __init__(self):
        self.nonograma = Nonograma()
        self.title_font = pygame.font.Font(None, 74)
        self.level_font = pygame.font.Font(None, 60)
        self.list_levels = []
        self.list_image_levels = []
        self.niveles = 21
        self.levels_menu = ResourceManager.image_load('levels_menu.png')
        self.levels_menu_top_bar = ResourceManager.image_load('levels_menu_top_bar.png')
        self.filas = math.ceil(self.niveles / 7)
        buttons_per_row = 7
        self.filas = math.ceil(self.niveles / buttons_per_row)
        for i in range(self.filas):
            for j in range(min(buttons_per_row, self.niveles - i * buttons_per_row)):
                self.list_image_levels.append(pygame.transform.scale(ResourceManager.image_load('level' + f'{i * 7 + j + 1}' + '.png'), (116, 118)))
                x = 100 + 150 * j
                y = 130 + 200 * i
                self.list_levels.append(Button(x, y, 'level_button'))
        self.exit = Button(1190, 640, 'back_button')


    def draw(self, surface):
        surface.fill(Color.BLANCO)
        surface.blit(self.levels_menu,
                     self.levels_menu.get_rect())
        self.exit.draw(surface)
        for i in range(self.filas):
            for j in range(abs(7 - (7 + self.niveles % 7) * (math.ceil((self.niveles % 7) / 7)) * (math.floor((i + 1) / self.filas)))):
                level = self.level_font.render(f"{j + i * 7 + 1}", True, Color.NEGRO)
                level_rect = level.get_rect(center=(j * 150 + 64 + 100, 194 + i * 200))
                if j + 7 * i != 20:
                    self.list_levels[j + 7 * i].draw(surface)
                    surface.blit(level, level_rect)
                    if self.nonograma.completado[j + 7 * i] == 1:
                        surface.blit(self.list_image_levels[i * 7 + j],
                                     (self.list_levels[j + 7 * i].x + 7, self.list_levels[j + 7 * i].y + 5))
                else:
                    if self.nonograma.Shop.is_item_purchased('New Level'):
                        self.list_levels[j + 7 * i].draw(surface)
                        surface.blit(level, level_rect)
                        if self.nonograma.completado[j + 7 * i] == 1:
                            surface.blit(self.list_image_levels[i * 7 + j],
                                         (self.list_levels[j + 7 * i].x + 7, self.list_levels[j + 7 * i].y + 5))
        surface.blit(self.levels_menu_top_bar, self.levels_menu_top_bar.get_rect())

    def handle_events(self, events):
        for index, button in enumerate(self.list_levels, start=1):
            if index != 21:
                if button.click_event(events):
                        self.scroll_y = 0
                        ResourceManager.stop_music()
                        if self.nonograma.Shop.is_item_purchased("New Music"):
                            ResourceManager.music_load("game2.wav")
                        else:
                            ResourceManager.music_load("game.wav")
                        return 'game', index, 'level'
            else:
                if self.nonograma.Shop.is_item_purchased('New Level'):
                    if button.click_event(events):
                        self.scroll_y = 0
                        ResourceManager.stop_music()
                        if self.nonograma.Shop.is_item_purchased("New Music"):
                            ResourceManager.music_load("game2.wav")
                        else:
                            ResourceManager.music_load("game.wav")
                        return 'game', index, 'level'
        if self.exit.click_event(events):
            return 'main_menu'
        return None
