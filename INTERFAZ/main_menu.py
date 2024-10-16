import pygame
from button import Button
from LOGICA.gestor_recursos import GestorRecursos
import Color

class MainMenu():
    def __init__(self):
        self.title_font = pygame.font.Font(None, 74)
        self.diff_button = Button(300, 300, GestorRecursos.image_load('icon.png'))

    def draw(self, surface):
        surface.fill(Color.AZUL)
        title = self.title_font.render("Menu Principal", True, Color.BLANCO)
        surface.blit(title, (100, 100))
        self.diff_button.draw(surface)

    def handle_events(self, events):
        if self.diff_button.click_event(events):
            return 'difficulty'
        return None