import pygame
import input_event
from INTERFAZ.resource_manager import ResourceManager


class Button:
    def __init__(self, x, y, image, item=None):
        self.state = ''
        self.image_name = image
        self.image = ResourceManager.image_load(image + '.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.y_scroll = 0
        self.pressed = False
        self.item = item

    def draw(self, surface):
        self.rect.topleft = (self.x, self.y + self.y_scroll)
        if self.rect.collidepoint(pygame.mouse.get_pos()) and 'buttonST' in self.image_name:
            surface.blit(ResourceManager.image_load(self.image_name + self.state + 'A.png'), self.rect.topleft)
        elif self.rect.collidepoint(pygame.mouse.get_pos()) and 'button' in self.image_name:
            surface.blit(ResourceManager.image_load(self.image_name + 'A.png'), self.rect.topleft)
        else:
            surface.blit(self.image, self.rect.topleft)

    def click_event(self, events):
        if input_event.left_click(events):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if 'buttonST' in self.image_name:
                    self.change_state()
                return True
        return False

    def change_state(self):
        if self.state == '':
            self.state = '1'
        else:
            self.state = ''
        self.image = ResourceManager.image_load(self.image_name + self.state + '.png')

    def update_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.topleft = (x, y)

