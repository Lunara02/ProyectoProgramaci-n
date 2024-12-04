import pygame

import Color
from resource_manager import ResourceManager
import math
from LOGICA.nonograma import Nonograma

class Block:
    def __init__(self, x, y, size):
        self.state = 0
        self.x = x
        self.y = y
        self.y_pos = 0
        self.rect_size = size
        self.face_size = size * 0.94
        self.spacing = (self.rect_size - self.face_size) / 2
        self.rect = pygame.Rect(int(640 + (self.x * (self.rect_size - self.spacing) - 200)), int(360 + (self.y * (self.rect_size - self.spacing) - 100)), int(self.rect_size), int(self.rect_size))
        self.face = pygame.Rect(self.rect.center[0] - int((self.face_size / 2)), self.rect.center[1] - int((self.face_size / 2)), int(self.face_size), int(self.face_size))
        self.nonograma = Nonograma()
        self.lock = ResourceManager.image_load('fallo.png')
        self.fallo = ResourceManager.image_load('fallo_pista.png')
        self.default_mark = ResourceManager.sound_load('mark.wav')
        self.default_delete = ResourceManager.sound_load('delete.wav')
        self.default_locking = ResourceManager.sound_load('lock.wav')
        self.new_mark = ResourceManager.sound_load('mark2.ogg')
        self.new_delete = ResourceManager.sound_load('delete2.ogg')
        self.new_locking = ResourceManager.sound_load('lock2.ogg')

    def collide(self):
        if self.face.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def state_change(self, mouse_action, sfx_state):
        self.muted = sfx_state
        if mouse_action != self.state:
            if self.muted == 0:
                if self.nonograma.Shop.is_item_purchased("New SFX"):
                    if mouse_action == 1:
                        self.new_mark.play()
                    elif mouse_action == 2:
                        self.new_locking.play()
                    elif mouse_action == 0:
                        self.new_delete.play()
                else:
                    if mouse_action == 1:
                        self.default_mark.play()
                    elif mouse_action == 2:
                        self.default_locking.play()
                    elif mouse_action == 0:
                        self.default_delete.play()
            self.state = mouse_action

    def draw(self, surface, scoll_prop, move):
        self.rect.x = int((surface.get_size()[0] / 2) + (self.x * (self.rect_size - self.spacing) - 200) * scoll_prop) + move[0]
        self.rect.y = int((surface.get_size()[1] / 2) + (self.y * (self.rect_size - self.spacing) - 100)* scoll_prop) + move[1]
        self.rect.width = math.ceil(self.rect_size * scoll_prop)
        self.rect.height =math.ceil(self.rect_size * scoll_prop)
        self.face.x = self.rect.center[0] - int((self.face_size / 2) * scoll_prop)
        self.face.y = self.rect.center[1] - int((self.face_size / 2) * scoll_prop)
        self.face.width = int(self.face_size * scoll_prop)
        self.face.height = int(self.face_size * scoll_prop)
        pygame.draw.rect(surface, Color.GRIS_PLOMO, self.rect)
        if self.state == 0:
            pygame.draw.rect(surface, Color.BLANCO, self.face)
        if self.state == 1:
            pygame.draw.rect(surface, Color.NEGRO, self.face)
        if self.state == 2:
            pygame.draw.rect(surface, Color.BLANCO, self.face)
            surface.blit(pygame.transform.scale(self.lock, (int(self.face_size * scoll_prop), int(self.face_size) * scoll_prop)), (self.rect.center[0] - int((self.face_size / 2) * scoll_prop), self.rect.center[1] - int((self.face_size / 2) * scoll_prop)))
        if self.state == 3:
            pygame.draw.rect(surface, Color.GRIS_CLARO, self.face)
        if self.state == 4:
            pygame.draw.rect(surface, Color.AZUL_CLARO, self.face)
        if self.state == 5:
            pygame.draw.rect(surface, Color.BLANCO, self.face)
            surface.blit(
                pygame.transform.scale(self.fallo, (int(self.face_size * scoll_prop), int(self.face_size) * scoll_prop)),
                (self.rect.center[0] - int((self.face_size / 2) * scoll_prop),
                 self.rect.center[1] - int((self.face_size / 2) * scoll_prop)))
