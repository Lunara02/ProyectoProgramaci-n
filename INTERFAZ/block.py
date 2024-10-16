import pygame
import Color
import mouse_event


class Block:
    def __init__(self, x, y, size):
        self.state = 0
        self.x = x
        self.y = y
        self.rect_size = size
        self.face_size = size - 2
        self.rect = None
        self.face = None

    def handle_event(self, events):
        if mouse_event.left_click(events):
            if self.face.collidepoint(pygame.mouse.get_pos()):
                self.state = 1
                return 1
        elif mouse_event.right_click(events):
            if self.face.collidepoint(pygame.mouse.get_pos()):
                self.state = 0
                return 0

    def draw(self, surface):
        xprop = surface.get_size()[0] / 1280
        yprop = surface.get_size()[1] / 720
        self.rect = pygame.Rect(int(self.x * xprop), int(self.y * yprop), int(self.rect_size * xprop), int(self.rect_size * yprop)) # Estos son los bordes del bloque
        self.face = pygame.Rect(int((self.x + 1) * xprop), int((self.y + 1) * yprop), int(self.face_size * xprop), int(self.face_size * yprop))

        pygame.draw.rect(surface, Color.NEGRO, self.rect)
        if self.state == 0:
            pygame.draw.rect(surface, Color.BLANCO, self.face)
        if self.state == 1:
            pygame.draw.rect(surface, Color.NEGRO, self.face)