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
final = y.get_id()
print(final)
print(type(final))

#dictionary
for i in final:
    print(type(i))
    x = i['id']
    print(type(x))


