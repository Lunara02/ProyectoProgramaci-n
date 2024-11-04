import pygame

from INTERFAZ.resource_manager import ResourceManager
from button import Button
import Color
import input_event


class Levels():
    def __init__(self):
        self.title_font = pygame.font.Font(None, 74)
        button_image = ResourceManager.image_load('icon.png')
        self.level_1 = Button(100, 200, button_image)
        self.level_2 = Button(100, 300, button_image)
        self.level_3 = Button(100, 400, button_image)
        self.level_4 = Button(100, 500, button_image)
        self.level_5 = Button(100, 600, button_image)
        self.level_6 = Button(400, 200, button_image)
        self.level_7 = Button(400, 300, button_image)
        self.level_8 = Button(400, 400, button_image)
        self.level_9 = Button(400, 500, button_image)
        self.level_10 = Button(400, 600, button_image)

        self.list_levels = [self.level_1, self.level_2, self.level_3, self.level_4, self.level_5,
                            self.level_6, self.level_7, self.level_8, self.level_9, self.level_10]
        self.exit = Button(980, 640, ResourceManager.image_load('icon.png'))

    def draw(self, surface):
        surface.fill((100, 0, 100))
        title = self.title_font.render("Niveles", True, Color.BLANCO)
        surface.blit(title, (100, 100))
        self.exit.draw(surface)
        for button in self.list_levels:
            button.draw(surface)

    def handle_events(self, events):
        for index, button in enumerate(self.list_levels, start=1):
            if button.click_event(events):
                return 'game', index
        if self.exit.click_event(events):
            return 'main_menu'
        return None
