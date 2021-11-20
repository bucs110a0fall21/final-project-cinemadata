import pygame
import sys
from src import Button
from src import APIrequest

class Controller:
    def __init__(self):
        super().__init__()
        self.width = 1080
        self.height = 720
        self.state = "MAIN"
        pygame.display.set_caption("SuggestCinema")  # Title of program
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface((self.width, self.height))
        self.font_name = pygame.font.get_default_font()
        self.screen.fill((130, 210, 220)) #background color
        self.genre_list = pygame.sprite.Group()
        self.clicked = False
        self.user_genre_list = []
        self.user_selected_ids = []

        #first screen
        raw_genre_list = APIrequest.APIrequest.get_id(self)

        # setting up buttons
        x_pos = 467
        y_pos = 150
        for genre in raw_genre_list:
            y_pos += 55
            self.genre_list.add(Button.Button(x_pos, y_pos, "assets/buttonicon.png", 1, genre['name'], genre['name'], genre['id']))
        self.exit_button = Button.Button(900, 600, "assets/buttonicon.png", 1, "Exit")
        self.search_button = Button.Button(900, 400, "assets/buttonicon.png", 1, "Search")
        self.first_screen_sprites = pygame.sprite.Group(tuple(self.genre_list) + (self.exit_button,) + (self.search_button,))

    def mainLoop(self):
        while self.state:
            if self.state == "MAIN":
                self.firstScreenLoop()
            elif self.state == "SECOND":
                self.secondScreenLoop()
            elif self.state == "THIRD":
                self.thirdScreenLoop()

    def firstScreenLoop(self):

        while self.state == "MAIN":
            #setting up static images
            logo = pygame.image.load('assets/screenlogo.png')
            self.screen.blit(logo, (277, 0))
            tmdb_logo = pygame.image.load('assets/moviedb.png')
            self.screen.blit(tmdb_logo, (800, 0))
            self.first_screen_sprites.draw(self.screen)
            #loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.rect.collidepoint(event.pos):
                        sys.exit()
                    elif self.search_button.rect.collidepoint(event.pos):
                        temp = APIrequest.APIrequest(self.user_selected_ids)
                        print(temp.apiRequest())
                        # self.state = "SECOND"
                    for button in self.genre_list:
                        if button.rect.collidepoint(event.pos):
                            if pygame.mouse.get_pressed()[0] == 1:
                                self.clicked = True
                                if button.label in self.user_genre_list:
                                    pass
                                else:
                                    self.user_genre_list.append(button.label)
                                    self.user_selected_ids.append(button.id)
                                    x_pos = 40
                                    y_pos = 40
                                    for i in self.user_selected_ids:
                                        y_pos += 55
                                        logo = pygame.image.load('assets/buttonicon.png')
                                        self.screen.blit(logo, (x_pos, y_pos))
                                        # self.genre_list.add(Button.Button(x_pos, y_pos, "assets/buttonicon.png", 1, genre['name'],genre['name'], genre['id']))
                                print(button.label)
                                print(button.id)
                                print(self.user_genre_list)
                                print(self.user_selected_ids)

            pygame.display.flip()

