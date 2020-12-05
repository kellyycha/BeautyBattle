from cmu_112_graphics import *
import math
import random

def appStarted(mode):
    mode.opponentPenX = 160
    mode.opponentPenY = 330
    mode.opponentR = 10
    mode.opponentScore = 100

    mode.centerx = 170
    mode.centery = 330

    mode.drawnBlushL = []
    mode.drawnBlushR = []
    mode.drawingBlushL = False
    mode.drawingBlushR = False
    mode.filledBlushL = False
    mode.filledBlushR = False
    mode.opponentBlushLScore = 100
    mode.opponentBlushRScore = 100

    mode.timerDelay = 50


def timerFired(mode):
    #blush
    if mode.filledBlushL == False:
        mode.drawingBlushL = True
        moveEasyAI(mode)
    elif mode.filledBlushL == True and mode.filledBlushR == False:
        mode.drawingBlushL = False
        mode.drawingBlushR = True
        moveEasyAI(mode)
    elif mode.filledBlushR == True:
        mode.drawingBlushR = False

def distance(mode, x1, y1, x2, y2):
    return ((x1- x2)**2 + (y1-y2)**2)**0.5 + mode.opponentR

def moveEasyAI(mode):
    if mode.drawingBlushL:
        mode.centerx = 170
        mode.centery = 330
        mode.drawnBlushL.append((mode.opponentPenX,mode.opponentPenY))

        if len(mode.drawnBlushL) >= 77:
            mode.filledBlushL = True

        if distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 23:
            mode.drawnBlushL.pop()
            
    elif mode.drawingBlushR:
        mode.centerx = 265
        if mode.drawnBlushR == []:
            mode.opponentPenX = 255
            mode.opponentPenY = 330
        mode.drawnBlushR.append((mode.opponentPenX,mode.opponentPenY))
                
        if len(mode.drawnBlushL) >= 77:
            mode.filledBlushL = True
        
        if distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 23:
            mode.drawnBlushR.pop()

            
    if mode.drawingBlushL or mode.drawingBlushR:
        if distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 20 and mode.opponentPenY >= 330:
            mode.opponentPenY += 1
        elif distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 20 and mode.opponentPenY < 330:
            mode.opponentPenY -= 1
        elif distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) >= 20 and mode.opponentPenY >= 330:
            mode.opponentPenX += 1
            mode.opponentPenY -= 1
        elif distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) >= 20 and mode.opponentPenY < 330:
            mode.opponentPenX -= 1
        

def redrawAll(mode, canvas):
    canvas.create_oval(170 - 20, 330 - 20, 170 + 20, 330 + 20)

    canvas.create_oval(265 - 20, 330 - 20, 265 + 20, 330 + 20)
        
    for (cx, cy) in mode.drawnBlushL:
        canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                    fill = 'red', outline = '')   
    for (cx, cy) in mode.drawnBlushR:
        canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                    fill = 'red', outline = '')


runApp(width=1000, height=500)