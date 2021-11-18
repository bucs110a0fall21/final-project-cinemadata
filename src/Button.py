import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, scale, text):
        #initiates the button values

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.scale = scale
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.scaled = pygame.transform.scale(self.image, (int(self.width * self.scale), int(self.height * self.scale)))
        #self.label
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.status = False
        self.label = text
        self.text = pygame.font.SysFont(None, 30)
        self.message = self.text.render(text, True, (255, 255, 255))
        self.message_rect = self.message.get_rect(center = (self.width / 2, self.height/2))
        self.image.blit(self.message, self.message_rect)


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
