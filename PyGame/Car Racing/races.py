import pygame, sys, time, random
from pygame.locals import *

pygame.init()

width = 800
height = 600
FPS = 40 #Frame Rate (Frames per Second)
white = (255, 255, 255)
l_red = (255, 0 ,0)
red = (150, 0 , 0)
l_green = (0, 255, 0)
green = (0, 150, 0)
yellow = (255, 299, 10)
l_yellow = (212, 255, 10)
black = (0, 0, 0)
road_color = (47, 47, 47)

Display = pygame.display.set_mode((width,height)) #Display surface object
pygame.display.set_caption("The Car Racing") # Caption 
clock = pygame.time.Clock() #Time Object

CarImg = pygame.image.load("resources/car.png") #Loading Car Image
Road_Img1 = pygame.image.load("resources/road1.jpg")
Tree_Img1 = pygame.image.load("resources/tree1.jpg")
Tree_Img2 = pygame.image.load("resources/tree2.jpg")
Bugatti = pygame.image.load("resources/Bugatti.png")
GameIcon = pygame.image.load("resources/GameIcon.png")
pygame.display.set_icon(GameIcon)

life = 2 #Life of the Player
Previous_Score = DodgeCars(Display)
Previous_Score.Previous_Score()

EndGame = False
