import pygame
from button import Button
import sys
from INTERFAZ.resource_manager import ResourceManager
import Color
from LOGICA.nonograma import Nonograma


class MainMenu:
    def __init__(self):
        self.nonograma = Nonograma()
        self.title_font = pygame.font.Font(None, 74)
        self.diff_button = Button(310, 400, 'play_button')
        self.create_button = Button(490, 400, 'create_button')
        self.shop_button = Button(670, 400, 'shop_button')
        self.exit_button = Button(850, 400, 'exit_button')
        self.menu_image = ResourceManager.image_load('main_menu.png')

    def arrange_buttons(self):
        nonograma = Nonograma()
        if nonograma.Shop.is_item_purchased("Level Creator"):
            x_positions = [310, 490, 670, 850]
        else:
            x_positions = [370, 550, 730]

        self.diff_button.update_position(x_positions[0], 400)
        if nonograma.Shop.is_item_purchased("Level Creator"):
            self.create_button.update_position(x_positions[1], 400)
        self.shop_button.update_position(x_positions[-2], 400)
        self.exit_button.update_position(x_positions[-1], 400)

    def draw(self, surface):
        surface.blit(self.menu_image, self.menu_image.get_rect())
        self.arrange_buttons()
        self.diff_button.draw(surface)
        if self.nonograma.Shop.is_item_purchased("Level Creator"):
            self.create_button.draw(surface)
        self.shop_button.draw(surface)
        self.exit_button.draw(surface)

    def handle_events(self, events):
        if self.diff_button.click_event(events):
            return 'levels'
        elif self.exit_button.click_event(events):
            pygame.quit()
            sys.exit()
        elif self.shop_button.click_event(events):
            ResourceManager.music_load("sans.wav")
            return 'shop'
        elif (
                self.create_button.click_event(events)
                and Nonograma().Shop.is_item_purchased("Level Creator")
        ):
            return 'editor_levels'
        return None
