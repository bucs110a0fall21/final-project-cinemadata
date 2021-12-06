import pygame
from src import Controller
import tempfile

def main():
	pygame.init()
	team = {"lead": "Kevin Wu", "backend": "Daniel Zheng", "frontend": "Wilson Huang"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:", team["frontend"])
	temp_directory = tempfile.TemporaryDirectory(dir = 'assets')
	directory_name = temp_directory.name.split("\\")
	main_window = Controller.Controller(directory_name[1])
	main_window.mainLoop()
	directory_name.cleanup()
main()
