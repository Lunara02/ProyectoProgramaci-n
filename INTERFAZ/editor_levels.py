import pygame

from LOGICA.nonograma import Nonograma
from button import Button
from INTERFAZ.resource_manager import ResourceManager
from button import Button
from LOGICA.nonogramaCreator import num_levels
import Color
import math
import input_event


class MyLevels():
    def __init__(self):
        self.nonograma = Nonograma()
        self.list_levels=None
        self.niveles=None
        self.filas=None
        self.y_scroll = 0
        self.my_levels_menu_top_bar = ResourceManager.image_load('my_levels_menu_top_bar.png')
        self.level_font = pygame.font.Font(None, 60)
        self.image = pygame.transform.scale(ResourceManager.image_load('my_levels_background.png'), (1280, 720))
        self.create_button = Button(1000, 20, 'create_levels_button')

        self.exit = Button(1190, 640, 'back_button')

    def reload_levels(self):
        self.list_levels = []
        self.niveles = num_levels()

        self.filas = math.ceil(self.niveles / 7)
        button_image = 'level_button'

        for i in range(self.filas):
            for j in range(abs(7 - (7 + self.niveles % 7) * (math.ceil((self.niveles % 7) / 7)) * (
            math.floor((i + 1) / self.filas)))):
                self.list_levels.append(Button(100 + 150 * j, 120 + 200 * i, button_image))

    def draw(self, surface):
        surface.blit(self.image, (0,0))
        # mylevels
        self.exit.draw(surface)
        for i in range(self.filas):
            for j in range(abs(7 - (7 + self.niveles % 7) * (math.ceil((self.niveles % 7) / 7)) * (math.floor((i + 1) / self.filas)))):
                self.list_levels[j + 7 * i].y_scroll = self.y_scroll
                self.list_levels[j + 7 * i].draw(surface)
                level = self.level_font.render(f"{j + i * 7 + 1}", True, Color.NEGRO)
                level_rect = level.get_rect(center=(j * 150 + 64 + 100, 184 + i * 200 + self.y_scroll))
                surface.blit(level, level_rect)
        surface.blit(self.my_levels_menu_top_bar, self.my_levels_menu_top_bar.get_rect())
        self.create_button.draw(surface)


    def handle_events(self, events):
        if self.niveles > 14:
            if input_event.scroll_down(events) and self.list_levels[self.niveles - 1].y + self.y_scroll > 572:
                self.y_scroll -= 15
            if input_event.scroll_up(events) and self.list_levels[0].y + self.y_scroll < 120:
                self.y_scroll += 15
        for index, button in enumerate(self.list_levels, start=1):
            if button.click_event(events):
                ResourceManager.stop_music()
                if self.nonograma.Shop.is_item_purchased("New Music"):
                    ResourceManager.music_load("game2.wav")
                else:
                    ResourceManager.music_load("game.wav")
                return 'game', index, 'my_level'

        if self.exit.click_event(events):
            return 'main_menu'
        if self.create_button.click_event(events):
            return 'editor_size_board'
        return None
