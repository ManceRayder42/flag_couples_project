import pygame

import consts


def background(screen):
    screen.fill(consts.BACKRND)
    pygame.display.flip()

def create_screen():
    screen = pygame.display.set_mode(
        (1200, 800))
    background(screen)
    return screen