import requests
import pygame
class MoviePoster(pygame.sprite.Sprite):
    def __init__(self, url, save_path):
        #requests for image and saves image to path being used
        super().__init__()
        self.url = url
        self.save_path = save_path
        response = requests.get(self.url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            file.close()
