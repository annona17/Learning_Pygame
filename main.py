import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 850
WINDOWHEIGHT = 600
BACKGROUND = pygame.image.load('img/background.jpg')

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Flappy bird')

def main(): 
    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
                
        DISPLAYSURF.blit(BACKGROUND, (0,0))
        pygame.display.update()
        fpsClock.tick(FPS)
        
if __name__ == '__main__': 
    main()