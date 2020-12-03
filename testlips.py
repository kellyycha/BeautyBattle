from cmu_112_graphics import *
import math
import random

def appStarted(mode):
    mode.x = 210
    mode.y = 360
    mode.r = 3
    mode.drawnDots1 = []
    mode.directions = [+2,1,-1,-2]
    mode.dx = random.choice(mode.directions)
    mode.dy = random.choice(mode.directions)
    mode.centerx = 220
    mode.centery = 340
    mode.centerx2 = 210
    mode.centery2 = 365
    mode.centerx3 = 230
    mode.centery3 = 365
    mode.draw1 = True
    mode.filled1 = False
    mode.timerDelay = 10

def timerFired(mode):
    if mode.filled1 == False and mode.draw1 == True:
        moveDot(mode)
    elif mode.filled1 == True:
        print('done')
        mode.draw2 = False
    
def distance(mode, x1, y1, x2, y2):
    return ((x1- x2)**2 + (y1-y2)**2)**0.5 + mode.r

def mousePressed(mode, event):
    print(f'{(event.x,event.y)},')

def moveDot(mode):
    mode.drawnDots1.append((mode.x,mode.y))

    #xValues = []
    #yValues = []
    #for (x,y) in mode.drawnDots1:
    #    xValues.append(x)
    #    yValues.append(y)
    #minX = min(xValues)
    #maxX = max(xValues)
    #minY = min(yValues)
    #maxY = max(yValues)
    #print(f"1: {minX},{maxX},{minY},{maxY}")
    #if maxX-minX >= 50 and maxY-minY >=20:
    #    mode.filled1 = True



    if distance(mode, mode.centerx2, mode.centery2, mode.x, mode.y) > 13 and \
        distance(mode, mode.centerx3, mode.centery3, mode.x, mode.y) < 13 and \
        distance(mode, mode.centerx, mode.centery, mode.x, mode.y) <= 30:
        mode.x += mode.dx
        mode.y += mode.dy
    
    elif distance(mode, mode.centerx2, mode.centery2, mode.x, mode.y) < 13 and \
        distance(mode, mode.centerx3, mode.centery3, mode.x, mode.y) > 13 and \
        distance(mode, mode.centerx, mode.centery, mode.x, mode.y) <= 30:
        mode.x += mode.dx
        mode.y += mode.dy

    else:
        mode.x -= mode.dx
        mode.y -= mode.dy
        mode.dx = random.choice(mode.directions)
        mode.dy = random.choice(mode.directions)


def redrawAll(mode, canvas):
    canvas.create_oval(220 - 30, 340 - 30, 220 + 30, 340 + 30)
    canvas.create_oval(220-10 - 13, 365 - 13, 220-10 + 13, 365 + 13)
    canvas.create_oval(220+10 - 13, 365 - 13, 220+10 + 13, 365 + 13)

    #canvas.create_oval(220 - 7, 364 - 7, 220 + 7, 364 + 7)
    #canvas.create_oval(220-10 - 7, 361 - 7, 220-10 + 7, 361 + 7)
    #canvas.create_oval(220+10 - 7, 361 - 7, 220+10 + 7, 361 + 7)


    for (cx, cy) in mode.drawnDots1:
        canvas.create_oval(cx-mode.r, cy-mode.r, cx+mode.r, cy+mode.r, fill = 'red', outline = '')


runApp(width=1000, height=500)
