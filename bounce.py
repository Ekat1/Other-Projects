import pygame as py
py.init() 

floor = 500

win = py.display.set_mode((1400,floor))
py.display.set_caption("Bouncy")
win.fill((255,255,255))

xPos = 0
yPos = 0
xVel = 1
yVel = 0
vLoss = 0.5

run = True
while run:

    py.time.delay(100)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    py.draw.circle(win,(0,0,0),(xPos,yPos),1)
    py.display.update()

    if yPos > floor:
        print("*"+str(yVel))
        xPos += (yPos - floor)/yVel
        yVel -= (yPos-floor)/yVel
        yPos = floor
        yVel *= -vLoss
        yPos += yVel
        print(str(yVel)+"\n")
    elif yPos == floor:
        print("*"+str(yVel))
        xPos += xVel
        yVel *= -vLoss
        yPos += yVel
        print(str(yVel)+"\n")
    elif yPos < floor:
        xPos += xVel
        yPos += yVel
        
    yVel +=1

py.quit()
