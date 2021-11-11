import pygame

class Button:
    def __init__(self, button_type, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.type = button_type
        self.image = pygame.image.load(img_file).convert_alpha()
        self.status = False
    
    def update(self, x, y):
        self.x = x
        self.y = y