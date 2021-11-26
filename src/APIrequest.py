import json
import requests

class APIrequest:
    #This is the list of selected genres#
    #I made the genre list feature to be separate from the button class so that genre buttons wont each have a list on their own#
    #we would use this as a way to store selected genres and it would involve taking values from genre buttons

    def __init__(self, user_genres):
        '''
        saves the genre dictionary and the current list of selected genres to the object
        Args:
            self
            user_genres (list) - list of genre ids that will be sent to the api
        Return: none
        '''
        self.user_genres = user_genres
        self.genre_dictionary = self.getGenre()

    def apiRequest(self):
        '''
        searches for movies with the selected genres
        Args:
            self
        Return:
            raw_data (dict) converted search results from api
        '''
        start = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'with_genres': self.user_genres, 'language': 'en-US'}
        search_request = requests.get("https://api.themoviedb.org/3/discover/movie?", params=start)
        print(search_request.url)
        raw_data = json.loads(search_request.text)
        return raw_data

    def getGenre(self):
        '''
        gets data and creates a dictionary of all genres with their id as the key
        Args:
            self
        Return:
            all_genres (dict) dict of all genres
        '''
        all_genres = {}
        start = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'language' : 'en-US'}
        request = requests.get("https://api.themoviedb.org/3/genre/movie/list?", params=start)
        raw_list = json.loads(request.text)
        genres = raw_list['genres']
        length = len(genres)
        for i in range(length):
            genre_value = genres[i]['name']
            genre_key = genres[i]['id']
            all_genres[genre_key] = genre_value
        print(all_genres)
        return all_genres

    def getId(self):
        '''
        gets the list of dictionaries with each dictionary containing a genre's name and id
        Args:
            self
        Return:
            genre_id (list) list of dictionaries with genre names and ids
        '''
        start = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'language' : 'en-US'}
        request = requests.get("https://api.themoviedb.org/3/genre/movie/list?", params=start)
        raw_list = json.loads(request.text)
        genre_id = raw_list['genres']
        return genre_id

    def moviesGenres(self, list_of_ids):
        '''
        takes a list of genre ids and returns a list of genre names
        Args:
            self
            list_of_ids (list) list of genre ids
        Return:
            genre_list (list) list of genre names
        '''
        genre_list = []
        for id_number in list_of_ids:
            genre_list.append(self.genre_dictionary[id_number])
        return genre_list
