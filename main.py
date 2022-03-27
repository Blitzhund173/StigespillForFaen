import sys,pygame, os, time
pygame.init()

size=width, height= 720, 720

black=0, 0, 0
white=255,255,255
red=255,0,0
blue=0,0,255
green=0,255,0
yellow=255,255,0

currentPlayer=0
currentPlayerPos=[0,0,0,0]
xCoords=[0]
yCoords=[0]

class Block:
    def __init__(self,pos):
        self.color=white
        self.pos=pos
    def paintBlock(self,color):
        self.color=color
        pass

screen=pygame.display.set_mode(size)#, pygame.SCALED

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()