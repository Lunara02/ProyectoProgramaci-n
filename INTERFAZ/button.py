import pygame
import input_event


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = image.get_rect()
        self.x = x
        self.y = y
        self.pressed = False

    def draw(self, surface):
        self.rect.topleft = (self.x, self.y)
        surface.blit(self.image, self.rect.topleft)

    def click_event(self, events):
        if input_event.left_click(events):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False