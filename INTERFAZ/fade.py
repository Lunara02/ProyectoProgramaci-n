import pygame
from game import GameScreen


class Fade:
    def __init__(self, screen, screens ,fade_speed=30):
        self.screens = screens
        self.screen = screen
        self.fade_speed = fade_speed
        self.fade_surface = pygame.Surface(self.screen.get_size())
        self.fade_surface.fill((0, 0, 0))  # Color de la transición, negro por defecto
        self.alpha = 0

    def fade_out(self):
        self.alpha = 0
        while self.alpha < 255:
            self.alpha += self.fade_speed
            if self.alpha > 255:
                self.alpha = 255
            self.fade_surface.set_alpha(self.alpha)
            self.screen.blit(self.fade_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(7)

    def fade_in(self, curren_screens):
        self.alpha = 255
        while self.alpha > 0:
            self.alpha -= self.fade_speed
            if self.alpha < 0:
                self.alpha = 0
            if curren_screens == 'game' or curren_screens=='editor_game':
                self.screens[curren_screens].draw_load(self.screen)
            else:
                self.screens[curren_screens].draw(self.screen)
            self.fade_surface.set_alpha(self.alpha)
            self.screen.blit(self.fade_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(7)
