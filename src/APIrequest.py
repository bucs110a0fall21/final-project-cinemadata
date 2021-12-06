import json
import requests
from src import APIproxy
class APIrequest:
    #This is the list of selected genres#
    #I made the genre list feature to be separate from the button class so that genre buttons wont each have a list on their own#
    #we would use this as a way to store selected genres and it would involve taking values from genre buttons

    def __init__(self, user_genres):
        '''
        saves the current list of selected genres to the object
        Args:
            self
            (list) user_genres, list of genre ids that will be sent to the api
        Return: none
        '''
        self.user_genres = user_genres

    def apiRequest(self):
        '''
        searches for movies with the selected genres
        Args:
            self
        Return:
            (dict) raw_data, converted search results from api
        '''
        payload = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'with_genres': self.user_genres, 'language': 'en-US'}
        search_request = requests.get("https://api.themoviedb.org/3/discover/movie?", params=payload)
        # print(search_request.url)
        raw_data = json.loads(search_request.text)
        return raw_data

    # def get_genre(self):
    #     '''
    #     gets data and creates a list of all genres
    #     Args:
    #         self
    #     Return:
    #         (list)all_genres, list of all genres
    #     '''
    #     all_genres = []
    #     payload = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'language' : 'en-US'}
    #     request = requests.get("https://api.themoviedb.org/3/genre/movie/list?", params=payload)
    #     raw_list = json.loads(request.text)
    #     genres = raw_list['genres']
    #     length = len(genres)
    #     for i in range(length):
    #         temp = genres[i]['name']
    #         all_genres.append(temp)
    #     print(genres)
    #     print(all_genres)
    #     return all_genres

    def get_id(self):
        '''
        gets the list of dictionaries with each dictionary containing a genre's name and id
        Args:
            self
        Return:
            (list) genre_id, list of dictionaries with genre names and ids
        '''
        payload = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'language' : 'en-US'}
        request = requests.get("https://api.themoviedb.org/3/genre/movie/list?", params=payload)
        raw_list = json.loads(request.text)
        genre_id = raw_list['genres']
        # print(genre_id)
        return genre_id
    
    def get_posters(self, movie_results, tempdir):
        '''
        Retrieves the poster image from the API and saves it to the temporary file
        Args:
            self
            (list) movie_results
            (str) tempdir
        Return:
            None
        '''
        counter = 0 
        for movie in movie_results['results']:
            poster = movie['poster_path']
            url = 'https://image.tmdb.org/t/p/w500' + poster
            APIproxy.MoviePoster(url, tempdir + f'sample{counter}.jpg')
            counter += 1

    def get_providers(self, movie_id):
        """
        Retrieves the providers that are streaming the movie
        args: (str) movie_id
        return: (str) output
        """
        payload = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'language' : 'en-US'}
        request = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?", params=payload)
        raw_list = json.loads(request.text)
        if raw_list['results'] == {}:
            pass
        else:
            providers = raw_list['results']
            try:
                output = providers['US']['flatrate'][0]['provider_name']
            except KeyError:
                try:
                    output = providers['US']['ads'][0]['provider_name']
                except KeyError:
                    output = "None"
            #for testing
            # print(providers)
            # print(request.url)
            return output