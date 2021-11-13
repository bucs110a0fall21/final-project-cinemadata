from src import Button
import pygame

class Controller:
    def __init__(self):
        #setting up pygame data/screen
        self.window_height = 600
        self.window_width = 900
        self.state = "Main screen"
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_height, self.window_width))
        self.background = pygame.Surface((self.window_height, self.window_width))
        self.background.fill(173, 216, 230)
        self.select_button = button.Button(x, y, "assets/selectbutton.png")

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
            self.gameEventLoop()
            self.Button.update()



