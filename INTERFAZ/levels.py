import pygame

from LOGICA.gestor_recursos import GestorRecursos
from button import Button
import Color


class Levels():
    def __init__(self):
        self.title_font = pygame.font.Font(None, 74)
        button_image = GestorRecursos.image_load('icon.png')
        self.level_1 = Button(100, 200, button_image)
        self.level_2 = Button(100, 300, button_image)
        self.level_3 = Button(100, 400, button_image)
        self.list_levels = [self.level_1, self.level_2, self.level_3]

    def draw(self, surface):
        surface.fill((100, 0, 100))
        title = self.title_font.render("Niveles", True, Color.BLANCO)
        surface.blit(title, (100, 100))

        for button in self.list_levels:
            button.draw(surface)