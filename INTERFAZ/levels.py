import pygame

from INTERFAZ.resource_manager import ResourceManager
from button import Button
import Color
import input_event


class Levels():
    def __init__(self):
        self.title_font = pygame.font.Font(None, 74)
        self.level_font = pygame.font.Font(None, 60)
        button_image = ResourceManager.image_load('level_button.png')
        self.level_1 = Button(100, 200, button_image)
        self.level_2 = Button(250, 200, button_image)
        self.level_3 = Button(400, 200, button_image)
        self.level_4 = Button(550, 200, button_image)
        self.level_5 = Button(700, 200, button_image)
        self.level_6 = Button(850, 200, button_image)
        self.level_7 = Button(700, 400, button_image)
        self.level_8 = Button(800, 400, button_image)
        self.level_9 = Button(900, 400, button_image)
        self.level_10 = Button(1000, 400, button_image)
        self.list_levels = [self.level_1, self.level_2, self.level_3, self.level_4, self.level_5,
                            self.level_6]
        self.exit = Button(1190, 640, ResourceManager.image_load('back_button.png'))

    def draw(self, surface):
        surface.fill((Color.BLANCO))
        title = self.title_font.render("Niveles", True, Color.NEGRO)
        title_rect = title.get_rect(center=(surface.get_width() // 2, 100))
        surface.blit(title, title_rect.topleft)
        self.exit.draw(surface)
        for index, button in enumerate(self.list_levels):
            button.draw(surface)
            level = self.level_font.render(f"{index+1}", True, Color.NEGRO)
            level_rect = level.get_rect()
            level_rect.center = (index*150 + 128/2 + 100, 200 + 128/2)
            surface.blit(level,level_rect)

    def handle_events(self, events):
        for index, button in enumerate(self.list_levels, start=1):
            if button.click_event(events):
                return 'game', index
        if self.exit.click_event(events):
            return 'main_menu'
        return None
