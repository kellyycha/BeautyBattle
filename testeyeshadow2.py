from cmu_112_graphics import *
import math
import random

def appStarted(mode):
    mode.x = 170
    mode.y = 260
    mode.r = 10
    mode.drawnDots1 = []
    mode.drawnDots2 = []
    mode.directions = [+2,1,-1,-2]
    mode.dx = random.choice(mode.directions)
    mode.dy = random.choice(mode.directions)
    mode.centerx = 170
    mode.centery = 290
    mode.centerx2 = 160
    mode.centery2 = 370
    mode.draw1 = True
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
    
def distance(mode, x1, y1, x2, y2):
    return ((x1- x2)**2 + (y1-y2)**2)**0.5 + mode.r

def mousePressed(mode, event):
    print(f'{(event.x,event.y)},')

def moveDot(mode):
    if mode.draw1:
        mode.drawnDots1.append((mode.x,mode.y))

        xValues = []
        yValues = []
        for (x,y) in mode.drawnDots1:
            xValues.append(x)
            yValues.append(y)
        minX = min(xValues)
        maxX = max(xValues)
        minY = min(yValues)
        maxY = max(yValues)
        print(f"1: {minX},{maxX},{minY},{maxY}")
        if maxX-minX >= 50 and maxY-minY >=20:
            mode.filled1 = True
    
    elif mode.draw2:
        mode.centerx = 170 + 150
        mode.centerx2 = 160 + 150 + 20
        if mode.drawnDots2 == []:
            mode.x = 310
        mode.drawnDots2.append((mode.x,mode.y))

        xValues = []
        yValues = []
        for (x,y) in mode.drawnDots2:
            xValues.append(x)
            yValues.append(y)
        minX = min(xValues)
        maxX = max(xValues)
        minY = min(yValues)
        maxY = max(yValues)
        print(f"2: {minX},{maxX},{minY},{maxY}")
        if maxX-minX >= 50 and maxY-minY >=20:
            mode.filled2 = True
    
    if mode.x < 155 or mode.x > 335:
        mode.x -= mode.dx
        mode.y -= mode.dy
        mode.dx = random.choice(mode.directions)
        mode.dy = random.choice(mode.directions)
        print('3')
    
    if distance(mode, mode.centerx2, mode.centery2, mode.x, mode.y) <= 120:
        mode.x -= mode.dx
        mode.y -= mode.dy
        mode.dx = random.choice(mode.directions)
        mode.dy = random.choice(mode.directions)
        print('4')

    elif distance(mode, mode.centerx, mode.centery, mode.x, mode.y) <= 50:
        mode.x += mode.dx
        mode.y += mode.dy
        print('1')
    
    elif distance(mode, mode.centerx, mode.centery, mode.x, mode.y) > 50:
        mode.x -= mode.dx
        mode.y -= mode.dy
        mode.dx = random.choice(mode.directions)
        mode.dy = random.choice(mode.directions)
        print('2')

def redrawAll(mode, canvas):
    canvas.create_oval(170 - 50, 290 - 50, 170 + 50, 290 + 50)
    canvas.create_line(150, 0, 150, mode.height)
    canvas.create_oval(160 - 100, 370 - 100, 160 + 100, 370 + 100)

    canvas.create_oval(170 - 50 + 150, 290 - 50, 170 + 50 + 150, 290 + 50)
    canvas.create_line(340, 0, 340, mode.height)
    canvas.create_oval(160 + 20 - 100 + 150, 370 - 100, 160 + 20 + 100 + 150, 370 + 100)

    for (cx, cy) in mode.drawnDots1:
        canvas.create_oval(cx-mode.r, cy-mode.r, cx+mode.r, cy+mode.r, fill = 'red', outline = '')
    for (cx, cy) in mode.drawnDots2:
        canvas.create_oval(cx-mode.r, cy-mode.r, cx+mode.r, cy+mode.r, fill = 'blue', outline = '')

    #canvas.create_text(mode.width//2, 20, text = f'score: {mode.score}')

runApp(width=1000, height=500)
