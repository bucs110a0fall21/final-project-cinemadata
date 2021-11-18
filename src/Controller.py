# Setting up pygame/window --------------------------------
import pygame
import sys
import random
from pygame.locals import *
from src import Button


class Controller:
    def __init__(self):
        # ---------------------------------
        self.running, self.playing = True, False
        self.mouse_click = False
# creating the background ---------------------------------
        self.window_height = 720
        self.window_width = 1280
        self.state = "Main screen"
        pygame.init()
        pygame.display.set_caption("SuggestCinema")  # Title of program
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.Surface((self.window_width, self.window_height))
        self.font_name = pygame.font.get_default_font()
        self.screen.fill((130, 210, 220)) #RGB colors

        logopng = pygame.image.load('assets/screenlogo.png')  # loading logo on screen
        self.screen.blit(logopng, (377, 0))

        databasepng = pygame.image.load('assets/moviedb.png')
        self.screen.blit(databasepng, (1000, 0))

        self.searchbutton = Button.Button(100, 109, "assets/searchbutton.png", 1, 'search')
        searchbutton = pygame.image.load('assets/searchbutton.png')
        self.screen.blit(searchbutton, (1050, 600))

        buttonicon = Button.Button(100, 109, "assets/buttonicon.png", 1, 'Genre')
        self.screen.blit(buttonicon.image, (10, 100))

        self.buttonicon = Button.Button(100, 109, "assets/buttonicon.png", 1, 'Genre')
        self.screen.blit(self.buttonicon.image, (10, 200))

        self.buttonicon = Button.Button(100, 109, "assets/buttonicon.png", 1, 'genre')
        buttonicon = pygame.image.load('assets/buttonicon.png')
        self.screen.blit(buttonicon, (10, 300))

        image = pygame.image.load('assets/buttonicon.png')
        sprite = pygame.sprite.Sprite()
        sprite.image = image
        sprite.rect = image.get_rect()

        font = pygame.font.SysFont('Sans', 40)
        text = font.render('Genre 1', True, (255, 255, 255))
        # sprite.image.blit(text, sprite.rect)
        self.screen.blit(text, (50, 150))
        group = pygame.sprite.Group()
        group.add(sprite)
        group.draw(self.screen)
        pygame.display.flip()

        position = pygame.mouse.get_pos()
        print(position)

        # Attempting to add/create 3 buttons
        # self.buttons = pygame.sprite.Group()
        # buttons_num = 3
        #
        # for i in range(buttons_num):
        #     x = random.randrange(100, 400)
        #     y = random.randrange(100, 400)
        #     self.buttons.add(Button.Button("Genre", x, y, 'assets/selectbutton'))
            # self.all_sprites = pygame.sprite.Group(self.buttons)

    def mainLoop(self):
        while self.state:
            if self.state == "Main screen":
                self.gameLoop()
            elif self.state == "Second screen":
                self.gameLoop()
            elif self.state == "Third screen":
                self.gameLoop()

    def gameLoop(self):
        # while self.playing:
        #     self.check_events()
        #     if self.start_key:
        #         self.playing = True
            # self.display.fill(self.BLACK) #resets the canvas
            # self.window.blit(self.display, (0,0))
            # pygame.display.update()
            # self.resetKeys()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.check_events()

            pygame.display.get_surface()
            pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if player clicks x close window
                self.running, self.playing = False, False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.key == pygame.MOUSEBUTTONDOWN:
                    self.start_key = True
                # self.select_button
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move("U")
    def resetKeys(self):
        self.start_key = False