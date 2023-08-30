import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((700,600))
pygame.display.set_caption('lna')

while True: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
            
    
