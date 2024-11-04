import pygame
import Color
from resource_manager import ResourceManager


class Block:
    def __init__(self, x, y, size):
        self.state = 0
        self.x = x
        self.y = y
        self.rect_size = size
        self.face_size = size - 2
        self.rect = None
        self.face = None
        self.lock = ResourceManager.image_load('fallo.png')

    def collide(self):
        if self.face.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def state_change(self, mouse_action):
        self.state = mouse_action

    def draw(self, surface):
        xprop = surface.get_size()[0] / 1280
        yprop = surface.get_size()[1] / 720
        self.rect = pygame.Rect(int(self.x * xprop), int(self.y * yprop), int(self.rect_size * xprop), int(self.rect_size * yprop)) # Estos son los bordes del bloque
        self.face = pygame.Rect(int((self.x + 1) * xprop), int((self.y + 1) * yprop), int(self.face_size * xprop), int(self.face_size * yprop))

        pygame.draw.rect(surface, Color.GRIS, self.rect)
        if self.state == 0:
            pygame.draw.rect(surface, Color.BLANCO, self.face)
        if self.state == 1:
            pygame.draw.rect(surface, Color.NEGRO, self.face)
        if self.state == 2:
            pygame.draw.rect(surface, Color.BLANCO, self.face)
            surface.blit(pygame.transform.scale(self.lock, (int(self.face_size * xprop), int(self.face_size * yprop))), (int((self.x + 1) * xprop), int((self.y + 1) * yprop)))
        if self.state == 3:
            pygame.draw.rect(surface, Color.GRIS_CLARO, self.face)
