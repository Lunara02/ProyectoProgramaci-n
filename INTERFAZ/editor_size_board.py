import pygame

from INTERFAZ.resource_manager import ResourceManager
from button import Button
import Color
import math
import input_event

class SizeBoard():
    def __init__(self):
        self.size_font = pygame.font.Font(None, 60)
        self.image = pygame.transform.scale(ResourceManager.image_load('my_levels_background.png'), (1280, 720))
        self.image2 = ResourceManager.image_load('select_size_top_bar.png')
        self.list_size=[]
        self.size = 18
        buttons_per_row = 7
        self.filas = math.ceil(self.size / buttons_per_row)

        for i in range(self.filas):
            for j in range(min(buttons_per_row, self.size - i * buttons_per_row)):
                x = 100 + 150 * j
                y = 130 + 200 * i
                self.list_size.append(Button(x, y, 'level_button'))

        self.exit = Button(1190, 640, 'back_button')


    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        surface.blit(self.image2, (0, 0))
        self.exit.draw(surface)


        self.exit.draw(surface)
        for i in range(self.filas):
            for j in range(abs(7 - (7 + self.size % 7) * (math.ceil((self.size % 7) / 7)) * (math.floor((i + 1) / self.filas)))):
                self.list_size[j + 7 * i].draw(surface)
                level = self.size_font.render(f"{j + i * 7 + 3}", True, Color.NEGRO)
                level_rect = level.get_rect(center=(j * 150 + 64 + 100, 194 + i * 200))
                surface.blit(level, level_rect)

    def handle_events(self, events):
        for size, button in enumerate(self.list_size, start=1):
            if button.click_event(events):
                return 'editor_game', size+2, None
        if self.exit.click_event(events):
            return 'editor_levels'
        return None