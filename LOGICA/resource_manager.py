import os
import pygame

class ResourceManager:
    proyect_folder = os.path.dirname(__file__)

    resources_folder = os.path.join(os.path.dirname(proyect_folder), 'resources')
    levels_folder = os.path.join(os.path.dirname(proyect_folder), 'levels')

    @staticmethod
    def level_path(file_name):
        return os.path.join(ResourceManager.levels_folder, file_name)

    @staticmethod
    def image_load(file_name):
        get_image_path = os.path.join(ResourceManager.resources_folder, file_name)
        try:
            return pygame.image.load(get_image_path)
        except pygame.error as e:
            print(f"No se pudo cargar la imagen {file_name}: {e}")
            return None

    def sound_load(self):
        None
    def music_load(self):
        None