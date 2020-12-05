from cmu_112_graphics import *
import math
import random

def appStarted(mode):
    mode.opponentPenX = 170
    mode.opponentPenY = 330
    mode.opponentR = 3

    mode.centerx = 170
    mode.centery = 330
    mode.centerx2 = 160
    mode.centery2 = 375 
    mode.direction = 1
    
    mode.drawnEyeshadowL = []
    mode.drawnEyeshadowR = []
    mode.drawingEyeshadowL = False
    mode.drawingEyeshadowR = False
    mode.filledEyeshadowL = False
    mode.filledEyeshadowR = False

def timerFired(mode):
    if mode.filledEyeshadowL == False:
        mode.drawingEyeshadowL = True
        moveEasyAI(mode)
    elif mode.filledEyeshadowL == True and mode.filledEyeshadowR == False: 
        mode.drawingEyeshadowL = False
        mode.drawingEyeshadowR = True
        moveEasyAI(mode)
    elif mode.filledEyeshadowR == True:
        mode.drawingEyeshadowR = False
    
def distance(mode, x1, y1, x2, y2):
    return ((x1- x2)**2 + (y1-y2)**2)**0.5 + mode.opponentR

def mousePressed(mode, event):
    print(f'{(event.x,event.y)},')

def moveEasyAI(mode):
    if mode.drawingEyeshadowL:
        mode.centerx = 160
        mode.centery = 313
        direction = 1
        eyeshadowList = mode.drawnEyeshadowL
        if mode.drawnEyeshadowL == []:
            mode.opponentPenX = 192
            mode.opponentPenY = 279
        mode.drawnEyeshadowL.append((mode.opponentPenX,mode.opponentPenY))
        #if len(mode.drawnEyeshadowL) >= 70:
        #    mode.filledEyeshadowL = True
            
    elif mode.drawingEyeshadowR:
        mode.centerx = 160 + 120
        mode.centerx2 = 160 + 120
        direction = -1
        eyeshadowList = mode.drawnEyeshadowR
        if mode.drawnEyeshadowR == []:
            mode.opponentPenX = 248
            mode.opponentPenY = 279
        mode.drawnEyeshadowR.append((mode.opponentPenX,mode.opponentPenY))
        #if len(mode.drawnEyeshadowR) >= 70:
        #    mode.filledEyeshadowR = True

    if mode.drawingEyeshadowL or mode.drawingEyeshadowR:

        if len(eyeshadowList) < 50 and distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 50:
            mode.opponentPenX -= 1 * direction
            #mode.opponentPenY -= 1
            print('1')
            
        elif len(eyeshadowList) < 50 and distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 50:
            mode.opponentPenY += 1
            #mode.opponentPenX -= 1 * direction
            print('2')
        
        if (mode.opponentPenX <= 150 or mode.opponentPenX >=290) and distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) > 105:
            mode.opponentPenX += 1 * direction
            #mode.opponentPenY += 1.5
            print('3')
        
        if len(eyeshadowList) > 50 and distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 50: 
            #mode.opponentPenX += 1 * direction
            mode.opponentPenY += 1
            print('4')

        if len(eyeshadowList) > 50 and distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) <= 105:
            mode.opponentPenX += 1 * direction
            #mode.opponentPenY -= 1
            print('5')
    

def redrawAll(mode, canvas):
    canvas.create_oval(160 - 50, 313 - 50, 160 + 50, 313 + 50)
    canvas.create_line(150, 0, 150, mode.height)
    canvas.create_oval(160 - 100, 375 - 100, 160 + 100, 375 + 100)

    canvas.create_oval(160 + 120 - 50, 313 - 50, 160 + 120 + 50, 313 + 50)
    canvas.create_line(290, 0, 290, mode.height)
    canvas.create_oval(160 + 120 - 100, 375 - 100, 160 + 120 + 100, 375 + 100)

    for (cx, cy) in mode.drawnEyeshadowL:            
        canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                fill = 'red', outline = '')   
        
    for (cx, cy) in mode.drawnEyeshadowR:
        canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                fill = 'red', outline = '')   

    #canvas.create_text(mode.width//2, 20, text = f'score: {mode.score}')

runApp(width=1000, height=500)
