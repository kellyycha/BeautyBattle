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

        #drawing
        mode.penX = mode.penY = mode.penR = 0
        mode.selectedColor = '' 
        mode.colorShow = False
        mode.drawnEyeshadowDots = []
        mode.drawnBlushLDots = []
        mode.drawnBlushRDots = []
        mode.drawnLipstickDots = []
        mode.drawnTotalDots = []

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

        mode.yourBlushLScore = 100
        mode.yourBlushRScore = 100
        mode.yourScore = 100

        mode.opponentScore = 100

        #AI
        mode.opponentPenX = 170
        mode.opponentPenY = 330
        mode.opponentR = 0
        mode.drawnBlushL = []
        mode.drawnBlushR = []
        mode.directions = [+1,2,-2,-1]
        mode.dx = random.choice(mode.directions)
        mode.dy = random.choice(mode.directions)
        mode.drawingBlushL = False
        mode.drawingBlushR = False
        mode.centerx = 170
        mode.centery = 330
        mode.filledBlushL = False
        mode.filledBlushR = False
        mode.opponentBlushLScore = 100
        mode.opponentBlushRScore = 100

        
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
                    GameMode.calculateOpponentScore(mode)
                    GameMode.calculateYourScore(mode)
                #eyeshadow selected
                elif (mode.width - 100 <= event.x <= mode.width) and (0 <= event.y < 125):
                    mode.eyeshadowSelection = True
                    mode.blushSelection = False
                    mode.lipstickSelection = False
                    mode.eraserSelection = False
                    mode.colorShow = False
                    mode.penR = 5
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
                    mode.penR = 5
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
                            mode.drawnEyeshadowDots.append((event.x, event.y, mode.penR, mode.selectedColor)) 
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
                if (cx, cy, r, color) in mode.drawnEyeshadowDots:
                    mode.drawnEyeshadowDots.remove((cx, cy, r, color))
                elif (cx, cy, r, color) in mode.drawnBlushDots:
                    mode.drawnBlushDots.remove((cx, cy, r, color))
                elif (cx, cy, r, color) in mode.drawnLipstickDots:
                    mode.drawnLipstickDots.remove((cx, cy, r, color))


    def keyPressed(mode, event):
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
                if mode.timerCount % 10 == 0:
                    if mode.timeLeft > 0:
                        mode.timeLeft -= 1
                    else:
                        mode.timeEnd = True
                        
                        
                if StartMode.easy:
                    mode.drawingBlushL = True
                    GameMode.easyAI(mode)
                
                mode.timerCount += 1

        #automatically shows the scoring screen 2 seconds after time ends
        if mode.scoringScreen == False and mode.timerCount > 63*10:
            GameMode.calculateOpponentScore(mode)
            GameMode.calculateYourScore(mode)
            mode.scoringScreen = True
            mode.gameScreen = False

    def easyAI(mode):
        #blush
        if mode.filledBlushL == False and mode.drawingBlushL == True:
            GameMode.moveEasyAI(mode)
        elif mode.filledBlushL == True and mode.filledBlushR == False:
            mode.drawingBlushL = False
            mode.drawingBlushR = True
            GameMode.moveEasyAI(mode)
        elif mode.filledBlushR == True:
            mode.drawingBlushR = False
    
    def distance(mode, x1, y1, x2, y2):
        return ((x1- x2)**2 + (y1-y2)**2)**0.5 + mode.opponentR

    def moveEasyAI(mode):
        #blush
        if mode.drawingBlushL:
            mode.centerx = 170
            mode.centery = 330
            mode.drawnBlushL.append((mode.opponentPenX,mode.opponentPenY))

            for (x1,y1) in mode.drawnBlushL:
                if GameMode.distance(mode, mode.centerx, mode.centery, x1, y1) == 20:
                    mode.filledBlushL = True
        
        elif mode.drawingBlushR:
            mode.centerx = 265
            if mode.drawnBlushR == []:
                mode.opponentPenX = 265
            mode.drawnBlushR.append((mode.opponentPenX,mode.opponentPenY))
            
            for (x1,y1) in mode.drawnBlushR:
                if GameMode.distance(mode, mode.centerx, mode.centery, x1, y1) == 20:
                    mode.filled2 = True

        if GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 20:
            mode.opponentPenX += mode.dx
            mode.opponentPenY += mode.dy
        elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 20:
            mode.opponentPenX -= mode.dx
            mode.opponentPenY -= mode.dy
            mode.dx = random.choice(mode.directions)
            mode.dy = random.choice(mode.directions)
    
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
        
            if blushLMaxXO-blushLMinXO >= 25 and blushLMaxYO-blushLMinYO >= 25: 
                mode.opponentBlushLScore = 100
            if blushLMaxYO-blushLMinYO < 25:
                mode.opponentBlushLScore -= (25 - (blushLMaxYO-blushLMinYO))
            elif blushLMaxXO-blushLMinXO < 25: 
                mode.opponentBlushLScore -= (25 - (blushLMaxXO-blushLMinXO))
            
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

            if blushRMaxXO-blushRMinXO >= 25 and blushRMaxYO-blushRMinYO >= 25: 
                mode.opponentBlushLScore = 100
            if blushRMaxYO-blushRMinYO < 25:
                mode.opponentBlushRScore -= (25 - (blushRMaxYO-blushRMinYO))
            if blushRMaxXO-blushRMinXO < 25: 
                mode.opponentBlushRScore -= (25 - (blushRMaxXO-blushRMinXO))
            
        elif blushRXValuesO == []:
            mode.opponentBlushRScore = 0
        
        mode.opponentScore = (mode.opponentBlushLScore+mode.opponentBlushRScore)//2

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
        
            if blushLMaxX-blushLMinX >= 25 and blushLMaxY-blushLMinY >= 25: 
                mode.yourBlushLScore = 100
            if blushLMaxY-blushLMinY < 25:
                mode.yourBlushLScore -= (25 - (blushLMaxY-blushLMinY))
            if blushLMaxX-blushLMinX < 25: 
                mode.yourBlushLScore -= (25 - (blushLMaxX-blushLMinX))
        
        elif blushLXValues == []:
            mode.yourBlushLScore = 0

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

            if blushRMaxX-blushRMinX >= 25 and blushRMaxY-blushRMinY >= 25: 
                mode.yourBlushLScore = 100
            if blushRMaxY-blushRMinY < 25:
                mode.yourBlushRScore -= (25 - (blushRMaxY-blushRMinY))
            if blushRMaxX-blushRMinX < 25: 
                mode.yourBlushRScore -= (25 - (blushRMaxX-blushRMinX))
           
        elif blushRXValues == []:
            mode.yourBlushRScore = 0

        for (cx, cy, r, color) in mode.drawnBlushLDots:
            if color != mode.correctBlushColor:
                mode.yourBlushLScore -= 10
        
        for (cx, cy, r, color) in mode.drawnBlushRDots:
            if color != mode.correctBlushColor:
                mode.yourBlushRScore -= 10
        
        mode.yourScore = (mode.yourBlushLScore+mode.yourBlushRScore)//2
        if mode.yourScore < 0:
            mode.yourScore = 0

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
        canvas.create_text(mode.cx - 30, 20, text=f'{mode.timeLeft}s remaining', font="Arial 20 bold")

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
        for (cx, cy) in mode.drawnBlushL:
            mode.opponentR = 10
            canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                fill = mode.correctBlushColor, outline = '')   
        for (cx, cy) in mode.drawnBlushR:
            mode.opponentR = 10
            canvas.create_oval(cx-mode.opponentR, cy-mode.opponentR, cx+mode.opponentR, cy+mode.opponentR, \
                                fill = mode.correctBlushColor, outline = '')

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