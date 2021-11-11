import pygame
from pygame import display
from src import button
t=True
pygame.init()
pygame.display.set_mode((100,100))
bob = button.Button("back", 3, 4, "assets/class_diagram.jpg")
print(bob.type)
bob.type = "front"
print(bob.type)
print(bob.x, bob.y)
