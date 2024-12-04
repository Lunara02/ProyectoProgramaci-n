from difficulty import Difficult
from main_menu import MainMenu
from levels import Levels
from editor_levels import MyLevels
from editor_game import GameEditor
from editor_size_board import SizeBoard
from game import GameScreen
from INTERFAZ.tienda import Tienda
from fade import Fade
import pygame
from resource_manager import ResourceManager
class ScreenManager:
    def __init__(self):
        self.screens = {
            'main_menu': MainMenu(),
            'difficulty': Difficult(),
            'levels': Levels(),
            'game': GameScreen(),
            'editor_levels': MyLevels(),
            'editor_game': GameEditor(),
            'editor_size_board': SizeBoard(),
            'shop': Tienda()
        }
        ResourceManager.music_load("main.wav")
        self.current_screen = 'main_menu'
        self.fade = Fade(pygame.display.get_surface(), self.screens)

    def handle_events(self, events):
        result = self.screens[self.current_screen].handle_events(events)
        if result:
            if isinstance(result, tuple):
                next_screen, level_index, mode = result
                if next_screen == 'game':
                    self._fade_transition(next_screen)
                    self.screens['game'].def_level(level_index, mode)
                elif next_screen=='editor_game':
                    self._fade_transition(next_screen)
                    self.screens['editor_game'].set_size(level_index)
            else:
                if result =='editor_levels':
                    self.screens['editor_levels'].reload_levels()
                self._fade_transition(result.lower())

    def draw(self, surface):
        self.screens[self.current_screen].draw(surface)
        pygame.display.flip()

    def _fade_transition(self, next_screen):
        self.fade.fade_out()
        self.current_screen = next_screen.lower()
        self.fade.fade_in(next_screen.lower())