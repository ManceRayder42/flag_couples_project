import pygame

import consts


def background(screen):
    screen.fill(consts.BACKRND)
    pygame.display.flip()


def drew_bushes():
    pass

def drew_soldier():
    pass

def drew_flag():
    pass



def create_screen():
    screen = pygame.display.set_mode(
        (1400, 700))
    background(screen)
    return screen