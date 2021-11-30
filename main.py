import pygame
from src import Controller
import tempfile

def main():
	pygame.init()
	team = {"lead": "Kevin Wu", "backend": "Daniel Zheng", "frontend": "Wilson Huang"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:", team["frontend"])
	fo = tempfile.TemporaryDirectory(dir = 'assets')
	r = fo.name.split("\\")
	main_window = Controller.Controller(r[1])
	main_window.mainLoop()
	fo.cleanup()
main()
