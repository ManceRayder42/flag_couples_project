import pygame
import screen


def main():
    pygame.init()
    print(screen.create_screen())



    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

main()