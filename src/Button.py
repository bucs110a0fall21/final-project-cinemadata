import pygame

class Button:
    def __init__(self, x, y, img_file, scale):
        #initiates the button values

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.scaled = pygame.transform.scale(self.image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.status = False
        self.genre = ''

    def genreButton(self, genre):
        #Add a genre to the button if it is a genre
        self.genre = genre
        #Genre is not included as a parameter in the init so that buttons that are not genre buttons dont need to have a genre parameter

    def selected(self):
        #changes status of the button to True(selected) or False(unselected), based on current status and returns that value
        if not self.status:
            self.status = True
            return True
        else:
            self.status = False
            return False

    def update(self, x, y, status):
        #updates the position of the button and status if needed
        self.rect.x = x
        self.rect.y = y
        self.status = status
