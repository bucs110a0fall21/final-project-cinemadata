import pygame
import sys

from src import Button


class Controller:
    def __init__(self):
        # setting up pygame data/screen
        self.window_height = 720
        self.window_width = 1280
        self.state = "Main screen"
        pygame.init()
        pygame.display.set_caption("SuggestCinema")  # Title of program
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.Surface((self.window_width, self.window_height))
        self.screen.fill((130, 210, 220))
        logopng = pygame.image.load('assets/screenlogo.png')  # loading logo on screen
        self.screen.blit(logopng, (377, 0))
        databasepng = pygame.image.load('assets/moviedb.png')  # loading logo on screen
        self.screen.blit(databasepng, (1000, 600))

        self.select_button = Button.Button(10, 10, "assets/selectbutton.png", 1)

    def mainLoop(self):
        while self.state:
            if self.state == "Main screen":
                self.gameLoop()
            elif self.state == "Second screen":
                self.gameLoop()
            elif self.state == "Third screen":
                self.gameLoop()

    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.gameEventLoop()
            # pygame.display.get_surface()
            # pygame.display.update()

    def gameEventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.select_button
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move("U")
