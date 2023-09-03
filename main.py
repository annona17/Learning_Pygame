import pygame, sys
from pygame.locals import *
import random 

# Khoi tao cua so game 
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 600
BACKGROUND = pygame.image.load('img/background.jpg')

pygame.init()
FPS = 10
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy bird')

# Tao lop con chim 
BIRD_WIDTH = 60
BIRD_HEIGHT = 60
G = 0.5
SPEED_FLY = -8
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
    
    def update(self):
        self.y += self.speed + 0.5*G
        self.speed += G
        if self.y >= WINDOW_HEIGHT: 
            self.y = WINDOW_HEIGHT - 60
    
    def upFly(self, event):
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: 
                self.speed = SPEED_FLY   

# Tao lop cot 
COLUMN_WIDTH = 40
COLUMN_HEIGHT = 350
BLANK = 120
DISTANCE = 250
COLUMN_SPEED = 2
COLUMN_IMG = pygame.image.load('img/column.png')
COLUMN_scale = pygame.transform.scale(COLUMN_IMG, (COLUMN_WIDTH, COLUMN_HEIGHT))

class Columns(): 
    def __init__(self):
        self.width = COLUMN_WIDTH
        self.height = COLUMN_HEIGHT
        self.blank = BLANK
        self.distance = DISTANCE
        self.speed = COLUMN_SPEED
        self.surface = COLUMN_scale
        self.ls = []
        for i in range(4):
            x = i*self.distance
            y = random.randrange(100, WINDOW_HEIGHT - self.blank - 100, 30)
            self.ls.append([x,y])
    
    def draw(self): 
        for i in range(4): 
            DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] - self.height))
            DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] + self.blank)) 
             
def main(): 
    bird = Bird()
    columns = Columns()
    
    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            bird.upFly(event)
                
        DISPLAYSURF.blit(BACKGROUND, (0,0))
        
        columns.draw()
        
        bird.draw()
        bird.update()
        
        pygame.display.update()
        fpsClock.tick(FPS)
        
if __name__ == '__main__': 
    main()