import pygame
from button import Button
from resource_manager import ResourceManager
import sys
import Color

class PauseMenu:
    def __init__(self, x, y, nonograma):
        self.x = x
        self.y = y
        self.nonograma = nonograma
        self.state = 0
        self.resume_Button = Button(515, 200, ResourceManager.image_load('resume_button.png'))
        self.back_levels_menu_Button = Button(515, 400, ResourceManager.image_load('return_levels_button.png'))
        self.save_level = Button(515, 300, ResourceManager.image_load('save_button.png'))
        self.exit_The_Game_Button = Button(581, 500, ResourceManager.image_load('exit_button.png'))
        self.background_surface = pygame.Surface((1280, 720), pygame.SRCALPHA)
        self.background_surface.fill((0, 0, 0, 128))

    def draw(self, surface):
        surface.blit(self.background_surface, (0, 0))
        pygame.draw.rect(surface, Color.BLANCO, pygame.Rect((self.x, self.y),(290, 410)))
        self.resume_Button.draw(surface)
        self.back_levels_menu_Button.draw(surface)
        self.save_level.draw(surface)
        self.exit_The_Game_Button.draw(surface)

    def handle_events(self, events, index):
        if self.back_levels_menu_Button.click_event(events):
            return 'levels'
        elif self.save_level.click_event(events):
            self.nonograma.save_level(index)
        elif self.resume_Button.click_event(events):
            self.state = 0
        elif self.exit_The_Game_Button.click_event(events):
            pygame.quit()
            sys.exit()
        return None

    def set_state(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0
