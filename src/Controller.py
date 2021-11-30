import pygame
import sys
from src import Button
from src import APIrequest
from src import APIproxy
class Controller:
    def __init__(self, tempdir):
        super().__init__()
        self.width = 1080
        self.height = 720
        self.state = "MAIN"
        pygame.display.set_caption("SuggestCinema")  # Title of program
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface((1080, 1440))
        self.font_name = pygame.font.get_default_font()
        self.screen.fill((130, 210, 220)) #background color
        self.genre_list = pygame.sprite.Group()
        self.user_genre_buttons = pygame.sprite.Group()
        self.user_genre_list = []
        self.user_selected_ids = []
        self.tempdir = tempdir
        #first screen
        raw_genre_list = APIrequest.APIrequest.get_id(self)
        # setting up buttons
        x_pos = 467
        y_pos = 0
        for genre in raw_genre_list:
            y_pos += 55
            self.genre_list.add(Button.Button(x_pos, y_pos, "assets/buttonicon.png", 1, genre['name'], genre['name'], genre['id']))
        self.exit_button = Button.Button(900, 600, "assets/buttonicon.png", 1, "Exit")
        self.search_button = Button.Button(900, 400, "assets/buttonicon.png", 1, "Search")
        self.back_button = Button.Button(900, 500, "assets/buttonicon.png", 1, "Back")
        self.logo = pygame.image.load('assets/screenlogo.png')
        self.tmdb_logo = pygame.image.load('assets/tmdblogo.png')
        self.first_screen_sprites = pygame.sprite.Group(tuple(self.genre_list) + (self.exit_button,) + (self.search_button,))

        #second screen
        self.second_screen_sprites = pygame.sprite.Group((self.exit_button,) + (self.back_button,))

    def mainLoop(self):
        while self.state:
            if self.state == "MAIN":
                self.firstScreenLoop()
            elif self.state == "SECOND":
                self.secondScreenLoop()
            elif self.state == "THIRD":
                self.thirdScreenLoop()

    def firstScreenLoop(self):
        x_pos = 15
        y_pos = 200
        while self.state == "MAIN":
            y_offset = 0
            #checking for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #scrolling
                    if event.button == 4:
                        y_offset += 15
                    if event.button == 5:
                        y_offset -= 15
                    #exit button
                    if self.exit_button.rect.collidepoint(event.pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            sys.exit()
                    #search button
                    elif self.search_button.rect.collidepoint(event.pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            self.state = "SECOND"
                    #center genre buttons
                    for button in self.genre_list:
                        if button.rect.collidepoint(event.pos) and pygame.mouse.get_pressed()[0] == 1:
                            if button.label in self.user_genre_list:
                                pass
                            elif button not in self.user_genre_buttons:
                                button_var = Button.Button(x_pos, y_pos, 'assets/buttonicon.png', 1, button.label, button.label, button.id)
                                self.user_genre_buttons.add(button_var)
                                self.user_genre_list.append(button.label)
                                self.user_selected_ids.append(button.id)
                                # printing for testing purposes
                                print(self.user_genre_list)
                                print(self.user_selected_ids)
                    #left side buttons
                    y_pos = 200
                    for button in self.user_genre_buttons:
                        if button.rect.collidepoint(event.pos) and pygame.mouse.get_pressed()[0] == 1:
                            button.kill()
                            self.user_genre_list.remove(button.label)
                            self.user_selected_ids.remove(button.id)
                            # printing for testing purposes
                            print(self.user_genre_list)
                            print(self.user_selected_ids)
                        else:
                            button.rect.y = y_pos
                            y_pos += 55


            #update
            self.screen.fill((130, 210, 220))
            self.screen.blit(self.logo, (180, 0))
            self.screen.blit(self.tmdb_logo, (850, 20))
            for button in self.genre_list:
                button.update(y_offset)
            self.first_screen_sprites.draw(self.screen)
            self.user_genre_buttons.draw(self.screen)

            #draw
            pygame.display.update()

    def secondScreenLoop(self):
        movie_data = APIrequest.APIrequest(self.user_selected_ids)
        results = movie_data.apiRequest()
        print(movie_data.apiRequest())
        movie_data.getPosters(results, f'assets/{self.tempdir}/')
        while self.state == "SECOND":
            #check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.rect.collidepoint(event.pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            sys.exit()
                    if self.back_button.rect.collidepoint(event.pos):
                        if pygame.mouse.get_pressed()[0] == 1:
                            self.state = "MAIN"


            #update
            self.screen.fill((130, 210, 220))
            self.screen.blit(self.logo, (467, 0))
            self.screen.blit(self.tmdb_logo, (850, 20))
            self.second_screen_sprites.draw(self.screen)

            #redraw
            pygame.display.update()

