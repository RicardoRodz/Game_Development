import pygame, sys, os, time, random
from pygame.locals import *


class DodgeCars:
    def __init__(self, Display):
        self.Display = Display
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.width = 800
        self.height = 600
        self.GOImg = pygame.image.load("resources/gameover.png")
        self.Pscore = []
        
    def Blit_Image(self, Image, x, y):
        self.Display.blit(Image, (x, y))