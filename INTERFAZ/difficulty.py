import pygame

from resource_manager import ResourceManager
from button import Button
import Color


class Difficult():
    def __init__(self):
        self.title_font = pygame.font.Font(None, 74)
        self.level_button = Button(300, 300, ResourceManager.image_load('icon.png'))

    def draw(self, surface):
        surface.fill((0, 100, 100))
        title = self.title_font.render("Dificultad", True, Color.BLANCO)
        surface.blit(title, (100, 100))
        self.level_button.draw(surface)

    def handle_events(self, events):
        if self.level_button.click_event(events):
            return 'levels'
        return None