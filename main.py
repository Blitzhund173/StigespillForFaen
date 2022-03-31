#Import packages, standard stuff
import sys,pygame, os, time, random

#Initiate pygame
pygame.init()

#Sets the size of the window
size=width, height=1000, 720
#Husk å gange alt med 1,5

#Defines some colores we will use later
black=0, 0, 0
white=255,255,255
red=255,0,0
blue=0,0,255
green=0,255,0
yellow=255,255,0
#Adds them to a list
colorList=[red,blue,yellow,green,white,black]

#Some playerdata, such as the current player, their position on the board (number they are on) and the x and y coordinates
currentPlayer=0
currentPlayerPos=[1,1,1,1]
xCoords=[0]
yCoords=[0]

#The lists for ladders
ladderList=[3,7,25,41,70,85,88,96]
endLadderList=[45,13,67,80,51,29,56,77]
endLadderX=[4,7,6,0,8,4,3]
endLadderY=[5,8,3,2,7,4,2]

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

#List for the rects for each color
playerList=[redPlayer,bluePlayer,yellowPlayer,greenPlayer]
rectList=[redRect,blueRect,yellowRect,greenRect]

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

#This clusterfuck of a function makes the player go backwards when not getting a perfect amount on the dice on the last block
def moveBack(num):
    screen.blit(playerList[currentPlayer],rectList[currentPlayer])
    #Moves back and paints
    for i in range(0,num-1):
        #Moves the current player position back
        currentPlayerPos[currentPlayer]-=1 
        #Changes the position of the rectangles or "hitboxes"
        rectList[currentPlayer].topleft=xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1
        #Actually moves the player
        screen.blit(playerList[currentPlayer],rectList[currentPlayer])
        #Paints the block the player is currently on
        drawSquare(colorList[currentPlayer],xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
        drawNumber(f"{currentPlayerPos[currentPlayer]}",xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
        #Paints the block the player was on, painting over the old player sprite
        drawSquare(colorList[currentPlayer],xCoords[currentPlayerPos[currentPlayer]+1]*72+1,yCoords[currentPlayerPos[currentPlayer]+1]*72+1)
        drawNumber(f"{currentPlayerPos[currentPlayer]+1}",xCoords[currentPlayerPos[currentPlayer]+1]*72+1,yCoords[currentPlayerPos[currentPlayer]+1]*72+1)
        #Checks if the current player position is in the list of ladder
        if currentPlayerPos[currentPlayer] in ladderList:
            #I suspect this is redundant, but it paints the block the player is on
            drawSquare(colorList[currentPlayer],xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
            drawNumber(f"{currentPlayerPos[currentPlayer]}",xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
            #Changes the position of the player and "hitbox"
            currentPlayerPos[currentPlayer]=endLadderList[int(ladderList.index(currentPlayerPos[currentPlayer]))]
            rectList[currentPlayer].topleft=xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1
            #Paints the player
            screen.blit(playerList[currentPlayer],rectList[currentPlayer])
            #Paints the block the player landed on
            drawSquare(colorList[currentPlayer],xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
            drawNumber(f"{currentPlayerPos[currentPlayer]}",xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
        #Paints the players so they are not painted over
        for i in range(0,4):
                    screen.blit(playerList[i],rectList[i])
                    pygame.display.flip()
        #Takes a power-nap
        time.sleep(0.3)

def move(num):
    global currentPlayer
    #Repeats num amount of times
    for i in range(0,num):
        time.sleep(0.3)
        #Changes the position
        currentPlayerPos[currentPlayer]+=1
        #Checks if the current player position is larger than 100
        if currentPlayerPos[currentPlayer]>=100:
            #If i is equal to num(-1) it means that the player has won
            if i>=num-1:
                font=pygame.font.Font("Freesansbold.ttf",32)
                winText=font.render(str(f"Player {currentPlayer+1} is the winner!"),True,(colorList[currentPlayer]))
                exit
            #If not, it moves the player back
            else:
                moveBack(num-i)
                for i in range(0,4):
                    screen.blit(playerList[i],rectList[i])
                    pygame.display.flip()
                break                
        #If not, move like normal
        else:
            #Change the "hitbox" and player position
            rectList[currentPlayer].topleft=xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1
            screen.blit(playerList[currentPlayer],rectList[currentPlayer])
            #Paints the blocks at the player position and behind him
            drawSquare(colorList[currentPlayer],xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
            drawNumber(f"{currentPlayerPos[currentPlayer]}",xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
            drawSquare(colorList[currentPlayer],xCoords[currentPlayerPos[currentPlayer]-1]*72+1,yCoords[currentPlayerPos[currentPlayer]-1]*72+1)
            drawNumber(f"{currentPlayerPos[currentPlayer]-1}",xCoords[currentPlayerPos[currentPlayer]-1]*72+1,yCoords[currentPlayerPos[currentPlayer]-1]*72+1)
            #Paints the other players so they are visible
            for i in range(0,4):
                screen.blit(playerList[i],rectList[i])
                pygame.display.flip()
    #If the player position is in the list of ladder, move up/down the ladder
    if currentPlayerPos[currentPlayer] in ladderList:
        drawSquare(colorList[currentPlayer],xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
        drawNumber(f"{currentPlayerPos[currentPlayer]}",xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
        currentPlayerPos[currentPlayer]=endLadderList[int(ladderList.index(currentPlayerPos[currentPlayer]))]
        rectList[currentPlayer].topleft=xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1
        screen.blit(playerList[currentPlayer],rectList[currentPlayer])
        drawSquare(colorList[currentPlayer],xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)
        drawNumber(f"{currentPlayerPos[currentPlayer]}",xCoords[currentPlayerPos[currentPlayer]]*72+1,yCoords[currentPlayerPos[currentPlayer]]*72+1)

        pygame.display.flip()
    #Paint the players
    for i in range(0,4):
        screen.blit(playerList[i],rectList[i])
    #Change the currentplayer 
    if currentPlayer>=3:
        currentPlayer=0
    else:
        currentPlayer+=1

#Set up the dice list and co.
dices=[]
diceRect=[]
#Loads the dices into the list
for i in range(1,7):
    dices.append(pygame.image.load(f"Assets/{i}.png"))
    diceRect.append(dices[i-1].get_rect())
    diceRect[i-1].center=850,360

def diceRoll():
    #"Rolls" the dice 10 times
    for i in range(0,10):
        #Takes a random number and displays the corrosponding dice
        rand=random.randint(0,5)
        screen.blit(dices[rand],diceRect[rand])
        pygame.display.flip()
        time.sleep(0.2)
    #Returns a random number between 1 and 6
    return rand+1

#Sets up the screen
screen.fill(black)
#Draws all the squares and constructs the coordinate list
for y in range(0,10):
    y=9-y
    if y%2==0:
        for x in range(0,10):
            x=9-x
            #Paints a white square
            drawSquare(white,x*72+1,y*72+1)           
            pygame.display.flip()
            #Adds the coordinate to the lists
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
    #It has to write them backwards sometimes because of some unknown bug that drew half of the screen
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

#Moves the players to the start
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
        #Checks if you pressed the exit button
        if event.type == pygame.QUIT: sys.exit()
        #Checks if you pressed space and moves in that case
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                move(diceRoll())

    #Flips the display from vram to the screen
    pygame.display.flip()