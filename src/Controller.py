from src import Button
import pygame
import sys

class Controller:
    def __init__(self):
        #setting up pygame data/screen
        self.window_height = 600
        self.window_width = 600
        self.state = "Main screen"
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_height, self.window_width))
        self.background = pygame.Surface((self.window_height, self.window_width))
        self.background.fill([173, 216, 230])
        self.select_button = Button.Button(10, 10, "assets/selectbutton.png", 1)

    def mainloop(self):
        while self.state:
            if self.state == "Main screen":
                self.gameloop()
            elif self.state == "Second screen":
                self.gameloop()
            elif self.state == "Third screen":
                self.gameloop()

    def gameloop(self):
        while self.state == "Main screen":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.select_button.update(self.select_button.rect.x, self.select_button.rect.x, False)
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()