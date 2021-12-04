import pygame
import sys
from src import Button
from src import APIrequest
class Controller:
    def __init__(self, tempdir):
        """
        Creates all objects in the program
        args: (str) tempdir
        return: None
        """
        super().__init__()
        self.width = 1080
        self.height = 720
        self.state = "MAIN"
        pygame.display.set_caption("SuggestCinema")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface((1080, 14400))
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
        #first screen
        self.first_screen_sprites = pygame.sprite.Group(tuple(self.genre_list) + (self.exit_button,) + (self.search_button,))
        #second screen
        self.second_screen_sprites = pygame.sprite.Group((self.exit_button,) + (self.back_button,))

    def mainLoop(self):
        """
        Checks for the current state of the program, and changes subloops in respect to the state.
        args: None
        return: None
        """
        while self.state:
            if self.state == "MAIN":
                self.firstScreenLoop()
            elif self.state == "SECOND":
                self.secondScreenLoop()
            elif self.state == "THIRD":
                self.thirdScreenLoop()

    def firstScreenLoop(self):
        """
        Subloop for the first screen of the program, and runs when the game state is "MAIN"
        args: None
        return: None
        """
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
                    if self.exit_button.rect.collidepoint(event.pos) and pygame.mouse.get_pressed()[0] == 1:
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
            self.screen.blit(self.logo, (150, 0))
            self.screen.blit(self.tmdb_logo, (850, 20))
            for button in self.genre_list:
                button.update(y_offset)
            self.first_screen_sprites.draw(self.screen)
            self.user_genre_buttons.draw(self.screen)

            #draw
            pygame.display.update()

    def secondScreenLoop(self):
        """
        Subloop for the second screen of the program, and runs when the game state is "SECOND", displays movie data
        based on chosen genres from the first screen. Movie data is blitted onto the background. Background moves
        up and down on y-axis based on scroll wheel input.
        args: None
        return: None
        """
        #retrieving movie data
        movie_data = APIrequest.APIrequest(self.user_selected_ids)
        results = movie_data.apiRequest()
        results_list = results['results']
        provider_list = []
        for movie in results_list:
            temp_movie_id = movie['id']
            temp_providers = APIrequest.APIrequest.get_providers(self, temp_movie_id)
            if temp_providers == None:
                temp_providers = "None"
            else:
                pass
            provider_list.append(temp_providers)
        # print(provider_list)
        directory = f'assets/{self.tempdir}/'
        movie_data.get_posters(results, directory)
        y_position = 0
        while self.state == "SECOND":
            #check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.rect.collidepoint(event.pos) and pygame.mouse.get_pressed()[0] == 1:
                            sys.exit()
                    if self.back_button.rect.collidepoint(event.pos) and pygame.mouse.get_pressed()[0] == 1:
                            self.state = "MAIN"
                    if event.button == 4:
                        y_position = min(y_position + 150, 0)
                    if event.button == 5:
                        y_position = max(y_position -150, -5500)


            #update
            title_font = pygame.font.SysFont('arial', 30, True)
            standard_font = pygame.font.SysFont('arial', 15)
            y_pos = 0
            x_pos = 200
            poster_y_pos = 0
            accum = 0

            self.background.fill((130, 210, 220))
            self.background.blit(self.logo, (850, 0))
            self.background.blit(self.tmdb_logo, (850, 200))
            #movie data
            for movie in results_list:
                items = []
                temp_title = movie['title']
                temp_description = movie['overview']
                temp_date = movie['release_date']
                temp_avg_vote = movie['vote_average']
                temp_vote_count = movie['vote_count']
                temp_provider = provider_list[accum]
                accum += 1
                convert_str = [temp_description, temp_date, temp_avg_vote, temp_vote_count, temp_provider]
                for i in convert_str:
                    str(i)
                date = f'Release Date: {temp_date}'
                avg_vote = f'Average Rating: {temp_avg_vote} / 10'
                vote_count = f'Vote Count: {temp_vote_count}'
                provider = f'Streaming On: {temp_provider}'
                #order temp_items is in determines order on screen
                temp_items = [
                    date,
                    avg_vote,
                    vote_count,
                    provider,
                    temp_description
                ]
                title = title_font.render(temp_title, True, (0, 0, 0))
                for i in temp_items:
                    temp = standard_font.render(i, True, (0, 0, 0))
                    items.append(temp)
                self.background.blit(title, (x_pos, y_pos))
                y_pos += 40
                for item in items:
                    self.background.blit(item, (x_pos, y_pos))
                    y_pos += 20
                y_pos += 160
                poster = pygame.image.load(f'assets/{self.tempdir}/sample{accum-1}.jpg')
                poster = pygame.transform.scale(poster, (167, 250))
                self.background.blit(poster, (0, poster_y_pos))
                poster_y_pos += 300
            self.screen.blit(self.background, (0, y_position))
            self.second_screen_sprites.draw(self.screen)

            #redraw
            pygame.display.update()

    def thirdScreenLoop(self):
        """
        Subloop for the third screen of the program, and runs when the game state is "THIRD", displays more information about the movie chosen from the second screen.
        args: None
        return: None
        """
        while self.state == "THIRD":
            #check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #update
            self.screen.fill((130, 210, 220))
            self.screen.blit(self.logo, (467, 0))
            self.screen.blit(self.tmdb_logo, (850, 20))

            #redraw
            pygame.display.update()

