import pygame
import sys

from src import Button

class Controller:
    def __init__(self):
        #setting up pygame data/screen
        pygame.init()
        self.window_height = 600
        self.window_width = 600
        self.state = "Main screen"
        self.screen = pygame.display.set_mode((self.window_height, self.window_width))
        self.background = pygame.Surface((self.window_height, self.window_width))
        self.background.fill([173, 216, 230])
        self.select_button = Button.Button(10, 10, "assets/selectbutton.png", 1)
        self.background.fill((173, 216, 230))
        self.select_button = Button.Button(100, 100, "assets/selectbutton.png", 1)

    def mainLoop(self):
        while self.state:
            if self.state == "Main screen":
                self.gameLoop()
            elif self.state == "Second screen":
                self.gameLoop()
            elif self.state == "Third screen":
                self.gameLoop()

    def gameLoop(self):
        while self.state == "Main screen":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.select_button.update(self.select_button.rect.x, self.select_button.rect.x, False)
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
            self.gameEventLoop()
            self.display.update()
    def gameEventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.select_button
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
