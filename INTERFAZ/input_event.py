import pygame

def left_click(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return True
    return False

def left_hold():
    if pygame.mouse.get_pressed()[0] == 1:
        return True
    return False

def right_click(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                return True
    return False

def right_hold():
    if pygame.mouse.get_pressed()[2] == 1:
        return True
    return False

def scroll_up(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                return True
    return False

def scroll_down(events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:
                return True
    return False

def esc_press(events):
    for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
    return False
