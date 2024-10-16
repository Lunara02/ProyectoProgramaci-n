import pygame
from button import Button
from LOGICA.gestor_recursos import GestorRecursos
import Color

class MainMenu():
    def __init__(self):
        self.title_font = pygame.font.Font(None, 74)
        self.diff_button = Button(300, 300, GestorRecursos.image_load('icon.png'))