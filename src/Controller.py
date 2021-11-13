import pygame

from src import Button

class Controller:
    def __init__(self):
        #setting up pygame data/screen
        self.window_height = 600
        self.window_width = 900
        self.state = "Main screen"
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_height, self.window_width))
        self.background = pygame.Surface((self.window_height, self.window_width))
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
            self.gameEventLoop()
            self.display.update()
    def gameEventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.select_button
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move("U")


