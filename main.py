import sys,pygame, os, time
pygame.init()

size=width, height=720, 720
#Husk å gange alt med 1,5


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

def drawSquare(color,posX,posY):
    pygame.draw.rect(screen,color,pygame.Rect(posX,posY,70,70))

def drawNumber(text,posX,posY):
    font=pygame.font.Font("freesansbold.ttf",16)
    number=font.render(str(text),True,(0,0,0))
    screen.blit(number,(posX,posY))
    pygame.display.flip()

screen=pygame.display.set_mode(size)

for x in range(0,10):
        for y in range(0,10):
            drawSquare(white,x*72+1,y*72+1)
            drawNumber(x,x*72+1,y*72+1)
            pygame.display.flip()
            

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    