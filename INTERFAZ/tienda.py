from LOGICA.nonograma import Nonograma
import pygame
from INTERFAZ.resource_manager import ResourceManager
from INTERFAZ.button import Button
import Color


class Tienda():
    def __init__(self):
        self.title_font = pygame.font.Font(None, 74)
        self.item_font = pygame.font.Font("Comic Sans MS.ttf", 20)
        self.shop = ResourceManager.image_load('shop.png')
        self.nonograma = Nonograma()
        self.buy_buttons = []
        self.items = self.nonograma.Shop.items
        for i, item in enumerate(self.items):
            button_x = 100 + (i % 3) * 247
            button_y = 100 + (i // 3) * 220
            button_image = f'buy_button{i + 1}'
            self.buy_buttons.append(Button(button_x, button_y, button_image, item))
        for i, item in enumerate(self.items):
            if item in self.nonograma.Shop.purchased_items:
                self.buy_buttons[i].image_name = 'sold'
                self.buy_buttons[i].image = ResourceManager.image_load('sold.png')

        self.exit = Button(1190, 640, 'back_button')

    def draw(self, surface):
        surface.blit(self.shop, self.shop.get_rect())
        self.exit.draw(surface)

        for i, button in enumerate(self.buy_buttons):
            button.draw(surface)
            item = self.items[i]
            item_text = self.item_font.render(f"{item.name} - {item.price}$", True, Color.BLANCO)
            item_rect = item_text.get_rect(center=(button.rect.centerx, button.rect.centery + 100))
            surface.blit(item_text, item_rect.topleft)

        fuentes = pygame.font.SysFont('Comic Sans MS.ttf', 30)
        time_text = fuentes.render(f"${self.nonograma.Shop.money}", True, Color.BLANCO)
        surface.blit(time_text, (1120, 65))

    def handle_events(self, events):
        for index, button in enumerate(self.buy_buttons):
            if button.click_event(events):
                item = self.items[index]
                if item not in self.nonograma.Shop.purchased_items:
                    if self.nonograma.Shop.buy(index):
                        print(f"Comprado: {item.name}")
                        self.buy_buttons[index].image_name = 'sold'
                        ResourceManager.sound_load("buy.wav").play()
                        self.buy_buttons[index].image = ResourceManager.image_load('sold.png')
                        return
                else:
                    print("Este artículo ya ha sido comprado.")
                return

        if self.exit.click_event(events):
            ResourceManager.stop_music()
            ResourceManager.music_load("main.wav")
            return 'main_menu'

        return None
