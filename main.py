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
def Collision(ob1, ob2):
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
        if Collision(obBird, obColumn1) == True or Collision(obBird, obColumn2) == True: 
            return True
    if bird.y + bird.height < 0 or bird.y + bird.height > WINDOW_HEIGHT: 
        return True
    return False

# Tao lop Score tinh diem 
class Score(): 
    def __init__(self):
        self.score = 0
        self.addScore = True
        
    def draw(self): 
        font = pygame.font.SysFont('consolas', 30)
        scoreSurface = font.render('Score: ' + str(self.score), True, (0,0,255)) 
        textSize = scoreSurface.get_size()
        DISPLAYSURF.blit(scoreSurface, ((int(WINDOW_WIDTH) - textSize[0]), 0) )
         
    def update(self, bird, columns) : 
        collision = False
        for i in range(4): 
            obColumn = [columns.ls[i][0] + columns.width, columns.ls[i][1], 1, columns.blank]
            obBird = [bird.x, bird.y, bird.width, bird.height]
            if Collision(obBird, obColumn) == True: 
                collision = True
                break
        if collision == True: 
            if self.addScore == True:  
                self.score += 1
            self.addScore = False 
        else: 
            self.addScore = True 
            
# Tao gamePlay: 
def gamePlay(bird, columns, score): 
    bird.__init__()
    bird.speed = SPEED_FLY
    
    columns.__init__()
    score.__init__()
    
    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            bird.upFly(event)
                
        if isGameOver(bird, columns) == True: 
           return 
                    
        DISPLAYSURF.blit(BACKGROUND, (0,0)) 
        
        columns.draw()
        columns.update()
        
        bird.draw()
        bird.update()

        score.draw()
        score.update(bird, columns)
        
        pygame.display.update()
        fpsClock.tick(FPS)

# Tao gameStart
def gameStart(bird): 
    bird.__init__()
    
    font = pygame.font.SysFont('consolas', 60)
    headingSurface = font.render('FLAPPY CHICKEN', True, (255, 0, 0))
    headingSize = headingSurface.get_size()
    
    font = pygame.font.SysFont('consolas', 50)
    playSurface = font.render('Play game', True, (0,255,0))
    playSize = playSurface.get_size()
    
    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN: 
                return
        
        DISPLAYSURF.blit(BACKGROUND, (0,0))
        
        bird.draw()
        DISPLAYSURF.blit(headingSurface, (int((WINDOW_WIDTH - headingSize[0])/2), 100))
        DISPLAYSURF.blit(playSurface, (int((WINDOW_WIDTH - playSize[0])/3*2), 280))
        
        pygame.display.update()
        fpsClock.tick(FPS)

#Tao gameOver
def gameOver(bird, columns, score ): 
    font = pygame.font.SysFont('consolas', 60)
    headingSurface = font.render('Game over', True, (255, 0, 0))
    headingSize = headingSurface.get_size()
    
    font = pygame.font.SysFont('consolas', 40)
    scoreSurface = font.render('Score: ' + str(score.score), True, (0,255,0))
    scoreSize = scoreSurface.get_size()
    
    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN: 
                return
            
        DISPLAYSURF.blit(BACKGROUND, (0,0))    
        columns.draw()
        bird.draw()
            
        overWindow = pygame.Surface((500, 350))
        overWindow.fill((128, 128, 128))

        overWindow.blit(headingSurface, (int((500-headingSize[0])/2), 50))
        overWindow.blit(scoreSurface, (int((500-scoreSize[0])/2), 200))
        
        DISPLAYSURF.blit(overWindow, (175,125))
        pygame.display.update()
        fpsClock.tick(FPS)          
           
def main(): 
    bird = Bird()
    columns = Columns()
    score = Score()
    
    while True: 
        gameStart(bird)
        gamePlay(bird, columns, score)
        gameOver(bird, columns, score)
            
if __name__ == '__main__': 
    main()