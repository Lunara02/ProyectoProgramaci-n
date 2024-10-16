import pygame

from LOGICA.gestor_recursos import GestorRecursos
from button import Button
import Color


class Difficult():
    def __init__(self):
        self.title_font = pygame.font.Font(None, 74)
        self.level_button = Button(300, 300, GestorRecursos.image_load('icon.png'))