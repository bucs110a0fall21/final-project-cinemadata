class Genre:
    #This is the list of selected genres#
    #I made the genre list feature to be separate from the button class so that genre buttons wont each have a list on their own#
    #we would use this as a way to store selected genres and it would involve taking values from genre buttons

    def __init__(self):
        self.selected_genres = []
    #Adding and removing selected genres from the list
    def addRemove(self, genre, status):
        if status:
            self.selected_genres.append(genre)
        else:
            self.selected_genres.remove(genre)