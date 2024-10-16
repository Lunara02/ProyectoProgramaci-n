import pygame
import mouse_event


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.pressed = False

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def click_event(self, events):
        if mouse_event.left_click(events):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False