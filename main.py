import pygame

def main():
	pygame.init()
	team = {"lead": "Kevin Wu", "backend": "Daniel Zheng", "frontend": "Wilson Huang"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:", team["frontend"])
main()
