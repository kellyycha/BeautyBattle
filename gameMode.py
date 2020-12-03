from cmu_112_graphics import *
from tkinter import *
import random
import math
from startMode import *

class GameMode(Mode):

    def appStarted(mode):
        mode.cx, mode.cy = mode.width // 2, mode.height // 2
        #background
        mode.background = mode.loadImage("images/background.jpg")

        # Customers generated with: https://www.cartoonify.de/#cartoonify
        customers = ["customer1.png", "customer2.png", "customer3.png","customer4.png","customer5.png","customer6.png"]
        customer = random.choice(customers)
        mode.customer = mode.scaleImage(mode.loadImage(f"images/customers/{customer}"), 2/3)

        #three different modes in the game
        mode.customerScreen = True
        mode.gameScreen = False
        mode.scoringScreen = False

        #timer 
        mode.timeLeft = 61
        mode.timerCount = 0
        mode.timeEnd = False
        mode.pause = False

        #selected product
        mode.eyeshadowSelection = False
        mode.blushSelection = False
        mode.lipstickSelection = False
        mode.eraserSelection = False

        # Eyeshadow image: http://clipart-library.com/clipart/1401830.htm 
        mode.eyeshadow = mode.scaleImage(mode.loadImage("images/eyeshadow.png"), 1/6)
        # Blush image: https://webstockreview.net/pict/getfirst 
        mode.blush = mode.scaleImage(mode.loadImage("images/blush.png"), 1/5)
        # Lipstick image: https://pngriver.com/pink-lipstick-png-transparent-clipart-image-2-5461/women-lipstick-png-transparent-images-transparent-backgrounds-pink-lipstick-png-12/ 
        mode.lipstick = mode.scaleImage(mode.loadImage("images/lipstick.png"), 1/9)
        # Eraser image: http://clipart-library.com/clipart/15308.htm 
        mode.erase = mode.scaleImage(mode.loadImage("images/erase.png"), 1/5)

        #color picker
        mode.eyeshadowColors = ["pink", "orange", "gold", "green", "blue", "purple"]
        mode.eyeshadowColorNames = ["hot pink", "dark orange", "gold", "yellow green", "deep sky blue", "medium orchid"]
        mode.eyeshadowColor = random.choice(mode.eyeshadowColors)

        eyeshadowIndex = mode.eyeshadowColors.index(mode.eyeshadowColor)
        mode.correctEyeshadowColor = mode.eyeshadowColorNames[eyeshadowIndex]

        mode.blushColors = ["pink", "red", "peach", "orange"]
        mode.blushColorNames = ["hot pink", "red", "salmon", "dark orange"]
        mode.blushColor = random.choice(mode.blushColors)

        blushIndex = mode.blushColors.index(mode.blushColor)
        mode.correctBlushColor = mode.blushColorNames[blushIndex]

        mode.lipstickColors = ["pink", "red", "nude", "purple"]
        mode.lipstickColorNames = ["hot pink", "red", "LightSalmon2", "medium orchid"]
        mode.lipstickColor = random.choice(mode.lipstickColors)   

        lipstickIndex = mode.lipstickColors.index(mode.lipstickColor)
        mode.correctLipstickColor = mode.lipstickColorNames[lipstickIndex]

        #drawing
        mode.penX = mode.penY = mode.penR = 0
        mode.selectedColor = '' 
        mode.colorShow = False
        mode.yourScore = 100
        mode.drawnEyeshadowLDots = []
        mode.drawnEyeshadowRDots = []
        mode.yourEyeshadowLScore = 100
        mode.yourEyeshadowRScore = 100
        mode.drawnBlushLDots = []
        mode.drawnBlushRDots = []
        mode.yourBlushLScore = 100
        mode.yourBlushRScore = 100
        mode.drawnLipstickDots = []
        mode.yourLipstickScore = 100
        mode.drawnTotalDots = []

        #AI
        mode.opponentPenX = 170
        mode.opponentPenY = 330
        mode.opponentR = 0
        mode.directions = [+1,2,-2,-1]
        mode.dx = random.choice(mode.directions)
        mode.dy = random.choice(mode.directions)
        mode.opponentScore = 100

        mode.centerx = 170
        mode.centery = 330
        mode.centerx2 = 160
        mode.centery2 = 375
        mode.centerx3 = 230
        mode.centery3 = 365 

        mode.drawnBlushL = []
        mode.drawnBlushR = []
        mode.drawingBlushL = False
        mode.drawingBlushR = False
        mode.filledBlushL = False
        mode.filledBlushR = False
        mode.opponentBlushLScore = 100
        mode.opponentBlushRScore = 100

        mode.drawnEyeshadowL = []
        mode.drawnEyeshadowR = []
        mode.drawingEyeshadowL = False
        mode.drawingEyeshadowR = False
        mode.filledEyeshadowL = False
        mode.filledEyeshadowR = False
        mode.opponentEyeshadowLScore = 100
        mode.opponentEyeshadowRScore = 100

        mode.drawnLipstick = []
        mode.drawingLipstick = False
        mode.filledLipstick = False
        mode.opponentLipstickScore = 100
        
    def mousePressed(mode, event):
        print(f'{(event.x,event.y)},')
        if mode.pause == False:
            if mode.customerScreen:
                #start the game
                if (670 <= event.x <= 775) and (370 <= event.y < 425):
                    mode.customerScreen = False
                    mode.gameScreen = True
                    mode.scoringScreen = False
 
            if mode.gameScreen:
                #submit button
                if (420 <= event.x <= 520) and (310 <= event.y < 353):
                    mode.scoringScreen = True
                    mode.gameScreen = False
                    mode.customerScreen = False
                    GameMode.calculateYourScore(mode)
                    GameMode.calculateOpponentScore(mode)
                #eyeshadow selected
                elif (mode.width - 100 <= event.x <= mode.width) and (0 <= event.y < 125):
                    mode.eyeshadowSelection = True
                    mode.blushSelection = False
                    mode.lipstickSelection = False
                    mode.eraserSelection = False
                    mode.colorShow = False
                    mode.penR = 3
                #blush selected
                elif (mode.width - 100 <= event.x <= mode.width) and (125 <= event.y < 250):
                    mode.eyeshadowSelection = False
                    mode.blushSelection = True
                    mode.lipstickSelection = False
                    mode.eraserSelection = False
                    mode.colorShow = False
                    mode.penR = 10
                #lipstick selected
                elif (mode.width - 100 <= event.x <= mode.width) and (250 <= event.y < 375):
                    mode.eyeshadowSelection = False
                    mode.blushSelection = False
                    mode.lipstickSelection = True
                    mode.eraserSelection = False
                    mode.colorShow = False
                    mode.penR = 3
                #eraser selected
                elif (mode.width - 100 <= event.x <= mode.width) and (375 <= event.y < 500):
                    mode.eyeshadowSelection = False
                    mode.blushSelection = False
                    mode.lipstickSelection = False
                    mode.eraserSelection = True
                    mode.colorShow = False
                    mode.penR = 5
                    mode.selectedColor = ''
                #pick eyeshadow color
                if mode.eyeshadowSelection:
                    for i in range(len(mode.eyeshadowColorNames)):
                        if (850 <= event.x <= 900) and (i*50 <= event.y < (i+1)*50):
                            mode.colorShow = False
                            mode.selectedColor = mode.eyeshadowColorNames[i]
                #pick blush color
                if mode.blushSelection:
                    for i in range(len(mode.blushColorNames)):
                        if (850 <= event.x <= 900) and (125 + i*50 <= event.y < 125 + (i+1)*50):
                            mode.colorShow = False
                            mode.selectedColor = mode.blushColorNames[i]
                #pick lipstick color
                if mode.lipstickSelection:
                    for i in range(len(mode.lipstickColorNames)):
                        if (850 <= event.x <= 900) and (250 + i*50 <= event.y < 250 + (i+1)*50):
                            mode.colorShow = False
                            mode.selectedColor = mode.lipstickColorNames[i]
        
        #restart button
        if mode.scoringScreen == True and (320 <= event.x <= 680) and (440 <= event.y < 480):
            mode.app.startMode.appStarted()
            mode.app.gameMode.appStarted()
            mode.app.setActiveMode(mode.app.startMode)

    def mouseDragged(mode, event):
        if mode.pause == False and mode.timeEnd == False:
            if mode.gameScreen:
                if (600 <= event.x <= 780) and (190 <= event.y < 390):
                    mode.colorShow = True
                    mode.penX = event.x
                    mode.penY = event.y
                    if mode.selectedColor != '':
                        mode.drawnTotalDots.append((event.x, event.y, mode.penR, mode.selectedColor))
                        if mode.eyeshadowSelection:
                            if event.x > 690:
                                mode.drawnEyeshadowRDots.append((event.x, event.y, mode.penR, mode.selectedColor)) 
                            else:
                                mode.drawnEyeshadowLDots.append((event.x, event.y, mode.penR, mode.selectedColor))
                        if mode.blushSelection:
                            if event.x > 690:
                                mode.drawnBlushRDots.append((event.x, event.y, mode.penR, mode.selectedColor))
                            else:
                                mode.drawnBlushLDots.append((event.x, event.y, mode.penR, mode.selectedColor))
                        if mode.lipstickSelection:
                            mode.drawnLipstickDots.append((event.x, event.y, mode.penR, mode.selectedColor))
                if mode.eraserSelection:
                    GameMode.eraserIntersect(mode) #erasing

    def eraserIntersect(mode):
        for (cx, cy, r, color) in mode.drawnTotalDots:
            distanceFormula = ((mode.penX - cx)**2 + (mode.penY - cy)**2)**0.5
            if (distanceFormula <= mode.penR + r):
                mode.drawnTotalDots.remove((cx, cy, r, color))
                if (cx, cy, r, color) in mode.drawnEyeshadowLDots:
                    mode.drawnEyeshadowLDots.remove((cx, cy, r, color))
                elif (cx, cy, r, color) in mode.drawnEyeshadowRDots:
                    mode.drawnEyeshadowRDots.remove((cx, cy, r, color))
                elif (cx, cy, r, color) in mode.drawnBlushLDots:
                    mode.drawnBlushLDots.remove((cx, cy, r, color))
                elif (cx, cy, r, color) in mode.drawnBlushRDots:
                    mode.drawnBlushRDots.remove((cx, cy, r, color))
                elif (cx, cy, r, color) in mode.drawnLipstickDots:
                    mode.drawnLipstickDots.remove((cx, cy, r, color))


    def keyPressed(mode, event):
        if event.key == "f":
            mode.filledBlushL = True
            mode.filledBlushR = True
            mode.drawingBlushL = False
            mode.drawingBlushR = False
        
        if event.key == "g":
            mode.filledEyeshadowL = True
            mode.filledEyeshadowR = True
            mode.drawingEyeshadowL = False
            mode.drawingEyeshadowR = False

        if event.key == "h":    #help
            mode.app.setActiveMode(mode.app.helpMode)

        if event.key == "p":    #pause
            mode.pause = not mode.pause
        
        if event.key == 'q':
            print(f'eyeshadow:{mode.drawnEyeshadowDots}')
            print(f'blush:{mode.drawnBlushDots}')
            print(f'lipstick:{mode.drawnLipstickDots}')
            print(f'total:{mode.drawnTotalDots}')

    def timerFired(mode):
        if mode.pause == False:
            if mode.gameScreen:
                #countdown every second
                if mode.timeLeft > 0.1:
                    mode.timeLeft -= 0.1
                else:
                    mode.timeLeft = 0
                    mode.timeEnd = True
                        
                if StartMode.easy:
                    GameMode.easyAI(mode)
                
                elif StartMode.medium:
                    GameMode.mediumAI(mode)
                
                elif StartMode.hard:
                    GameMode.hardAI(mode)
                
                mode.timerCount += 1

        #automatically shows the scoring screen 2 seconds after time ends
        if mode.scoringScreen == False and mode.timerCount > 63*10: 
            GameMode.calculateYourScore(mode)
            GameMode.calculateOpponentScore(mode)
            mode.scoringScreen = True
            mode.gameScreen = False
        
    def distance(mode, x1, y1, x2, y2):
        return ((x1- x2)**2 + (y1-y2)**2)**0.5 + mode.opponentR

    def easyAI(mode):
        #start other eye 25 seconds left
        if mode.timeLeft <= 25 and mode.filledEyeshadowR == False and mode.drawingEyeshadowL == True:            
            mode.filledEyeshadowL = True
            mode.drawingEyeshadowL = False
            mode.drawingEyeshadowR = True
            GameMode.moveEasyAI(mode)
        #start lips if 15 seconds left
        if mode.timeLeft <= 15 and mode.filledLipstick == False and mode.drawingEyeshadowR == True:            
            mode.filledEyeshadowR = True
            mode.drawingEyeshadowR = False
            mode.drawingLipstick = True
            GameMode.moveEasyAI(mode)
        
        #blush
        if mode.filledBlushL == False:
            mode.drawingBlushL = True
            GameMode.moveEasyAI(mode)
        elif mode.filledBlushL == True and mode.filledBlushR == False:
            mode.drawingBlushL = False
            mode.drawingBlushR = True
            GameMode.moveEasyAI(mode)
        #eyeshadow
        elif mode.filledBlushR == True and mode.filledEyeshadowL == False:
            mode.drawingBlushR = False
            mode.drawingEyeshadowL = True
            GameMode.moveEasyAI(mode)
        elif mode.filledEyeshadowL == True and mode.filledEyeshadowR == False: 
            mode.drawingEyeshadowL = False
            mode.drawingEyeshadowR = True
            GameMode.moveEasyAI(mode)
        #lipstick
        elif mode.filledEyeshadowR == True and mode.filledLipstick == False:
            mode.drawingEyeshadowR = False
            mode.drawingLipstick = True
            GameMode.moveEasyAI(mode)
        
        #time is up
        if mode.timeLeft == 0:
            mode.drawingLipstick = False

    def moveEasyAI(mode):
        #blush
        if mode.drawingBlushL:
            mode.centerx = 170
            mode.centery = 330
            mode.drawnBlushL.append((mode.opponentPenX,mode.opponentPenY))

            xValues = []
            for (x,y) in mode.drawnBlushL:
                xValues.append(x)
            minX = min(xValues)
            maxX = max(xValues)
            if maxX-minX >= 22:
                mode.filledBlushL = True
        
        elif mode.drawingBlushR:
            mode.centerx = 265
            if mode.drawnBlushR == []:
                mode.opponentPenX = 265
            mode.drawnBlushR.append((mode.opponentPenX,mode.opponentPenY))
            
            xValues = []
            for (x,y) in mode.drawnBlushR:
                xValues.append(x)
            minX = min(xValues)
            maxX = max(xValues)
            if maxX-minX >= 22:
                mode.filledBlushR = True
        
        if mode.drawingBlushL or mode.drawingBlushR:
            if GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 20:
                mode.opponentPenX += mode.dx
                mode.opponentPenY += mode.dy
            elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 20:
                mode.opponentPenX -= mode.dx
                mode.opponentPenY -= mode.dy
                mode.dx = random.choice(mode.directions)
                mode.dy = random.choice(mode.directions)

        #eyeshadow
        if mode.drawingEyeshadowL:
            mode.centerx = 160
            mode.centery = 313
            if mode.drawnEyeshadowL == []:
                mode.opponentPenX = 165
                mode.opponentPenY = 270
            mode.drawnEyeshadowL.append((mode.opponentPenX,mode.opponentPenY))
            
            xValues = []
            for (x,y) in mode.drawnEyeshadowL:
                xValues.append(x)
            minX = min(xValues)
            maxX = max(xValues)
            if maxX-minX >= 45:
                mode.filledEyeshadowL = True

        elif mode.drawingEyeshadowR:
            mode.centerx = 160 + 120
            mode.centerx2 = 160 + 120
            if mode.drawnEyeshadowR == []:
                mode.opponentPenX = 265
                mode.opponentPenY = 270
            mode.drawnEyeshadowR.append((mode.opponentPenX,mode.opponentPenY))
            
            xValues = []
            for (x,y) in mode.drawnEyeshadowR:
                xValues.append(x)
            minX = min(xValues)
            maxX = max(xValues)
            if maxX-minX >= 45:
                mode.filledEyeshadowR = True

        if mode.drawingEyeshadowL or mode.drawingEyeshadowR:
            if mode.opponentPenX < 155:
                mode.opponentPenX += 2
                mode.dx = random.choice(mode.directions)
                mode.dy = random.choice(mode.directions)
            if mode.opponentPenX > 285:
                mode.opponentPenX -= 2
                mode.dx = random.choice(mode.directions)
                mode.dy = random.choice(mode.directions)
            
            if GameMode.distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) <= 105:
                mode.opponentPenX -= mode.dx
                mode.opponentPenY = mode.opponentPenY - 1
                mode.dx = random.choice(mode.directions)
                mode.dy = random.choice(mode.directions)

            elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 50:
                mode.opponentPenX += 2*mode.dx
                mode.opponentPenY += mode.dy
            
            elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 50:
                mode.opponentPenX -= mode.dx
                mode.opponentPenY = mode.opponentPenY + 1
                mode.dx = random.choice(mode.directions)
                mode.dy = random.choice(mode.directions)
        
        #lipstick
        if mode.drawingLipstick:
            mode.centerx = 220
            mode.centery = 340
            mode.centerx2 = 210
            mode.centery2 = 365
            if mode.drawnLipstick == []:
                mode.opponentPenX = 220
                mode.opponentPenY = 365
            mode.drawnLipstick.append((mode.opponentPenX,mode.opponentPenY))
            
            if GameMode.distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) >= 13 and \
                GameMode.distance(mode, mode.centerx3, mode.centery3, mode.opponentPenX, mode.opponentPenY) <= 13 and \
                GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 30:
                mode.opponentPenX += mode.dx
                mode.opponentPenY += mode.dy
            
            elif GameMode.distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) <= 13 and \
                GameMode.distance(mode, mode.centerx3, mode.centery3, mode.opponentPenX, mode.opponentPenY) >= 13 and \
                GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 30:
                mode.opponentPenX += mode.dx
                mode.opponentPenY += mode.dy
                
            else:
                mode.opponentPenX -= mode.dx
                mode.opponentPenY -= mode.dy
                mode.dx = random.choice(mode.directions)
                mode.dy = random.choice(mode.directions)
        
    def mediumAI(mode):
        pass
    
    def moveMediumAI(mode):
        pass

    def hardAI(mode):
        #blush
        if mode.filledBlushL == False:
            mode.drawingBlushL = True
            GameMode.moveHardAI(mode)
        elif mode.filledBlushL == True and mode.filledBlushR == False:
            mode.drawingBlushL = False
            mode.drawingBlushR = True
            GameMode.moveHardAI(mode)
        elif mode.filledBlushR == True:
            mode.drawingBlushR = False
    
    def moveHardAI(mode):
        if mode.drawingBlushL:
            mode.centerx = 170
            mode.centery = 330
            if mode.drawnBlushL == []:
                mode.opponentPenX = 160
                mode.opponentPenY = 330
            mode.drawnBlushL.append((mode.opponentPenX,mode.opponentPenY))

            if len(mode.drawnBlushL) >= 77:
                mode.filledBlushL = True

            if GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 23:
                mode.drawnBlushL.pop()
                
        elif mode.drawingBlushR:
            mode.centerx = 265
            if mode.drawnBlushR == []:
                mode.opponentPenX = 255
                mode.opponentPenY = 330
            mode.drawnBlushR.append((mode.opponentPenX,mode.opponentPenY))
     
            if len(mode.drawnBlushL) >= 77:
                mode.filledBlushL = True

            if GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 23:
                mode.drawnBlushR.pop()

        if mode.drawingBlushL or mode.drawingBlushR:
            if GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 20 and mode.opponentPenY >= 330:
                mode.opponentPenY += 1
            elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 20 and mode.opponentPenY < 330:
                mode.opponentPenY -= 1
            elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) >= 20 and mode.opponentPenY >= 330:
                mode.opponentPenX += 1
                mode.opponentPenY -= 1
            elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) >= 20 and mode.opponentPenY < 330:
                mode.opponentPenX -= 1

    def calculateOpponentScore(mode):
        blushLXValuesO = []
        blushLYValuesO = []
        for (x,y) in mode.drawnBlushL:
            blushLXValuesO.append(x)
            blushLYValuesO.append(y)
        if len(blushLXValuesO) > 0:
            blushLMinXO = min(blushLXValuesO)
            blushLMaxXO = max(blushLXValuesO)
            blushLMinYO = min(blushLYValuesO)
            blushLMaxYO = max(blushLYValuesO)
            print(f'len L blush {len(blushLXValuesO)}')
        
            if blushLMaxXO-blushLMinXO >= 22 and blushLMaxYO-blushLMinYO >= 22: 
                mode.opponentBlushLScore = 100
            if blushLMaxYO-blushLMinYO < 22:
                mode.opponentBlushLScore -= (22 - (blushLMaxYO-blushLMinYO))
            
        elif blushLXValuesO == []:
            mode.opponentBlushLScore = 0

        blushRXValuesO = []
        blushRYValuesO = []
        for (x,y) in mode.drawnBlushR:
            blushRXValuesO.append(x)
            blushRYValuesO.append(y)
        if len(blushRXValuesO) > 0:
            blushRMinXO = min(blushRXValuesO)
            blushRMaxXO = max(blushRXValuesO)
            blushRMinYO = min(blushRYValuesO)
            blushRMaxYO = max(blushRYValuesO)
            print(f'len R blush {len(blushRXValuesO)}')

            if blushRMaxXO-blushRMinXO >= 22 and blushRMaxYO-blushRMinYO >= 22: 
                mode.opponentBlushRScore = 100
            if blushRMaxYO-blushRMinYO < 22:
                mode.opponentBlushRScore -= (22 - (blushRMaxYO-blushRMinYO))
            
        elif blushRXValuesO == []:
            mode.opponentBlushRScore = 0
        
        eyeshadowLXValuesO = []
        eyeshadowLYValuesO = []
        for (x,y) in mode.drawnEyeshadowL:
            eyeshadowLXValuesO.append(x)
            eyeshadowLYValuesO.append(y)
        if len(eyeshadowLXValuesO) > 0:
            eyeshadowLMinXO = min(eyeshadowLXValuesO)
            eyeshadowLMaxXO = max(eyeshadowLXValuesO)
            eyeshadowLMinYO = min(eyeshadowLYValuesO)
            eyeshadowLMaxYO = max(eyeshadowLYValuesO)
            print(eyeshadowLMinYO, eyeshadowLMaxYO)
            print(f'len L eye {len(eyeshadowLXValuesO)}')

            if (eyeshadowLMaxXO-eyeshadowLMinXO >= 45 and eyeshadowLMaxYO-eyeshadowLMinYO >= 15 and
                eyeshadowLMaxXO-eyeshadowLMinXO < 48 and eyeshadowLMaxYO-eyeshadowLMinYO < 17 and
                len(eyeshadowLXValuesO) > 200): 
                mode.opponentEyeshadowLScore = 100
            if len(eyeshadowLXValuesO) <= 200:
                mode.opponentEyeshadowLScore -= 10
            if eyeshadowLMaxXO-eyeshadowLMinXO >= 48: 
                mode.opponentEyeshadowLScore -= ((eyeshadowLMaxXO-eyeshadowLMinXO) - 48)
            if eyeshadowLMaxYO-eyeshadowLMinYO >= 17:
                mode.opponentEyeshadowLScore -= ((eyeshadowLMaxYO-eyeshadowLMinYO) - 17)
            if eyeshadowLMaxYO-eyeshadowLMinYO < 15:
                mode.opponentEyeshadowLScore -= (15 - (eyeshadowLMaxYO-eyeshadowLMinYO))
            if eyeshadowLMaxXO-eyeshadowLMinXO < 45: 
                mode.opponentEyeshadowLScore -= (45 - (eyeshadowLMaxXO-eyeshadowLMinXO))

        elif eyeshadowLXValuesO == []:
            mode.opponentEyeshadowLScore = 0
        
        eyeshadowRXValuesO = []
        eyeshadowRYValuesO = []
        for (x,y) in mode.drawnEyeshadowR:
            eyeshadowRXValuesO.append(x)
            eyeshadowRYValuesO.append(y)
        if len(eyeshadowRXValuesO) > 0:
            eyeshadowRMinXO = min(eyeshadowRXValuesO)
            eyeshadowRMaxXO = max(eyeshadowRXValuesO)
            eyeshadowRMinYO = min(eyeshadowRYValuesO)
            eyeshadowRMaxYO = max(eyeshadowRYValuesO)
            print(eyeshadowRMinYO, eyeshadowRMaxYO)
            print(f'len R eye {len(eyeshadowRXValuesO)}')

            if (eyeshadowRMaxXO-eyeshadowRMinXO >= 45 and eyeshadowRMaxYO-eyeshadowRMinYO >= 15 and
                eyeshadowRMaxXO-eyeshadowRMinXO < 48 and eyeshadowRMaxYO-eyeshadowRMinYO < 17 and
                len(eyeshadowLXValuesO) > 200): 
                mode.opponentEyeshadowRScore = 100
            if len(eyeshadowRXValuesO) <= 200:
                mode.opponentEyeshadowRScore -= 10
            if eyeshadowRMaxXO-eyeshadowRMinXO >= 48: 
                mode.opponentEyeshadowRScore -= ((eyeshadowRMaxXO-eyeshadowRMinXO) - 48)
            if eyeshadowRMaxYO-eyeshadowRMinYO >= 17:
                mode.opponentEyeshadowRScore -= ((eyeshadowRMaxYO-eyeshadowRMinYO) - 17)
            if eyeshadowRMaxYO-eyeshadowRMinYO < 15:
                mode.opponentEyeshadowRScore -= (15 - (eyeshadowRMaxYO-eyeshadowRMinYO))
            if eyeshadowRMaxXO-eyeshadowRMinXO < 45: 
                mode.opponentEyeshadowRScore -= (45 - (eyeshadowRMaxXO-eyeshadowRMinXO))

        elif eyeshadowRXValuesO == []:
            mode.opponentEyeshadowRScore = 0

        lipstickXValuesO = []
        lipstickYValuesO = []
        for (x, y) in mode.drawnLipstick:
            lipstickXValuesO.append(x)
            lipstickYValuesO.append(y)
        if len(lipstickXValuesO) > 0:
            lipstickMinXO = min(lipstickXValuesO)
            lipstickMaxXO = max(lipstickXValuesO)
            lipstickMinYO = min(lipstickYValuesO)
            lipstickMaxYO = max(lipstickYValuesO)
            print(lipstickMinYO, lipstickMaxYO)
            print(f'len lip {len(lipstickXValuesO)}')

            if (lipstickMaxXO-lipstickMinXO >= 37 and lipstickMaxYO-lipstickMinYO >= 13 and
                lipstickMaxXO-lipstickMinXO < 39 and lipstickMaxYO-lipstickMinYO < 15 and
                len(lipstickXValuesO) > 200 ): 
                mode.opponentLipstickScore = 100
            if len(lipstickXValuesO) <= 200:
                mode.opponentLipstickScore -= 20
            if lipstickMaxXO-lipstickMinXO >= 39: 
                mode.opponentLipstickScore -= ((lipstickMaxXO-lipstickMinXO) - 39)
            if lipstickMaxYO-lipstickMinYO >= 15:
                mode.opponentLipstickScore -= ((lipstickMaxYO-lipstickMinYO) - 15)
            if lipstickMaxYO-lipstickMinYO < 13:
                mode.opponentLipstickScore -= (13 - (lipstickMaxYO-lipstickMinYO))
            if lipstickMaxXO-lipstickMinXO < 37: 
                mode.opponentLipstickScore -= (37 - (lipstickMaxXO-lipstickMinXO))

        elif lipstickXValuesO == []:
            mode.opponentLipstickScore = 0
        
        mode.opponentScore = (mode.opponentBlushLScore + mode.opponentBlushRScore \
                            + mode.opponentEyeshadowLScore + mode.opponentEyeshadowRScore \
                            + mode.opponentLipstickScore)//5

        if mode.opponentScore < 0:
            mode.opponentScore = 0
        
        print(mode.opponentBlushLScore,mode.opponentBlushRScore, \
              mode.opponentEyeshadowLScore, mode.opponentEyeshadowRScore, \
              mode.opponentLipstickScore)


    def calculateYourScore(mode):
        blushLXValues = []
        blushLYValues = []
        for (x,y,r,color) in mode.drawnBlushLDots:
            blushLXValues.append(x)
            blushLYValues.append(y)
        if len(blushLXValues) > 0:
            blushLMinX = min(blushLXValues)
            blushLMaxX = max(blushLXValues)
            blushLMinY = min(blushLYValues)
            blushLMaxY = max(blushLYValues)
            print(f"blushL: {blushLMinX, blushLMaxX, blushLMinY, blushLMaxY}")
        
            if (blushLMaxX-blushLMinX >= 20 and blushLMaxY-blushLMinY >= 20 and 
                blushLMaxX-blushLMinX < 23 and blushLMaxY-blushLMinY < 23 and
                blushLMinX > 625 and blushLMinY > 315): 
                mode.yourBlushLScore = 100
            if blushLMinX <= 625:
                mode.yourBlushLScore -= 10
            if blushLMinY <= 315:
                mode.yourBlushRScore -= 10
            if blushLMaxX-blushLMinX >= 23: 
                mode.yourBlushLScore -= ((blushLMaxX-blushLMinX) - 23)
            if blushLMaxY-blushLMinY >= 23:
                mode.yourBlushLScore -= ((blushLMaxY-blushLMinY) - 23)
            if blushLMaxY-blushLMinY < 20:
                mode.yourBlushLScore -= (20 - (blushLMaxY-blushLMinY))
            if blushLMaxX-blushLMinX < 20: 
                mode.yourBlushLScore -= (20 - (blushLMaxX-blushLMinX))
        
        elif blushLXValues == []:
            mode.yourBlushLScore = 0

        for (cx, cy, r, color) in mode.drawnBlushLDots:
            if color != mode.correctBlushColor:
                mode.yourBlushLScore -= 10

        blushRXValues = []
        blushRYValues = []
        for (x,y,r,color) in mode.drawnBlushRDots:
            blushRXValues.append(x)
            blushRYValues.append(y)
        if len(blushRXValues) > 0:
            blushRMinX = min(blushRXValues)
            blushRMaxX = max(blushRXValues)
            blushRMinY = min(blushRYValues)
            blushRMaxY = max(blushRYValues)
            print(f"blushR: {blushRMinX, blushRMaxX, blushRMinY, blushRMaxY}")
            
            if (blushRMaxX-blushRMinX >= 20 and blushRMaxY-blushRMinY >= 20 and
                blushRMaxX-blushRMinX <= 23 and blushRMaxY-blushRMinY <= 23 and
                blushRMinX > 720 and blushRMinY > 315): 
                mode.yourBlushRScore = 100
            if blushRMinX <= 720:
                mode.yourBlushRScore -= 10
            if blushRMinY <= 315:
                mode.yourBlushRScore -= 10
            if blushRMaxX-blushRMinX > 23: 
                mode.yourBlushRScore -= ((blushRMaxX-blushRMinX) - 20)
            if blushRMaxY-blushRMinY > 23:
                mode.yourBlushRScore -= ((blushRMaxY-blushRMinY) - 20)
            if blushRMaxY-blushRMinY < 20:
                mode.yourBlushRScore -= (20 - (blushRMaxY-blushRMinY))
            if blushRMaxX-blushRMinX < 20: 
                mode.yourBlushRScore -= (20 - (blushRMaxX-blushRMinX))
           
        elif blushRXValues == []:
            mode.yourBlushRScore = 0

        for (cx, cy, r, color) in mode.drawnBlushRDots:
            if color != mode.correctBlushColor:
                mode.yourBlushRScore -= 10
        
        eyeshadowLXValues = []
        eyeshadowLYValues = []
        for (x,y,r,color) in mode.drawnEyeshadowLDots:
            eyeshadowLXValues.append(x)
            eyeshadowLYValues.append(y)
        if len(eyeshadowLXValues) > 0:
            eyeshadowLMinX = min(eyeshadowLXValues)
            eyeshadowLMaxX = max(eyeshadowLXValues)
            eyeshadowLMinY = min(eyeshadowLYValues)
            eyeshadowLMaxY = max(eyeshadowLYValues)
            print(f"eyeL: {eyeshadowLMinX, eyeshadowLMaxX, eyeshadowLMinY, eyeshadowLMaxY}")
            print(f'your len L eye {len(eyeshadowLXValues)}')

            if (eyeshadowLMaxX-eyeshadowLMinX >= 48 and eyeshadowLMaxY-eyeshadowLMinY >= 17 and
                eyeshadowLMaxX-eyeshadowLMinX < 50 and eyeshadowLMaxY-eyeshadowLMinY < 20 and
                eyeshadowLMinX > 610 and eyeshadowLMinY > 260 and len(eyeshadowLXValues) >= 50):
                mode.yourEyeshadowLScore = 100
            if len(eyeshadowLXValues) < 50:
                mode.yourEyeshadowLScore -= 10
            if eyeshadowLMinX <= 610:
                mode.yourEyeshadowLScore -= 10
            if eyeshadowLMinY <= 260:
                mode.yourEyeshadowLScore -= 10
            if eyeshadowLMaxX-eyeshadowLMinX >= 50: 
                mode.yourEyeshadowLScore -= ((eyeshadowLMaxX-eyeshadowLMinX) - 50)
            if eyeshadowLMaxY-eyeshadowLMinY >= 20:
                mode.yourEyeshadowLScore -= ((eyeshadowLMaxY-eyeshadowLMinY) - 20)
            if eyeshadowLMaxY-eyeshadowLMinY < 17:
                mode.yourEyeshadowLScore -= (17 - (eyeshadowLMaxY-eyeshadowLMinY))
            if eyeshadowLMaxX-eyeshadowLMinX < 48: 
                mode.yourEyeshadowLScore -= (48 - (eyeshadowLMaxX-eyeshadowLMinX))

        elif eyeshadowLXValues == []:
            mode.yourEyeshadowLScore = 0

        for (cx, cy, r, color) in mode.drawnEyeshadowLDots:
            if color != mode.correctEyeshadowColor:
                mode.yourEyeshadowLScore -= 10
        
        eyeshadowRXValues = []
        eyeshadowRYValues = []
        for (x,y,r,color) in mode.drawnEyeshadowRDots:
            eyeshadowRXValues.append(x)
            eyeshadowRYValues.append(y)
        if len(eyeshadowRXValues) > 0:
            eyeshadowRMinX = min(eyeshadowRXValues)
            eyeshadowRMaxX = max(eyeshadowRXValues)
            eyeshadowRMinY = min(eyeshadowRYValues)
            eyeshadowRMaxY = max(eyeshadowRYValues)
            print(f"eyeR: {eyeshadowRMinX, eyeshadowRMaxX, eyeshadowRMinY, eyeshadowRMaxY}")
            print(f'your len R eye {len(eyeshadowRXValues)}')

            if (eyeshadowRMaxX-eyeshadowRMinX >= 48 and eyeshadowRMaxY-eyeshadowRMinY >= 17 and
                eyeshadowRMaxX-eyeshadowRMinX < 50 and eyeshadowRMaxY-eyeshadowRMinY < 20 and
                eyeshadowRMinX > 705 and eyeshadowRMinY > 260 and len(eyeshadowRXValues) >= 50):
                mode.yourEyeshadowRScore = 100
            if len(eyeshadowRXValues) < 50:
                mode.yourEyeshadowRScore -= 10
            if eyeshadowRMinX <= 705:
                mode.yourEyeshadowRScore -= 10
            if eyeshadowRMinY <= 260:
                mode.yourEyeshadowRScore -= 10
            if eyeshadowRMaxX-eyeshadowRMinX >= 50: 
                mode.yourEyeshadowRScore -= ((eyeshadowRMaxX-eyeshadowRMinX) - 50)
            if eyeshadowRMaxY-eyeshadowRMinY >= 20:
                mode.yourEyeshadowRScore -= ((eyeshadowRMaxY-eyeshadowRMinY) - 20)
            if eyeshadowRMaxY-eyeshadowRMinY < 17:
                mode.yourEyeshadowRScore -= (17 - (eyeshadowRMaxY-eyeshadowRMinY))
            if eyeshadowRMaxX-eyeshadowRMinX < 48: 
                mode.yourEyeshadowRScore -= (48 - (eyeshadowRMaxX-eyeshadowRMinX))

        elif eyeshadowRXValues == []:
            mode.yourEyeshadowRScore = 0

        for (cx, cy, r, color) in mode.drawnEyeshadowRDots:
            if color != mode.correctEyeshadowColor:
                mode.yourEyeshadowRScore -= 10

        lipstickXValues = []
        lipstickYValues = []
        for (x, y, r, color) in mode.drawnLipstickDots:
            lipstickXValues.append(x)
            lipstickYValues.append(y)
        if len(lipstickXValues) > 0:
            lipstickMinX = min(lipstickXValues)
            lipstickMaxX = max(lipstickXValues)
            lipstickMinY = min(lipstickYValues)
            lipstickMaxY = max(lipstickYValues)
            print(f'lips:{lipstickMinX,lipstickMaxX,lipstickMinY,lipstickMaxY}')
            print(f'your len lips {len(lipstickXValues)}')

            if (lipstickMaxX-lipstickMinX >= 38 and lipstickMaxY-lipstickMinY >= 13 and
                lipstickMaxX-lipstickMinX < 39 and lipstickMaxY-lipstickMinY < 15 and
                lipstickMinX > 665 and lipstickMinY > 350 and len(lipstickXValues) >= 80): 
                mode.yourLipstickScore = 100
            if len(lipstickXValues) < 80:
                mode.yourLipstickScore -= 10
            if lipstickMinX <= 665:
                mode.yourLipstickScore -= 10
            if lipstickMinY <= 350:
                mode.yourLipstickScore -= 10
            if lipstickMaxX-lipstickMinX >= 39: 
                mode.yourLipstickScore -= ((lipstickMaxX-lipstickMinX) - 39)
            if lipstickMaxY-lipstickMinY >= 15:
                mode.yourLipstickScore -= ((lipstickMaxY-lipstickMinY) - 15)
            if lipstickMaxY-lipstickMinY < 13:
                mode.yourLipstickScore -= (13 - (lipstickMaxY-lipstickMinY))
            if lipstickMaxX-lipstickMinX < 38: 
                mode.yourLipstickScore -= (38 - (lipstickMaxX-lipstickMinX))

        elif lipstickXValues == []:
            mode.yourLipstickScore = 0
        
        for (cx, cy, r, color) in mode.drawnLipstickDots:
            if color != mode.correctLipstickColor:
                mode.yourLipstickScore -= 10
        
        mode.yourScore = (mode.yourBlushLScore+mode.yourBlushRScore \
                        + mode.yourEyeshadowLScore+mode.yourEyeshadowRScore \
                        + mode.yourLipstickScore)//5
        if mode.yourScore < 0:
            mode.yourScore = 0
        print(f'your: {mode.yourBlushLScore,mode.yourBlushRScore, mode.yourEyeshadowLScore,mode.yourEyeshadowRScore,mode.yourLipstickScore}')

    def drawCustomerScreen(mode, canvas):
        canvas.create_text(mode.cx, 70, text = "A customer has arrived!", font = "Arial 50 bold", fill = "black")
        canvas.create_image(mode.cx - 150, mode.cy + 50, image = ImageTk.PhotoImage(mode.customer))
        canvas.create_oval(mode.cx + 225 + 220, mode.cy + 100, mode.cx + 225 - 220, mode.cy - 100, fill = "white", outline = "pink")
        canvas.create_text(mode.cx + 225, mode.cy, text = f"\"I would like \n{mode.eyeshadowColor} eyeshadow, \nwith {mode.blushColor} blush, \nand {mode.lipstickColor} lipstick.\"",
                                font = "Arial 30 bold")
        canvas.create_rectangle(mode.cx + 175, mode.height - 125, mode.cx + 275, mode.height - 75, fill = "pink", outline = "")
        canvas.create_text(mode.cx + 225, mode.height - 100, text = "Go!", font = "Arial 30 bold", fill = "black")

        #instructions to open help
        canvas.create_rectangle(10, mode.height - 45, 180, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Press H for Help", font = "Arial 20 bold", fill = "black")

    def drawGameScreen(mode, canvas):
        #timer
        canvas.create_line(mode.cx - 30, 0, mode.cx - 30, mode.height, fill = "black", width = 5)
        canvas.create_rectangle(mode.cx - 80 - 30, 0, mode.cx + 80 - 30, 40, fill = "white", outline = "black")
        canvas.create_text(mode.cx - 30, 20, text=f'{math.floor(mode.timeLeft)}s remaining', font="Arial 20 bold")

        #customer and order
        canvas.create_text(mode.cx // 2 - 30, 70, text=StartMode.name, font="Arial 30 bold")
        canvas.create_image(mode.cx // 2 - 30, mode.cy + 50, image = ImageTk.PhotoImage(mode.customer))
        canvas.create_text(mode.cx + mode.cx // 2 - 60, 70, text='You', font="Arial 30 bold")
        canvas.create_image(mode.cx + mode.cx // 2 - 60, mode.cy + 50, image = ImageTk.PhotoImage(mode.customer))
        canvas.create_rectangle(mode.cx - 100 - 30, 50, mode.cx + 100 - 30, 160, fill = "white", outline = "pink")
        canvas.create_text(mode.cx - 30, 60, text = f"Check List:\n- {mode.eyeshadowColor} eyeshadow\n- {mode.blushColor} blush\n- {mode.lipstickColor} lipstick",
                                font = "Arial 20", anchor = "n")
        
        #submit button
        canvas.create_rectangle(mode.cx - 50 - 30, mode.cy + mode.cy//3 - 20, mode.cx + 50 - 30, mode.cy + mode.cy//3 + 20, fill = "pink", outline = "")
        canvas.create_text(mode.cx - 30, mode.cy + mode.cy//3, text = "SUBMIT")
            
        #makeup products
        products = ["Eyeshadow", "Blush", "Lipstick", "Erase"]
        pictures = [mode.eyeshadow, mode.blush, mode.lipstick, mode.erase]
        for i in range(len(products)):
            boxHeight = mode.height // 4
            canvas.create_rectangle(mode.width - 100, i * boxHeight, mode.width, (i+1) * boxHeight, fill = "pink", outline = "black")
            canvas.create_image(mode.width - 50, (i + 0.4) * boxHeight, image = ImageTk.PhotoImage(pictures[i]))
            canvas.create_text(mode.width - 50, (i + 0.8) * boxHeight, text = f'{products[i]}', font = "Arial 15 bold")

        #instructions to open help and pause
        canvas.create_rectangle(10, mode.height - 70, 190, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Press H for Help \nPress P to Pause", font = "Arial 20 bold", fill = "black")

    def timeIsUp(mode, canvas):
        if mode.timeEnd:
            canvas.create_rectangle(mode.cx - 200, mode.cy - 100, mode.cx + 200, mode.cy + 100, fill = "light gray", outline = "")
            canvas.create_text(mode.cx, mode.cy, text="Time is Up!", font="Arial 50 bold")

    def drawColorOptions(mode, canvas):
        if mode.eyeshadowSelection == True:
            #eyeshadow color options
            for i in range(len(mode.eyeshadowColors)):
                canvas.create_rectangle(mode.width - 150, i * 50, mode.width - 100, (i+1) * 50, fill = mode.eyeshadowColorNames[i])
                canvas.create_text(mode.width - 125, (i + 0.5) * 50, text = f'{mode.eyeshadowColors[i]}', font = "Arial 15")
            
            #draw bounds to color between
            rightEyeBounds = [(711, 286),(713, 283),(715, 282),(718, 280),(721, 278),(725, 277),(731, 276),(735, 276),(738, 276),
                            (742, 275),(746, 275),(750, 275),(752, 275),(754, 275),(759, 276),(762, 272),(764, 270),(764, 268),
                            (763, 266),(760, 263),(755, 262),(750, 262),(744, 262),(736, 263),(728, 265),(721, 268),(716, 270),
                            (712, 273),(710, 276),(708, 279),(708, 284),(709, 287)]
            leftEyeBounds = []
            for (x,y) in rightEyeBounds:
                newX = (mode.width - 30 - x) + (mode.cx - 90)
                leftEyeBounds.append((newX,y))
            for (x,y) in rightEyeBounds:
                canvas.create_text(x, y, text = '·')
            for (x,y) in leftEyeBounds:
                canvas.create_text(x, y, text = '·')

        elif mode.blushSelection == True:
            #blush color options
            for i in range(len(mode.blushColors)):
                canvas.create_rectangle(mode.width - 150, 125 + i * 50, mode.width - 100, 125 + (i+1) * 50, fill = mode.blushColorNames[i])
                canvas.create_text(mode.width - 125, 125 + (i + 0.5) * 50, text = f'{mode.blushColors[i]}', font = "Arial 15")
            #draw bounds to color between
            r = 20
            for i in range(15):
                angle = math.pi/2 - (2*math.pi)*(i/15)
                dotX = 645 + r * math.cos(angle)
                dotY = 330 - r * math.sin(angle)
                canvas.create_text(dotX, dotY, text='·')
            for i in range(15):
                angle = math.pi/2 - (2*math.pi)*(i/15)
                dotX = 735 + r * math.cos(angle)
                dotY = 330 - r * math.sin(angle)
                canvas.create_text(dotX, dotY, text='·')

        elif mode.lipstickSelection == True:
            #lipstick color options
            for i in range(len(mode.lipstickColors)):
                canvas.create_rectangle(mode.width - 150, 250 + i * 50, mode.width - 100, 250 + (i+1) * 50, fill = mode.lipstickColorNames[i])
                canvas.create_text(mode.width - 125, 250 + (i + 0.5) * 50, text = f'{mode.lipstickColors[i]}', font = "Arial 15")
            #draw bounds to color between
            rightLipstickBounds = [(690, 355),(694, 354),(698, 353),(701, 354),(706, 355),(711, 358),
                                (690, 370),(694, 369),(698, 368),(703, 367),(707, 364), (710, 362)]
            leftLipstickBounds = []
            for (x,y) in rightLipstickBounds:
                newX = (mode.width - 30 - x) + (mode.cx - 90)
                leftLipstickBounds.append((newX,y))
            for (x,y) in rightLipstickBounds:
                canvas.create_text(x, y, text = '·')
            for (x,y) in leftLipstickBounds:
                canvas.create_text(x, y, text = '·')

    def drawing(mode, canvas):
        for (cx, cy, r, color) in mode.drawnTotalDots[:-1]:
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')
        if mode.colorShow == True:
            cx = mode.penX
            cy = mode.penY
            r = mode.penR
            color = mode.selectedColor
            #current dot that is being dragged has an outline
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color) 

    def drawScoringScreen(mode, canvas):
        #labels
        canvas.create_text(mode.cx // 2, 70, text=StartMode.name, font="Arial 30 bold")
        canvas.create_text(mode.cx // 2, 150, text=f'Score: {mode.opponentScore}%', font="Arial 30 ")
        canvas.create_text(mode.cx + mode.cx // 2, 70, text='You', font="Arial 30 bold")
        canvas.create_text(mode.cx + mode.cx // 2, 150, text=f'Score: {mode.yourScore}%', font="Arial 30 ")
        canvas.create_rectangle(0, mode.cy - 50, mode.width, mode.cy + 50, fill = 'white', outline = '')

        if mode.yourScore > mode.opponentScore:
            canvas.create_text(mode.cx, mode.cy, text='You Win! Congrats on getting hired!', font="Arial 40 bold")
        elif mode.yourScore < mode.opponentScore:
            canvas.create_text(mode.cx, mode.cy, text=f'Better luck next time, {StartMode.name} beat you.', font="Arial 40 bold")
        elif mode.yourScore == mode.opponentScore:
            canvas.create_text(mode.cx, mode.cy, text=f"It's a tie... try to beat {StartMode.name} next time.", font="Arial 40 bold")
        
        #restart button
        canvas.create_rectangle(mode.cx - 180, mode.height - 60, mode.cx + 180, mode.height - 20, fill = "pink", outline = "")
        canvas.create_text(mode.cx, mode.height - 40, text = "Try Again", font = "Arial 30 bold", fill = "black")

    def opponentDrawing(mode, canvas):
        canvas.create_oval(170 - 20, 330 - 20, 170 + 20, 330 + 20)

        canvas.create_oval(265 - 20, 330 - 20, 265 + 20, 330 + 20)
        for (cx, cy) in mode.drawnBlushL:
            mode.opponentR = 10
            canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                fill = mode.correctBlushColor, outline = '')   
        for (cx, cy) in mode.drawnBlushR:
            mode.opponentR = 10
            canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                fill = mode.correctBlushColor, outline = '')

        for (cx, cy) in mode.drawnEyeshadowL:
            mode.opponentR = 3
            canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                fill = mode.correctEyeshadowColor, outline = '')   
        
        for (cx, cy) in mode.drawnEyeshadowR:
            mode.opponentR = 4
            canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                fill = mode.correctEyeshadowColor, outline = '')   

        for (cx, cy) in mode.drawnLipstick:
            mode.opponentR = 3
            canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                fill = mode.correctLipstickColor, outline = '')   


    def redrawAll(mode, canvas):
        #background
        canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.background))

        if mode.customerScreen:
            GameMode.drawCustomerScreen(mode, canvas)

        elif mode.gameScreen:
            GameMode.drawGameScreen(mode,canvas)
            GameMode.drawColorOptions(mode, canvas)
            GameMode.drawing(mode, canvas)
            GameMode.timeIsUp(mode, canvas)
            GameMode.opponentDrawing(mode, canvas)

        elif mode.scoringScreen:
            GameMode.drawScoringScreen(mode, canvas)