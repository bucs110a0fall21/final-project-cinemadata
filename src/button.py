import pygame

class Button:
    def __init__(self, button_type, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.type = button_type
        self.image = pygame.image.load(img_file).convert_alpha()
        self.status = False
        self.genre = ''
        self.selected_genres = []

    def genreButton(self, genre):
        self.genre = genre

    def selected(self):
        if not self.status:
            self.status = True
            return True
        else:
            self.status = False
            return False

    def update(self, x, y, status):
        self.x = x
        self.y = y
        self.status = status