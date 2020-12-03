from cmu_112_graphics import *
import math
import random

def appStarted(mode):
    mode.opponentPenX = 202
    mode.opponentPenY = 360
    mode.opponentR = 3

    mode.centerx = 220
    mode.centery = 340
    mode.centerx2 = 210
    mode.centery2 = 365
    mode.centerx3 = 230
    mode.centery3 = 365

    mode.drawnLipstick = []
    mode.drawingLipstick = False
    mode.filledLipstick = False

    mode.timerDelay = 50


def timerFired(mode):
    #blush
    if mode.filledLipstick == False:
        mode.drawingLipstick = True
        moveEasyAI(mode)
    elif mode.filledLipstick == True:
        print('done')
        mode.drawingLipstick = False

def distance(mode, x1, y1, x2, y2):
    return ((x1- x2)**2 + (y1-y2)**2)**0.5 + mode.opponentR

def moveEasyAI(mode):
    mode.drawnLipstick.append((mode.opponentPenX,mode.opponentPenY))
    
    if len(mode.drawnLipstick) >= 46 and distance(mode, mode.centerx3, mode.centery3, mode.opponentPenX, mode.opponentPenY) < 15:
        mode.opponentPenX -= 1
        mode.opponentPenY -= 2
        print('3')
 
    if distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 30:
        mode.opponentPenY += 1
        #mode.opponentPenX += 1
        print('1')

    if distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 30 and\
        (distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) < 15 or \
        distance(mode, mode.centerx3, mode.centery3, mode.opponentPenX, mode.opponentPenY) < 15):
        mode.opponentPenX += 1
        mode.opponentPenY -= 1
        print('2')


    #if distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) > 15 and \
     #   distance(mode, mode.centerx3, mode.centery3, mode.opponentPenX, mode.opponentPenY) > 15 and \
     #   distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 30

def redrawAll(mode, canvas):
    canvas.create_oval(220 - 30, 340 - 30, 220 + 30, 340 + 30)
    canvas.create_oval(220-10 - 13, 365 - 13, 220-10 + 13, 365 + 13)
    canvas.create_oval(220+10 - 13, 365 - 13, 220+10 + 13, 365 + 13)
        
    for (cx, cy) in mode.drawnLipstick:
        canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                    fill = 'red', outline = '')   


runApp(width=1000, height=500)