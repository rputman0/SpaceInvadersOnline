from random import *

class Square():
    def __init__(self,width,height):
        squareSize = 10 #duplicated variable?
        self.xValue = randint(0,width-(squareSize-10) )
        self.yValue = randint(0,height-(squareSize-10) )
        
        #start with blue color, and change every time it hits a wall
        self.color = [0,0,255]

        self.speedX = -1
        self.speedY = 1

##    def random():
##        return (1 or -1)
