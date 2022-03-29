import sys,pygame, os, time, random
pygame.init()

#Sets the size of the window
size=width, height=720, 720
#Husk å gange alt med 1,5

#Defines some colores we will use later
black=0, 0, 0
white=255,255,255
red=255,0,0
blue=0,0,255
green=0,255,0
yellow=255,255,0

#Some playerdata, such as the current player, their position on the board (number they are on) and the x and y coordinates
currentPlayer=0
currentPlayerPos=[0,0,0,0]
xCoords=[0]
yCoords=[0]

#Stores blocks that are a different color
redBlocks=[0]
blueBlocks=[0]
yellowBlocks=[0]
greenBlocks=[0]


#Actually draws the window to the screen
screen=pygame.display.set_mode(size)

#Loads player images ang gets them a hitbox. They are numbered from 0-3 starting from the top

#Player 0 / red
redPlayer=pygame.image.load("Assets\Bøtte-Rød.png")
redPlayer=pygame.transform.scale(redPlayer,(70,70))
redRect=redPlayer.get_rect()

#Player 1 / blue
bluePlayer=pygame.image.load("Assets\Bøtte-Blå.png")
bluePlayer=pygame.transform.scale(bluePlayer,(70,70))
blueRect=bluePlayer.get_rect()

#Player 2 / yellow
yellowPlayer=pygame.image.load("Assets\Bøtte-Gul.png")
yellowPlayer=pygame.transform.scale(yellowPlayer,(70,70))
yellowRect=yellowPlayer.get_rect()

#Player 3 / green
greenPlayer=pygame.image.load("Assets\Bøtte-Grønn.png")
greenPlayer=pygame.transform.scale(greenPlayer,(70,70))
greenRect=greenPlayer.get_rect()

#Defines drawSquare(). This is a function that draws a square in the designated position and color, is fixed to 70px x 70px
def drawSquare(color,posX,posY):
    pygame.draw.rect(screen,color,pygame.Rect(posX,posY,70,70))
    pygame.display.flip()

#Draws a number on the designated position
def drawNumber(text,posX,posY):
    font=pygame.font.Font("freesansbold.ttf",16)
    number=font.render(str(text),True,(0,0,0))
    screen.blit(number,(posX,posY))
    pygame.display.flip()

def move(num):
    if currentPlayer==0:
        for i in range(0,num):
            currentPlayerPos[0]+=1
            redRect.topleft=xCoords[currentPlayerPos[0]]*72+1,yCoords[currentPlayerPos[0]]*72+1
            screen.blit(redPlayer,redRect)
            drawSquare(white,xCoords[currentPlayerPos[0]-1]*72+1,yCoords[currentPlayerPos[0]-1]*72+1)
            time.sleep(1)
        
    if currentPlayer==1:
        pass
    if currentPlayer==2:
        pass
    if currentPlayer==3:
        pass

dices=[]
diceRect=[]
for i in range(1,6):
    dices.append(pygame.image.load(f"Assets/{i}.png"))
    diceRect.append(dices[i-1].get_rect())


def diceRoll():
    for i in range(1,6):
        pass
    return random.randint(1,6)

screen.fill(black)
#Draws all the squares and constructs the coordinate list
for y in range(0,10):
    y=9-y
    if y%2==0:
        for x in range(0,10):
            x=9-x
            drawSquare(white,x*72+1,y*72+1)           
            pygame.display.flip()
            xCoords.append(x)
            yCoords.append(y)
    else:
        for x in range(0,10):
            drawSquare(white,x*72+1,y*72+1)           
            pygame.display.flip()
            xCoords.append(x)
            yCoords.append(y)

#Sets the number the game should write to the board and draws them in order
numberToWrite=0
for y in range(0,10):
    y=9-y
    if y%2==0:
        numberToWriteDown=numberToWrite+10
        numberToWrite+=10
        for x in range(0,10):
            drawNumber(numberToWriteDown,x*72+1,y*72+1)
            numberToWriteDown-=1
    else:
        for x in range(0,10):
            numberToWrite+=1
            drawNumber(numberToWrite,x*72+1,y*72+1)

redRect.move(10,0)

redRect.topleft=xCoords[1]*72+1,yCoords[1]*72+1
screen.blit(redPlayer,redRect)

blueRect.topleft=xCoords[1]*72+1,yCoords[1]*72+1
screen.blit(bluePlayer,blueRect)

yellowRect.topleft=xCoords[1]*72+1,yCoords[1]*72+1
screen.blit(yellowPlayer,yellowRect)

greenRect.topleft=xCoords[1]*72+1,yCoords[1]*72+1
screen.blit(greenPlayer,greenRect)

#The main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    

    pygame.display.flip()