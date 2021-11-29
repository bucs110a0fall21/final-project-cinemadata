from src import APIrequest
from src import Button
import pygame
import sys

#APIrequest (movies) test
x = APIrequest.APIrequest(['28'])
print(x.apiRequest())

#APIrequest (genres) test
user_genres = []
y = APIrequest.APIrequest(user_genres)
final = y.getId()
print(final)
print(type(final))

# #dictionary
# for i in final:
#     print(type(i))
#     x = i['id']
#     print(type(x))

#genre id list conversion test
y = x.apiRequest()
print(y)
print(y['results'][0]['title'])
print(y['results'][0]['genre_ids'])
print(x.moviesGenres(y['results'][0]['genre_ids']))


###old api request model in case we need it for reference###
# import json
# import requests

# class MovieFinder:
#     def __init__(self, list):
#         self.selected_genres = list
#         self.movies_found = self.searchForMovies()
#         self.movies_data = []

#     def searchForMovies(self):
#         payload = {'api_key': 'ae2a71b3aac0b67e745c46b2ff92ecb9', 'with_genres' : self.selected_genres, 'language' : 'en-US'}
#         search_request = requests.get("https://api.themoviedb.org/3/discover/movie?", params=payload)
#         print(search_request.url)
#         conversion = json.loads(search_request.text)
#         return conversion

#     def searchMovieData(self, movie_name):
#         movie_list = self.movies_found['results']
#         movie_name = movie_name.lower()
#         for movie in movie_list:
#             name_in_list = movie['original_title']
#             name_in_list = name_in_list.lower()
#             if movie_name == name_in_list:
#                 self.movies_data.append(movie)

