import json
import requests

class APIrequest:
    #This is the list of selected genres#
    #I made the genre list feature to be separate from the button class so that genre buttons wont each have a list on their own#
    #we would use this as a way to store selected genres and it would involve taking values from genre buttons

    def __init__(self, user_genres):
        self.user_genres = user_genres

    def apiRequest(self):
        start = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'with_genres': self.user_genres, 'language': 'en-US'}
        search_request = requests.get("https://api.themoviedb.org/3/discover/movie?", params=start)
        print(search_request.url)
        raw_data = json.loads(search_request.text)
        return raw_data

    def get_genre(self):
        all_genres = []
        start = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'language' : 'en-US'}
        request = requests.get("https://api.themoviedb.org/3/genre/movie/list?", params=start)
        raw_list = json.loads(request.text)
        genres = raw_list['genres']
        length = len(genres)
        for i in range(length):
            temp = genres[i]['name']
            all_genres.append(temp)
        print(genres)
        return all_genres

    def get_id(self):
        start = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'language' : 'en-US'}
        request = requests.get("https://api.themoviedb.org/3/genre/movie/list?", params=start)
        raw_list = json.loads(request.text)
        genre_id = raw_list['genres']
        print(genre_id)
        return genre_id
