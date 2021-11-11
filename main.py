import pygame
from src import button
from src import controller
def main():
	pygame.init()
	team = {"lead": "Kevin Wu", "backend": "Daniel Zheng", "frontend": "Wilson Huang"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:", team["frontend"])
	screen = controller.Controller()
	test = button.Button("test", 100, 100, "assets/class_diagram.jpg")
main()
