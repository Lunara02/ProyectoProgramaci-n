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