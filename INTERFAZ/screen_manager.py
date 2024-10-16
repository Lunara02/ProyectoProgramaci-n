from difficulty import Difficult
from main_menu import MainMenu
from levels import Levels
from game import GameScreen


class ScreenManager:
    def __init__(self):
        self.screens = {
            'main_menu': MainMenu(),
            'difficulty': Difficult(),
            'levels': Levels(),
            'game': GameScreen()
        }
        self.current_screen = 'main_menu'

    def handle_events(self, events):
        result = self.screens[self.current_screen].handle_events(events)
        if result:
            if isinstance(result, tuple):
                next_screen, level_index = result
                self.screens['game'].def_level(level_index)
                self.current_screen = next_screen.lower()
            else:
                self.current_screen = result.lower()