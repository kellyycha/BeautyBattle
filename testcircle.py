from cmu_112_graphics import *
import math
import random

def appStarted(mode):
    mode.x = mode.width//2
    mode.y = mode.height//2
    mode.r = 20
    mode.drawnDots1 = []
    mode.drawnDots2 = []
    mode.directions = [+1,2,3,-3,-2,-1]
    mode.dx = random.choice(mode.directions)
    mode.dy = random.choice(mode.directions)
    mode.draw1 = True
    mode.centerx = mode.width//2
    mode.centery = mode.height//2
    mode.draw2 = False
    mode.filled1 = False
    mode.filled2 = False
    mode.score = 100
    mode.score1 = 100
    mode.score2 = 100
    mode.timerDelay = 50


def timerFired(mode):
    if mode.filled1 == False and mode.draw1 == True:
        moveDot(mode)
    elif mode.filled1 == True and mode.filled2 == False:
        mode.draw1 = False
        mode.draw2 = True
        moveDot(mode)
    elif mode.filled2 == True:
        print('done')
        mode.draw2 = False
        score(mode)

def score(mode):
    if mode.filled1:
        xValues = []
        yValues = []
        for (x,y) in mode.drawnDots1:
            xValues.append(x)
            yValues.append(y)
        minX = min(xValues)
        maxX = max(xValues)
        minY = min(yValues)
        maxY = max(yValues)

        if maxX-minX == 25 and maxY-minY == 25: 
            mode.score1 = 100
        elif maxX-minX == 25 and maxY-minY < 25:
            mode.score1 = 100 - (25 - (maxY-minY))
        elif maxX-minX < 25 and maxY-minY == 25: 
            mode.score1 = 100 - (25 - (maxX-minX))
        #if drawn out of bounds
        else:
            mode.score1 = 100 - (25 - (maxX-minX)) - (25 - (maxY-minY))
    
    if mode.filled2:
        xValues = []
        yValues = []
        for (x,y) in mode.drawnDots2:
            xValues.append(x)
            yValues.append(y)
        minX = min(xValues)
        maxX = max(xValues)
        minY = min(yValues)
        maxY = max(yValues)

        if maxX-minX == 25 and maxY-minY == 25: 
            mode.score2 = 100
        elif maxX-minX == 25 and maxY-minY < 25:
            mode.score2 = 100 - (25 - (maxY-minY))
        elif maxX-minX < 25 and maxY-minY == 25: 
            mode.score2 = 100 - (25 - (maxX-minX))
        #if drawn out of bounds
        else:
            mode.score2 = 100 - (25 - (maxX-minX)) - (25 - (maxY-minY))

    if mode.filled1 and mode.filled2:
        mode.score = (mode.score1+mode.score2)//2

def distance(mode, x1, y1, x2, y2):
    return ((x1- x2)**2 + (y1-y2)**2)**0.5 + mode.r

def moveDot(mode):
    if mode.draw1:
        mode.centerx = mode.width//2
        mode.centery = mode.height//2
        mode.drawnDots1.append((mode.x,mode.y))
        
        for (x1,y1) in mode.drawnDots1:
            if distance(mode, mode.centerx, mode.centery, x1, y1) == 30:
                mode.filled1 = True

    elif mode.draw2:
        mode.centerx = mode.width//2 + 80
        if mode.drawnDots2 == []:
            mode.x = mode.width//2 + 80
        mode.drawnDots2.append((mode.x,mode.y))
        
        for (x1,y1) in mode.drawnDots2:
            if distance(mode, mode.centerx, mode.centery, x1, y1) == 30:
                mode.filled2 = True

    if distance(mode, mode.centerx, mode.centery, mode.x, mode.y) <= 30:
        mode.x += mode.dx
        mode.y += mode.dy
        print('1')
    elif distance(mode, mode.centerx, mode.centery, mode.x, mode.y) > 30:
        mode.x -= mode.dx
        mode.y -= mode.dy
        mode.dx = random.choice(mode.directions)
        mode.dy = random.choice(mode.directions)
        print('2')


def redrawAll(mode, canvas):
    canvas.create_oval(mode.width//2 - 30, mode.height//2 - 30, mode.width//2 + 30, mode.height//2 + 30)

    canvas.create_oval(mode.width//2 + 50, mode.height//2 - 30, mode.width//2 + 110, mode.height//2 + 30)
    
    for (cx, cy) in mode.drawnDots1:
        canvas.create_oval(cx-mode.r, cy-mode.r, cx+mode.r, cy+mode.r, fill = 'red', outline = '')
    for (cx, cy) in mode.drawnDots2:
        canvas.create_oval(cx-mode.r, cy-mode.r, cx+mode.r, cy+mode.r, fill = 'blue', outline = '')

    if mode.filled1 == True and mode.filled2 == True:
        canvas.create_text(mode.width//2, 20, text = f'score: {mode.score}')

runApp(width=1000, height=500)