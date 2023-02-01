import pygame, sys
from settings import *
from editor import Editor


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.editor = Editor()

    def run(self):
        while True:
            tickrate = self.clock.tick() / 1000

            self.editor.run(tickrate)
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
