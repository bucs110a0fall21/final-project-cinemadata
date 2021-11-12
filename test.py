import pygame
import sys
from src import button
from src import genre

t=True

# test to see if I can change the values
pygame.init()
pygame.display.set_mode((600,600))
testButton = button.Button(3, 4, "assets/class_diagram.jpg")
print(testButton.x, testButton.y)
# test to see if I can change the values

#test to see if adding and removing genres to the list(genre class) works

testButton.genreButton("Action")    #gives the test button a genre       
testGenre = genre.Genre()   #creates a genre list

testButton.selected()   #makes the status of test button as selected
testGenre.addRemove(testButton.genre, testButton.status)    #adds genre to list
print(testGenre.selected_genres)    #print out list

testButton.selected()   #makes the status of test button unselected
testGenre.addRemove(testButton.genre, testButton.status)    #removes genre from list
print(testGenre.selected_genres)    #prints out list

# test to see if the list works
for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
#test to see if continous list works
while True:
    state =input("selected?")
    if state == 'true' or state == 'True':
        #there is a problem with having an else here because 
        #that would continously remove the genre if false which results in an error
        #so we want base it only if it is true that the button was clicked on
        #the condition above is just placeholder
        testButton.selected()
        testGenre.addRemove(testButton.genre, testButton.status)
        print(testGenre.selected_genres)
#test to see if continous list works

