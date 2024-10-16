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
