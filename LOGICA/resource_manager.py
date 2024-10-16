import os
import pygame

class ResourceManager:
    proyect_folder = os.path.dirname(__file__)

    resources_folder = os.path.join(os.path.dirname(proyect_folder), 'resources')
    levels_folder = os.path.join(os.path.dirname(proyect_folder), 'levels')

    @staticmethod
    def level_path(file_name):
        return os.path.join(ResourceManager.levels_folder, file_name)
    def image_load(self):
        None
    def sound_load(self):
        None
    def music_load(self):
        None