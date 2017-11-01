

import pygame, time, sys
from pygame.locals import *
from random import *

black = [0,0,0]

class Player():
    def __init__(self):
        self = Rect(10, 10, 30, 30)
        self.width = 20
        self.height = 50
        self.x = 10
        self.y = 10
        self.color = [255,0,255]


##        self.speedX = 0
##        self.speedY = 0

##    def move(self,screen):
##        for event in pygame.event.get():
##            if(event.type == pygame.KEYDOWN):
##                if(event.key == pygame.K_DOWN):
##                    pygame.draw.rect(screen,black,[self.xValue,self.yValue,20,50],0)
##                    self.yValue += 1
##                    pygame.draw.rect(screen,self.color,[self.xValue,self.yValue,20,50],0)
##                    pygame.display.update()
##                if(event.key == pygame.K_UP):
##                    pygame.draw.rect(screen,black,[self.xValue,self.yValue,20,50],0)
##                    self.yValue -= 1
##                    pygame.draw.rect(screen,self.color,[self.xValue,self.yValue,20,50],0)
##                    pygame.display.update()
