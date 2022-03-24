import sys,pygame, os, time
pygame.init()

size=width, height= 720, 720

black=0, 0, 0
white=255,255,255
red=255,0,0
blue=0,0,255
green=0,255,0
yellow=255,255,0

screen=pygame.display.set_mode(size)#, pygame.SCALED

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    pygame.display.flip()
    time.sleep(0.01666)
    screen.fill(white)
    pygame.display.flip()
    time.sleep(0.01666)
    screen.fill(red)
    pygame.display.flip()
    time.sleep(0.01666)
    screen.fill(blue)
    pygame.display.flip()
    time.sleep(0.01666)
    screen.fill(green)
    pygame.display.flip()
    time.sleep(0.01666)
    screen.fill(yellow)
    pygame.display.flip()

print("det funker for faen")
