import json
import requests

class Genre:
    #This is the list of selected genres#
    #I made the genre list feature to be separate from the button class so that genre buttons wont each have a list on their own#
    #we would use this as a way to store selected genres and it would involve taking values from genre buttons

    def __init__(self):
        self.selected_genres = []
        self.all_genres = self.genreList()
        self.all_ids = self.genreId()
    #Adding and removing selected genres from the list
    def apiRequest(self):
        payload = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'language' : 'en-US'}
        genreRequest = requests.get("https://api.themoviedb.org/3/genre/movie/list?", params=payload)
        conversion = json.loads(genreRequest.text)
        return conversion

    def genreList(self):
        conversion = self.apiRequest()
        genreDicts = conversion['genres']
        allGenres = []
        for genre in genreDicts:
            allGenres.append(genre['name'])
        return allGenres

    def genreId(self):
        conversion = self.apiRequest()
        genreDicts = conversion['id']
        allIds = []
        for genre in genreDicts:
            allIds.append(genre['name'])
        return allIds

    def addRemove(self, genre, status):
        if status:
            self.selected_genres.append(genre)
        else:
            self.selected_genres.remove(genre)