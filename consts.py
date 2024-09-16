import pygame

EXPLOSION = pygame.image.load("explotion.png")
FLAG = pygame.image.load("flag.png")
GRASS = pygame.image.load("grass.png")
MINE = pygame.image.load("mine.png")
SOLDIER = pygame.image.load("soldier.png")
GREEN_BACKGROUND = (2, 48, 32)

# SOLDIER_SIZE = pygame.transform.scale(SOLDIER, (12, 12))
# FLAG_SIZE = pygame.transform.scale(FLAG,(12,4))
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700

MATRIX_WIDTH = 50
MATRIX_HEIGHT = 25

SQUARE_SIZE = SCREEN_WIDTH / MATRIX_WIDTH
