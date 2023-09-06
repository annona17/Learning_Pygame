import pygame, sys
from pygame.locals import *
import random 

# Khoi tao cua so game 
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 600
BACKGROUND = pygame.image.load('img/background.jpg')

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy chicken')

# Tao lop con chim 
BIRD_WIDTH = 60
BIRD_HEIGHT = 60
G = 0.5
SPEED_FLY = -7
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
BLANK = 150
DISTANCE = 250
COLUMN_SPEED = 1
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
            y = random.randrange(60, WINDOW_HEIGHT - self.blank - 60, 30)
            self.ls.append([x,y])
    
    def draw(self): 
        for i in range(4): 
            DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] - self.height))
            DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] + self.blank)) 
    
    def update(self): 
        for i in range(4): 
            self.ls[i][0] -= self.speed
        if self.ls[0][0] < - self.width: 
            self.ls.pop(0)
            x = self.ls[2][0] + self.distance
            y = random.randrange(60, WINDOW_HEIGHT - self.blank - 60, 30)
            self.ls.append([x,y])

# Xu ly va cham
def collision(ob1, ob2):
    ob1 = [float(x) for x in ob1]  
    ob2 = [float(x) for x in ob2] 
    if ob1[0] <= ob2[0] + ob2[2] and ob2[0] <= ob1[0] + ob1[2] and ob1[1] <= ob2[1] + ob2[3] and ob2[1] <= ob1[1] + ob1[3]:
        return True
    return False

# Kiem tra game over 
def isGameOver(bird, columns): 
    for i in range(4): 
        obBird = [bird.x, bird.y, bird.width, bird.height]
        obColumn1 = [columns.ls[i][0], columns.ls[i][1] - columns.height, columns.width, columns.height]
        obColumn2 = [columns.ls[i][0], columns.ls[i][1] + columns.blank, columns.width, columns.height]
        if collision(obBird, obColumn1) == True or collision(obBird, obColumn2) == True: 
            return True
    if bird.y + bird.height < 0 or bird.y + bird.height > WINDOW_HEIGHT: 
        return True
    return False
        
def main(): 
    bird = Bird()
    columns = Columns()
    
    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            bird.upFly(event)    
        if isGameOver(bird, columns) == True: 
            pygame.quit()
            sys.exit()
                    
        DISPLAYSURF.blit(BACKGROUND, (0,0)) 
        
        columns.draw()
        columns.update()
        
        bird.draw()
        bird.update()
        
        pygame.display.update()
        fpsClock.tick(FPS)
        
if __name__ == '__main__': 
    main()