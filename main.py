import pygame, sys
from pygame.locals import *

# Khoi tao cua so game 
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 600
BACKGROUND = pygame.image.load('img/background.jpg')

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy bird')

# Tao lop con chim 
BIRD_WIDTH = 70
BIRD_HEIGHT = 70
G = 0.5
SPEEDLY = -8
BIRD_IMG = pygame.image.load('img/bird.png')
BIRD_scale = pygame.transform.scale(BIRD_IMG, (BIRD_WIDTH, BIRD_HEIGHT))

class Bird():
    def __init__(self):
        self.width = BIRD_WIDTH
        self.height = BIRD_HEIGHT
        self.x = (WINDOW_WIDTH - self.width)/5*2
        self.y = (WINDOW_HEIGHT - self.height)/2
        self.speed = 0
        self.surface = BIRD_scale
        
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y)))
            
def main(): 
    bird = Bird()
    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
                
        DISPLAYSURF.blit(BACKGROUND, (0,0))
        
        bird.draw()
        
        pygame.display.update()
        fpsClock.tick(FPS)
        
if __name__ == '__main__': 
    main()