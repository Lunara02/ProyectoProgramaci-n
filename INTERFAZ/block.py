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

        