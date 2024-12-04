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
        self.resume_Button = Button(515, 200, 'resume_button')
        self.back_levels_menu_Button = Button(515, 400, 'return_levels_button')
        self.save_level = Button(515, 300, 'save_button')
        self.exit_The_Game_Button = Button(581, 500, 'exit_button')

    def draw(self, surface):
        background_surface = pygame.Surface((surface.get_size()[0], surface.get_size()[1]), pygame.SRCALPHA)
        background_surface.fill((0, 0, 0, 128))
        surface.blit(background_surface, (0, 0))
        pygame.draw.rect(surface, Color.BLANCO, pygame.Rect((self.x, self.y),(290, 410)))
        self.resume_Button.draw(surface)
        self.back_levels_menu_Button.draw(surface)
        self.save_level.draw(surface)
        self.exit_The_Game_Button.draw(surface)

    def handle_events(self, events, index, mode):
        if self.back_levels_menu_Button.click_event(events):
            if mode == 'level':
                ResourceManager.stop_music()
                ResourceManager.music_load("main.wav")
                return 'levels'
            elif mode =='my_level':
                ResourceManager.stop_music()
                ResourceManager.music_load("main.wav")
                return 'editor_levels'
        elif self.save_level.click_event(events):
            self.nonograma.save_level(index, mode)
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
