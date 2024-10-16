import pygame

def left_click(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return True
    return False

def right_click(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                return True
    return False