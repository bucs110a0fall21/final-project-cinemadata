import pygame

def main():
	pygame.init()
	team = {"lead": "Kevin Wu", "backend": "Daniel Zheng", "frontend": "Wilson Huang"}
	print("The Software Lead is:", team["lead"])
	print("The Backend is:", team["backend"])
	print("The Frontend is:", team["frontend"])
main()
