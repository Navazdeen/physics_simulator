import pygame
import sys
import time
from src.shapes import Box, Cirle


class Main:
    WIDTH = 640
    HEIGHT = 480

    def __init__(self) -> None:
        pygame.init()
        self.display = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT), vsync=1)
        self.clock = pygame.time.Clock()

    def update(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.display.fill('black')
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    main = Main()
    main.update()
