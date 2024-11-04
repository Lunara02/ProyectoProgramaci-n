import pygame
from button import Button
import sys
from INTERFAZ.resource_manager import ResourceManager
import Color

class MainMenu():
    def __init__(self):
        self.title_font = pygame.font.Font(None, 74)
        self.diff_button = Button(569, 300, ResourceManager.image_load('play_button.png'))
        self.exit_button = Button(569, 400, ResourceManager.image_load('exit_button.png'))

    def draw(self, surface):
        surface.fill(Color.BLANCO)
        title = self.title_font.render("Super Nonograma", True, Color.NEGRO)
        title_rect = title.get_rect(center=(surface.get_width() // 2, 100)) #centra el centro del rect (importante para refactor numeros pista)
        surface.blit(title, title_rect.topleft)
        self.diff_button.draw(surface)
        self.exit_button.draw(surface)

    def handle_events(self, events):
        if self.diff_button.click_event(events):
            return 'levels'
        elif self.exit_button.click_event(events):
            pygame.quit()
            sys.exit()
        return None