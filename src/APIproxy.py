import requests
import pygame
class MoviePoster(pygame.sprite.Sprite):
    def __init__(self, url, save_path):
        #requests for image and saves image to path being used
        super().__init__()
        self.url = url
        response = requests.get(self.url)
        if response.status_code ==200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            file.close()
        self.image = pygame.image.load(save_path)
        self.rect = self.image.get_rect()
        self.resize()
    
    def resize(self):
        # Paramters of transform.scale = (surface, size(width, height), destination surface)
        pygame.transform.scale(self.image, ( 50, 100))
        self.rect = self.image.get_rect()
