import pygame
from screen_manager import ScreenManager
from LOGICA.resource_manager import ResourceManager


def main():
    pygame.init()
    imagen1 = ResourceManager.image_load('insano.png')
    pygame.display.set_icon(imagen1)
    screen_size = (1280, 720)
    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    pygame.display.set_caption("Main menu")
    screen_manager = ScreenManager()
    running = True
    while running:

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        screen_manager.handle_events(events)
        screen_manager.draw(screen)
        pygame.display.flip()

    pygame.quit()


main()