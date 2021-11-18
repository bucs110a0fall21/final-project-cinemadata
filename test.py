import pygame
import sys
from src import Button
from src import List


###Tests Part 1####
# t = True

# # test to see if I can change the values
# pygame.init()
# pygame.display.set_mode((600, 600))
# testButton = Button.Button(3, 4, "assets/class_diagram.jpg", 1)
# print(testButton.rect.x, testButton.rect.y)
# # test to see if I can change the values

# #test to see if adding and removing genres to the list(genre class) works

# testButton.genreButton("Action")    #gives the test button a genre       
# testGenre = List.Genre()   #creates a genre list

# testButton.selected()   #makes the status of test button as selected
# testGenre.addRemove(testButton.genre, testButton.status)    #adds genre to list
# print(testGenre.selected_genres)    #print out list

# testButton.selected()   #makes the status of test button unselected
# testGenre.addRemove(testButton.genre, testButton.status)    #removes genre from list
# print(testGenre.selected_genres)    #prints out list

# # test to see if the list works
# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         sys.exit()
# #test to see if continous list works
# while True:
#     state = input("selected?")
#     if state == 'true' or state == 'True':
#         #there is a problem with having an else here because 
#         #that would continously remove the genre if false which results in an error
#         #so we want base it only if it is true that the button was clicked on
#         #the condition above is just placeholder
#         testButton.selected()
#         testGenre.addRemove(testButton.genre, testButton.status)
#         print(testGenre.selected_genres)
# #test to see if continous list works

# ###Tests part 2(api requests)###
# y = List.Genre()
# print(y.all_genres)
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

        self.buttonicon = Button.Button(500, 300, "assets/buttonicon.png", 1, 'Genre')
        self.screen.blit(self.buttonicon.image, (500, 300))
        self.buttonicon = Button.Button(500, 350, "assets/buttonicon.png", 1, 'Genre')
        self.screen.blit(self.buttonicon.image, (500, 350))
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
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.buttonicon.update(100,200,False)
                    if(event.key == pygame.K_DOWN):
                        self.buttonicon.update(100,300,False)


            # update the screen
            self.screen.fill((130, 210, 220)) #RGB colors

            logopng = pygame.image.load('assets/screenlogo.png')  # loading logo on screen
            self.screen.blit(logopng, (377, 0))

            databasepng = pygame.image.load('assets/moviedb.png')
            self.screen.blit(databasepng, (1000, 0))
            self.screen.blit(self.buttonicon.image, (self.buttonicon.rect.x, self.buttonicon.rect.y))
            pygame.display.flip()

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

def main():
	pygame.init()
	team = {"lead": "Kevin Wu", "backend": "Daniel Zheng", "frontend": "Wilson Huang"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:", team["frontend"])

	main_window = Controller()
	main_window.mainLoop()
	# while controller.running:    # while the program is running(self.playing is true) it will run gameLoop
	# 	controller = Controller()
	# 	controller.gameLoop()
main()