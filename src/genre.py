class Genre:
    def __init__(self):
        self.selected_genres = []
    
    def addRemove(self, genre, status):
        if status:
            self.selected_genres.append(genre)
        else:
            self.selected_genres.remove(genre)