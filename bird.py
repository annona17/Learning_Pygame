import pygame, sys
from pygame.locals import *

WINDOW_WIDTH = 850
WINDOW_HEIGHT = 600

BIRD_WIDTH = 80
BIRD_HEIGHT = 60
G = 0.5
SPEEDLY = -8
BIRD_IMG = pygame.image.load('img/bird.png')

class Bird():
    def __init__(self):
        self.width = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.x = (WINDOW_WIDTH - self.width) /2
        self.y = (WINDOW_HEIGHT - self.height)/2
        self.speed = 0
        self.surface = BIRD_IMG
        
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y)))
        