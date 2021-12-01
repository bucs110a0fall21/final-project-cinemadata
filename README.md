:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Movie Recommender
## CS 110 Final Project
### Fall, 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

[https://github.com/bucs110a0fall21/final-project-cinemadata](#)

<< [link to demo presentation slides](#) >>

### Team: CinemaData
#### Daniel Zheng, Wilson Huang, Kevin Wu

***

## Project Description *(Software Lead)*
This is a program that takes user input based on genre and using selected genres, sends a request to the an API for films that have the attributes given by the user. It displays the movies in a graphical interface and the user is able to click on the "More Info" button to get a detailed description of the movie as well as where to buy, stream, or display if the movie is currently in theaters.

***    

## User Interface Design *(Front End Specialist)*
* ![class diagram](assets/GUI%20First%20Page.png)
* Main Menu Screen
* Contains:
* Selection dropdown box
* Scrolling screen(scroll wheel is wish feature)
* Search button
* Remove button
* Selectable genres for the movie
* ![class diagram](assets/GUI%20Second%20Page.png)
* Second Screen (Recommended movies)
* Contains:
* Poster for movies
* Back button
* Select button
* Scrolling screen
* More info button
* ![class diagram](assets/GUI%20Third%20Page.png)
* Third Screen (Watchlist add-on)
* Contains:
* List of all the movies the user selected
* ![class diagram](assets/GUI%20Fourth%20Page%20(addon)%20(1).png)
* Fourth Screen (More info screen)
* Contains:
* Information gathered from API about specific movie
* Also includes the previous back and scroll wheel


***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * (pygame)
    * Pygame
        * Documentation:  https://www.pygame.org/docs/
        * This module is used to create the "view" or visuals of the project.
* Class Interface Design
    * Main Menu (Screen 1)
    ![class diagram](assets/Class_screen_1.jpg)
    * Search Results (Screen 2)
    ![class diagram](assets/Class_screen_2.jpg)
    * Movie Details (Screen 3)
    ![class diagram](assets/Class_screen_3.jpg)
* Classes
    * Main Menu
        * Models 
            * GenreList - creates a list of movie genres and determines their selection status
            * GenreChosen - list of selected genres and option to remove genre from list
            * Select - confirms selection of genres and add them to the list of selected genres
            * SearchButton - searches for movies based on selected genres
        * Controller
            * Search - creates the screen and determines what if a search can be made based on user input
        * View
            * Managed by pygame, TBD
    * Search Results (Screen 2)
        * Models 
            * BackButton - goes back to main menu
            * MoreInfoButton - changes screen to show more information on a movie (goes to screen 3)
            * SelectButton - adds movie to movie list
            * ScrollWheel - changes position of screen based on user input
            * MovieInfo - gets movie information for all recommended movies
        * Controller
            * Recommendations - creates screen 2 and determines if buttons are pressed, calls certain class methods depending on the button pressed
        * View
            * Managed by pygame, TBD
    * More Info Screen (Screen 3)
        * Models 
            * MoviePage - detailed data of selected movie
            * ScrollWheel - (same as screen 2)
            * BackButton - goes back to screen 2
        * Controller
            * ExpandedMovieInfo - creates page with movie's rating, description, poster, availability, etc. and checks to see if back button or scroll wheel are pressed
        * View
            * Managed by pygame, TBD
    
    

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* src
    * Button.py
    * Controller.py
    * APIrequest.py
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Kevin Wu

Integrated the button and APIrequest models into the GUI, completed scrolling feature, caught various bugs that came up during the development process, and cleaned up code where needed.

### Front End Specialist - Wilson Huang

Created the scrolling feature, main, second, and third screens code and GUIs. Worked with back-end to create the buttons. 

### Back End Specialist - Daniel Zheng

Created the Button and APIrequest classes, and helped implement the models into the GUI.

## Testing *(Software Lead)*
* Tested code each time a new feature was added and tested all features, so long as they were implemented, as per the ATP.
    * Example: Tested 'Exit' button prior to scrolling feature as scrolling feature had yet to been implemented, and tested 'Search' button by printing out data prior to second screen being implemented. In addition, code was tested to ensure that user input would not break the program.

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Open terminal, navigate to folder, and type 'python3 main.py' | Program starts and displays main screen |    |
|  2  | Hover mouse over program window and mousewheel up in main screen | Genre buttons in center move up  |    |
|  3  | Hover mouse over program window and mousewheel down in main screen |  Genre buttons in center move down  |    |
|  4  | Left click on center button(s) with genres in main screen  | Button appears on the left with respective genre, indicating genre is added to selection |    |
|  5  | Left click on button(s) with selected genre(s) on the left in main screen | Button disappears, indicating that genre has been removed from selection |    |
|  6  | Left click on 'Search' button in the bottom right, above the 'Exit' button  | Window changes to different screen showing list of movies with matching genres  |    |
|  7  | Left click on 'Back button in the bottom right, above the 'Exit' button  |  Returns to previous screen  |    |
|  8  | Left click on 'Exit' Button in the bottom right  |  Program closes  |    |