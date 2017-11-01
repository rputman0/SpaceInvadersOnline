import pygame, time, sys
from pygame.locals import *
from random import *
from Square import *
from player import *

pygame.init()

#set up the window
width,height = (200,200);
screen = pygame.display.set_mode( (width,height) )
pygame.display.set_caption('')

#create the squares
squareSize = 10 #TODO: remove? rename variables
sOne = Square(width, height)
pOne = Player()

#set the background screen
black =[0,0,0]

def drawRect(color,xValue,yValue):
    pygame.draw.rect(screen,color,[xValue,yValue,squareSize,squareSize])

def drawPlayer(color,xValue,yValue,squareWidth,squareHeight):
    pygame.draw.rect(screen,color,[xValue,yValue,squareWidth,squareHeight])

def withinWindow(value,total):
    return (value > (total-squareSize) or value < 0)

def bounce(square,player):
    #if it hits a wall go in opposite direction, and change color
    if(withinWindow(square.yValue,height)):
        square.speedY *= -1
        square.color = [randint(20,255),randint(20,255),randint(20,255)]

    if(player.contains(square)):
        square.speedX *= -1
        square.color = [randint(20,255),randint(20,255),randint(20,255)]
      
    if(withinWindow(square.xValue,width+20)):
          print("Score + 1")
          drawRect(black,square.xValue,square.yValue) 
          square.xValue = 175
          square.yValue = 50
          drawMovingSquare(square,player)

def drawMovingSquare(square,player):
    #draw over the old square, and then draw a new one
    drawRect(black,square.xValue,square.yValue) 
    square.xValue += square.speedX
    square.yValue += square.speedY
    drawRect(square.color,square.xValue,square.yValue)

    #TODO:if it hits another square, go in the opposite direction
        #create a function that determines if a point is within a rectangle

    bounce(square,player)

    
drawPlayer(pOne.color,pOne.xValue,pOne.yValue,pOne.squareWidth,pOne.squareHeight)
    
#create an infinte loop of the colliding squares
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    drawMovingSquare(sOne,pOne)

    if(event.type == pygame.KEYDOWN):
        if(event.key == pygame.K_DOWN):
            pygame.draw.rect(screen,black,[pOne.xValue,pOne.yValue,20,50],0)
            pOne.yValue += 1
            pygame.draw.rect(screen,pOne.color,[pOne.xValue,pOne.yValue,20,50],0)
            pygame.display.update()
        if(event.key == pygame.K_UP):
            pygame.draw.rect(screen,black,[pOne.xValue,pOne.yValue,20,50],0)
            pOne.yValue -= 1
            pygame.draw.rect(screen,pOne.color,[pOne.xValue,pOne.yValue,20,50],0)
            pygame.display.update()
    
    pygame.display.update()
    time.sleep(0.01)
