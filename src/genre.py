class Genre:
    #This is the list of selected genres#
    def __init__(self):
        self.selected_genres = []
    #Adding and removing selected genres from the list
    def addRemove(self, genre, status):
        if status:
            self.selected_genres.append(genre)
        else:
            self.selected_genres.remove(genre)