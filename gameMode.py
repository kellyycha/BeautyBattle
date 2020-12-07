from cmu_112_graphics import *
from tkinter import *
import random
import math
from startMode import *
from PIL import Image, ImageDraw, ImageFilter
from datetime import date

class GameMode(Mode):
    fromGame = False
    selection = None
    def appStarted(mode):
        mode.cx, mode.cy = mode.width // 2, mode.height // 2
        
        #three different modes in the game
        mode.customerScreen = True
        mode.gameScreen = False
        mode.scoringScreen = False

        #timer 
        mode.timeLeft = 61
        mode.timerCount = 0
        mode.timeEnd = False
        mode.pause = False

        GameMode.images(mode)
        GameMode.yourDrawingAndScore(mode)
        GameMode.AIDrawingAndScore(mode)
        GameMode.transparentScreens(mode)

    def images(mode):
        #background
        mode.background = mode.loadImage("images/background.jpg")

        # Customers generated with: https://www.cartoonify.de/#cartoonify
        customers = ["customer1.png", "customer2.png", "customer4.png"]
        customer = random.choice(customers)
        mode.customer = mode.scaleImage(mode.loadImage(f"images/customers/{customer}"), 2/3)
        mode.customerScoringScreen = mode.scaleImage(mode.loadImage(f"images/customers/{customer}"), 1/3)

        # Eyeshadow image: http://clipart-library.com/clipart/1401830.htm 
        mode.eyeshadow = mode.scaleImage(mode.loadImage("images/eyeshadow.png"), 1/6)
        # Blush image: https://webstockreview.net/pict/getfirst 
        mode.blush = mode.scaleImage(mode.loadImage("images/blush.png"), 1/5)
        # Lipstick image: https://pngriver.com/pink-lipstick-png-transparent-clipart-image-2-5461/women-lipstick-png-transparent-images-transparent-backgrounds-pink-lipstick-png-12/ 
        mode.lipstick = mode.scaleImage(mode.loadImage("images/lipstick.png"), 1/9)
        # Eraser image: http://clipart-library.com/clipart/15308.htm 
        mode.erase = mode.scaleImage(mode.loadImage("images/erase.png"), 1/5)

        #color picker
        mode.eyeshadowColors = ["pink", "orange", "yellow", "green", "blue", "purple"]
        mode.eyeshadowColorCodes = [(255,102,178), (255,128,0), (255,230,0), (127,235,173), (30,158,255), (178,102,255)]
        mode.eyeshadowColor = random.choice(mode.eyeshadowColors)

        eyeshadowIndex = mode.eyeshadowColors.index(mode.eyeshadowColor)
        mode.correctEyeshadowColor = mode.eyeshadowColorCodes[eyeshadowIndex]

        mode.blushColors = ["pink", "peach", "orange"]
        mode.blushColorCodes = [(255,153,153), (255,181,169), (255,178,102)]
        mode.blushColor = random.choice(mode.blushColors)

        blushIndex = mode.blushColors.index(mode.blushColor)
        mode.correctBlushColor = mode.blushColorCodes[blushIndex]

        mode.lipstickColors = ["pink", "red", "nude", "purple"]
        mode.lipstickColorCodes = [(255,102,178), (240,0,0), (235,164,94), (178,102,255)]
        mode.lipstickColor = random.choice(mode.lipstickColors)   

        lipstickIndex = mode.lipstickColors.index(mode.lipstickColor)
        mode.correctLipstickColor = mode.lipstickColorCodes[lipstickIndex]

    def yourDrawingAndScore(mode):
        #selected product
        mode.eyeshadowSelection = False
        mode.blushSelection = False
        mode.lipstickSelection = False
        mode.eraserSelection = False

        mode.penX = mode.penY = mode.penR = 0
        mode.released = True
        mode.selectedColor = (255,255,255) 
        mode.colorShow = False
        mode.yourScore = 0
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
        mode.left = False

    def AIDrawingAndScore(mode):
        #AI
        mode.opponentPenX = 170
        mode.opponentPenY = 330
        mode.opponentR = 0
        mode.directions = [+1,2,-2,-1]
        mode.dx = random.choice(mode.directions)
        mode.dy = random.choice(mode.directions)
        mode.opponentScore = 0
        mode.step = 1

        mode.centerx = 170
        mode.centery = 330
        mode.centerx2 = 160
        mode.centery2 = 375
        mode.centerx3 = 230
        mode.centery3 = 365 

        mode.drawnEyeshadowL = []
        mode.drawnEyeshadowR = []
        mode.drawnEyeshadow = []
        mode.drawingEyeshadowL = False
        mode.drawingEyeshadowR = False
        mode.filledEyeshadowL = False
        mode.filledEyeshadowR = False
        mode.opponentEyeshadowLScore = 100
        mode.opponentEyeshadowRScore = 100
        mode.eyeshadowLen = 50
        mode.eyeshadowMaxLen = 70

        mode.drawnBlushL = []
        mode.drawnBlushR = []
        mode.drawnBlush = []
        mode.drawingBlushL = False
        mode.drawingBlushR = False
        mode.filledBlushL = False
        mode.filledBlushR = False
        mode.opponentBlushLScore = 100
        mode.opponentBlushRScore = 100
        mode.blushMaxLen = 77

        mode.drawnLipstick = []
        mode.drawingLipstick = False
        mode.filledLipstick = False
        mode.opponentLipstickScore = 100

    def transparentScreens(mode): 
        #empty drawing screens
        img1 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw1 = ImageDraw.Draw(img1) 
        img1.save('images/draw/drawEyeshadowL.png')
        mode.drawEyeshadowL = mode.loadImage('images/draw/drawEyeshadowL.png')
        img12 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw12 = ImageDraw.Draw(img12) 
        img12.save('images/draw/drawEyeshadowR.png')
        mode.drawEyeshadowR = mode.loadImage('images/draw/drawEyeshadowR.png')

        img2 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw2 = ImageDraw.Draw(img2) 
        img2.save('images/draw/drawBlushL.png')
        mode.drawBlushL = mode.loadImage('images/draw/drawBlushL.png')
        mode.drawBlushLScoringScreen = mode.scaleImage(mode.loadImage('images/draw/drawBlushL.png'), 1/3)
        img22 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw22 = ImageDraw.Draw(img22) 
        img22.save('images/draw/drawBlushR.png')
        mode.drawBlushR = mode.loadImage('images/draw/drawBlushR.png')

        img3 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw3 = ImageDraw.Draw(img3) 
        img3.save('images/draw/drawLipstick.png')
        mode.drawLipstick = mode.loadImage('images/draw/drawLipstick.png')

        img4 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw4 = ImageDraw.Draw(img4) 
        img4.save('images/draw/drawOpponentEyeshadowL.png')
        mode.drawOpponentEyeshadowL = mode.loadImage('images/draw/drawOpponentEyeshadowL.png')

        img42 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw42 = ImageDraw.Draw(img42) 
        img42.save('images/draw/drawOpponentEyeshadowR.png')
        mode.drawOpponentEyeshadowR = mode.loadImage('images/draw/drawOpponentEyeshadowR.png')

        img5 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw5 = ImageDraw.Draw(img5) 
        img5.save('images/draw/drawOpponentBlushL.png')
        mode.drawOpponentBlushL = mode.loadImage('images/draw/drawOpponentBlushL.png')

        img52 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw52 = ImageDraw.Draw(img52) 
        img52.save('images/draw/drawOpponentBlushR.png')
        mode.drawOpponentBlushR = mode.loadImage('images/draw/drawOpponentBlushR.png')

        img6 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw6 = ImageDraw.Draw(img6) 
        img6.save('images/draw/drawOpponentLipstick.png')
        mode.drawOpponentLipstick = mode.loadImage('images/draw/drawOpponentLipstick.png')
    
    def collectData(mode):
        GameMode.selection = StartMode.name
        with open(f"data/{''.join(LoginScreen.username)}.txt", 'a+') as fp:
            fp.write(f"Level: {StartMode.name}, Date: {date.today()}, Score: {mode.yourScore}\n")
        if StartMode.name == 'Amateur':
            with open('data/easyLeaderboard.txt', 'a+') as fp:
                fp.write(f"Name: {''.join(LoginScreen.username)}, Score: {mode.yourScore}\n")
        elif StartMode.name == 'Professional':
            with open('data/mediumLeaderboard.txt', 'a+') as fp:
                fp.write(f"Name: {''.join(LoginScreen.username)}, Score: {mode.yourScore}\n")
        elif StartMode.name == 'Expert':
            with open('data/hardLeaderboard.txt', 'a+') as fp:
                fp.write(f"Name: {''.join(LoginScreen.username)}, Score: {mode.yourScore}\n")

    #from 15112 PIL Notes
    def getCachedPhotoImage(mode, image):
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

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
                if (mode.cx - 30 - 60 <= event.x <= mode.cx - 30 + 60) and (mode.cy + mode.cy//3 - 30 <= event.y < mode.cy + mode.cy//3 + 30) and mode.timeEnd == False:
                    mode.scoringScreen = True
                    mode.gameScreen = False
                    mode.customerScreen = False
                    GameMode.calculateYourScore(mode)
                    GameMode.calculateOpponentScore(mode)
                    GameMode.collectData(mode)
                    
                #eyeshadow selected
                elif (mode.width - 100 <= event.x <= mode.width) and (0 <= event.y < 125):
                    mode.eyeshadowSelection = not mode.eyeshadowSelection
                    mode.blushSelection = False
                    mode.lipstickSelection = False
                    mode.eraserSelection = False
                    mode.colorShow = False
                    mode.penR = 3
                #blush selected
                elif (mode.width - 100 <= event.x <= mode.width) and (125 <= event.y < 250):
                    mode.eyeshadowSelection = False
                    mode.blushSelection = not mode.blushSelection
                    mode.lipstickSelection = False
                    mode.eraserSelection = False
                    mode.colorShow = False
                    mode.penR = 10
                #lipstick selected
                elif (mode.width - 100 <= event.x <= mode.width) and (250 <= event.y < 375):
                    mode.eyeshadowSelection = False
                    mode.blushSelection = False
                    mode.lipstickSelection = not mode.lipstickSelection 
                    mode.eraserSelection = False
                    mode.colorShow = False
                    mode.penR = 3
                #eraser selected
                elif (mode.width - 100 <= event.x <= mode.width) and (375 <= event.y < 500):
                    mode.eyeshadowSelection = False
                    mode.blushSelection = False
                    mode.lipstickSelection = False
                    mode.eraserSelection = not mode.eraserSelection
                    mode.colorShow = False
                    mode.penR = 5
                    mode.selectedColor = (255,255,255)
                #pick eyeshadow color
                if mode.eyeshadowSelection:
                    for i in range(len(mode.eyeshadowColorCodes)):
                        if (850 <= event.x <= 900) and (i*50 <= event.y < (i+1)*50):
                            mode.colorShow = False
                            mode.selectedColor = mode.eyeshadowColorCodes[i]
                #pick blush color
                if mode.blushSelection:
                    for i in range(len(mode.blushColorCodes)):
                        if (850 <= event.x <= 900) and (125 + i*50 <= event.y < 125 + (i+1)*50):
                            mode.colorShow = False
                            mode.selectedColor = mode.blushColorCodes[i]
                #pick lipstick color
                if mode.lipstickSelection:
                    for i in range(len(mode.lipstickColorCodes)):
                        if (850 <= event.x <= 900) and (250 + i*50 <= event.y < 250 + (i+1)*50):
                            mode.colorShow = False
                            mode.selectedColor = mode.lipstickColorCodes[i]
        
        if mode.scoringScreen:
            #restart button
            if (mode.cx - 100 <= event.x <= mode.cx + 100) and (mode.height - 80 - 40 <= event.y < mode.height - 80 + 40):
                StartMode.login = True
                GameMode.fromGame = False
                mode.app.startMode.appStarted()
                mode.app.gameMode.appStarted()
                mode.app.setActiveMode(mode.app.startMode)
            #clicks leaderboard
            if (10 <= event.x <= 210) and (mode.height - 45 <= event.y <= mode.height - 10):
                GameMode.fromGame = True
                mode.app.leaderboard.appStarted()
                mode.app.setActiveMode(mode.app.leaderboard)
            #logs out
            if (mode.width - 110 <= event.x <= mode.width - 10) and (mode.height - 45 <= event.y <= mode.height - 10):
                StartMode.login = False
                mode.app.startMode.appStarted()
                mode.app.loginScreen.appStarted()
                mode.app.gameMode.appStarted()
                mode.app.setActiveMode(mode.app.startMode)

    def mouseDragged(mode, event):
        mode.released = False
        if mode.pause == False and mode.timeEnd == False:
            if mode.gameScreen:
                if (600 <= event.x <= 780) and (190 <= event.y < 390):
                    mode.colorShow = True
                    mode.penX = event.x
                    mode.penY = event.y
                    if mode.selectedColor != (255,255,255):
                        mode.drawnTotalDots.append((event.x, event.y, mode.penR, mode.selectedColor))
                        if mode.eyeshadowSelection:
                            if event.x < 690:
                                mode.left = True
                                mode.drawnEyeshadowLDots.append((event.x, event.y, mode.penR, mode.selectedColor)) 
                            else:
                                mode.left = False
                                mode.drawnEyeshadowRDots.append((event.x, event.y, mode.penR, mode.selectedColor))
                        if mode.blushSelection:
                            if event.x < 690:
                                mode.left = True
                                mode.drawnBlushLDots.append((event.x, event.y, mode.penR, mode.selectedColor))
                            else:
                                mode.left = False
                                mode.drawnBlushRDots.append((event.x, event.y, mode.penR, mode.selectedColor))
                        if mode.lipstickSelection:
                            mode.drawnLipstickDots.append((event.x, event.y, mode.penR, mode.selectedColor))
                if mode.eraserSelection:
                    GameMode.eraserIntersect(mode) #erasing

    def mouseReleased(mode, event):
        mode.released = True
        mode.colorShow = False
        
        GameMode.drawOpacity(mode)

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

        GameMode.drawOpacity(mode)

    def drawOpacity(mode):
        img1 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw1 = ImageDraw.Draw(img1) 
        for (cx, cy, r, color) in mode.drawnEyeshadowLDots:
            colorR = color[0]
            colorG = color[1]
            colorB = color[2]
            draw1.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(colorR,colorG,colorB,210))
        img1 = img1.filter(ImageFilter.GaussianBlur(3))
        img1.save('images/draw/drawEyeshadowL.png')
        mode.drawEyeshadowL = mode.loadImage('images/draw/drawEyeshadowL.png')

        img12 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw12 = ImageDraw.Draw(img12) 
        for (cx, cy, r, color) in mode.drawnEyeshadowRDots:
            colorR = color[0]
            colorG = color[1]
            colorB = color[2]
            draw12.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(colorR,colorG,colorB,210))
        img12 = img12.filter(ImageFilter.GaussianBlur(3))
        img12.save('images/draw/drawEyeshadowR.png')
        mode.drawEyeshadowR = mode.loadImage('images/draw/drawEyeshadowR.png')

        img2 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw2 = ImageDraw.Draw(img2) 
        for (cx, cy, r, color) in mode.drawnBlushLDots:
            colorR = color[0]
            colorG = color[1]
            colorB = color[2]
            draw2.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(colorR,colorG,colorB,100))
        img2 = img2.filter(ImageFilter.GaussianBlur(5))
        img2.save('images/draw/drawBlushL.png')
        mode.drawBlushL = mode.loadImage('images/draw/drawBlushL.png')

        img22 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw22 = ImageDraw.Draw(img22) 
        for (cx, cy, r, color) in mode.drawnBlushRDots:
            colorR = color[0]
            colorG = color[1]
            colorB = color[2]
            draw22.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(colorR,colorG,colorB,100))
        img22 = img22.filter(ImageFilter.GaussianBlur(5))
        img22.save('images/draw/drawBlushR.png')
        mode.drawBlushR = mode.loadImage('images/draw/drawBlushR.png')

        img3 = Image.new('RGBA', (1000,500), (255, 102, 178, 0))
        draw3 = ImageDraw.Draw(img3) 
        for (cx, cy, r, color) in mode.drawnLipstickDots:
            colorR = color[0]
            colorG = color[1]
            colorB = color[2]
            draw3.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(colorR,colorG,colorB,210))
        img3 = img3.filter(ImageFilter.GaussianBlur(1))
        img3.save('images/draw/drawLipstick.png')
        mode.drawLipstick = mode.loadImage('images/draw/drawLipstick.png')

        GameMode.resizeDrawings(mode)

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

    def timerFired(mode):
        if mode.pause == False:
            if mode.gameScreen:
                #countdown every second
                if mode.timeLeft > 0.092:
                    mode.timeLeft -= 0.092
                else:
                    mode.timeLeft = 0
                    mode.timeEnd = True
                        
                if StartMode.easy:
                    GameMode.easyAI(mode)
                
                elif StartMode.medium:
                    mode.step = 0.75
                    mode.eyeshadowLen = 75
                    mode.eyeshadowMaxLen = 100
                    mode.blushMaxLen = 100
                    GameMode.hardAI(mode)
                
                elif StartMode.hard:
                    mode.step = 1
                    mode.eyeshadowLen = 50
                    mode.eyeshadowMaxLen = 70
                    mode.blushMaxLen = 77
                    GameMode.hardAI(mode)
                
                mode.timerCount += 1

        #automatically shows the scoring screen after time ends
        if mode.scoringScreen == False and mode.timerCount > 68*10: 
            GameMode.calculateYourScore(mode)
            GameMode.calculateOpponentScore(mode)
            mode.scoringScreen = True
            mode.gameScreen = False
            GameMode.collectData(mode)
        
    def distance(mode, x1, y1, x2, y2):
        return ((x1- x2)**2 + (y1-y2)**2)**0.5 + mode.opponentR

    def easyAI(mode):
        #time is up
        if mode.timeLeft <= 2 and mode.drawingLipstick == True and mode.filledLipstick == False:
            mode.filledLipstick = True
            mode.drawingLipstick = False
        #start lips if 15 seconds left
        if mode.timeLeft <= 15 and mode.filledLipstick == False and \
            (mode.drawingEyeshadowL or mode.drawingEyeshadowR or mode.drawingBlushL or mode.drawingBlushR):            
            mode.filledEyeshadowL = True
            mode.filledEyeshadowR = True
            mode.filledBlushL = True
            mode.filledBlushR = True
            mode.drawingEyeshadowL = False
            mode.drawingEyeshadowR = False
            mode.drawingBlushL = False
            mode.drawingBlushR = False
        
        #eyeshadow
        if mode.filledEyeshadowL == False:
            mode.drawingEyeshadowL = True
            GameMode.moveEasyAI(mode)
        elif mode.filledEyeshadowL == True and mode.filledEyeshadowR == False: 
            mode.drawingEyeshadowL = False
            mode.drawingEyeshadowR = True
            GameMode.moveEasyAI(mode)
        #blush
        elif mode.filledEyeshadowR == True and mode.filledBlushL == False:
            mode.drawingEyeshadowR = False
            mode.drawingBlushL = True
            GameMode.moveEasyAI(mode)
        elif mode.filledBlushL == True and mode.filledBlushR == False:
            mode.drawingBlushL = False
            mode.drawingBlushR = True
            GameMode.moveEasyAI(mode)
        #lipstick
        elif mode.filledBlushR == True and mode.filledLipstick == False:
            mode.drawingBlushR = False
            mode.drawingLipstick = True
            GameMode.moveEasyAI(mode)

    def moveEasyAI(mode):
        #eyeshadow
        if mode.drawingEyeshadowL:
            mode.centerx = 160
            mode.centery = 313
            if mode.drawnEyeshadowL == []:
                mode.opponentPenX = 165
                mode.opponentPenY = 270
            mode.drawnEyeshadowL.append((mode.opponentPenX,mode.opponentPenY,3))
            
            xValues = []
            for (x,y,r) in mode.drawnEyeshadowL:
                xValues.append(x)
            minX = min(xValues)
            maxX = max(xValues)
            if maxX-minX >= 45 or len(mode.drawnEyeshadowL) > 200:
                mode.filledEyeshadowL = True

        elif mode.drawingEyeshadowR:
            mode.centerx = 160 + 120
            mode.centerx2 = 160 + 120
            if mode.drawnEyeshadowR == []:
                mode.opponentPenX = 265
                mode.opponentPenY = 270
            mode.drawnEyeshadowR.append((mode.opponentPenX,mode.opponentPenY,3))
            
            xValues = []
            for (x,y,r) in mode.drawnEyeshadowR:
                xValues.append(x)
            minX = min(xValues)
            maxX = max(xValues)
            if maxX-minX >= 45 or len(mode.drawnEyeshadowR) > 200:
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
                if mode.drawingEyeshadowL:
                    mode.drawnEyeshadowL.pop()
                if mode.drawingEyeshadowR:
                    mode.drawnEyeshadowR.pop()
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

        #blush
        if mode.drawingBlushL:
            mode.centerx = 170
            mode.centery = 330
            if mode.drawnBlushL == []:
                mode.opponentPenX = 170
                mode.opponentPenY = 330
            mode.drawnBlushL.append((mode.opponentPenX,mode.opponentPenY,10))

            blushLXValuesO = []
            blushLYValuesO = []
            for (x,y,r) in mode.drawnBlushL:
                blushLXValuesO.append(x)
                blushLYValuesO.append(y)
            if len(blushLXValuesO) > 0:
                blushLMinXO = min(blushLXValuesO)
                blushLMaxXO = max(blushLXValuesO)
                blushLMinYO = min(blushLYValuesO)
                blushLMaxYO = max(blushLYValuesO)

            if (blushLMaxXO-blushLMinXO > 22 and blushLMaxYO-blushLMinYO > 22) or len(mode.drawnBlushL) > 60: 
                mode.filledBlushL = True
        
        elif mode.drawingBlushR:
            mode.centerx = 265
            if mode.drawnBlushR == []:
                mode.opponentPenX = 265
                mode.opponentPenY = 330
            mode.drawnBlushR.append((mode.opponentPenX,mode.opponentPenY,10))
            
            blushRXValuesO = []
            blushRYValuesO = []
            for (x,y,r) in mode.drawnBlushR:
                blushRXValuesO.append(x)
                blushRYValuesO.append(y)
            if len(blushRXValuesO) > 0:
                blushRMinXO = min(blushRXValuesO)
                blushRMaxXO = max(blushRXValuesO)
                blushRMinYO = min(blushRYValuesO)
                blushRMaxYO = max(blushRYValuesO)

            if (blushRMaxXO-blushRMinXO > 22 and blushRMaxYO-blushRMinYO > 22) or len(mode.drawnBlushR) > 60: 
                mode.filledBlushR = True
        
        if mode.drawingBlushL or mode.drawingBlushR:
            if GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 20:
                mode.opponentPenX += mode.dx
                mode.opponentPenY += mode.dy
            elif 20 < GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) < 23:
                mode.opponentPenX -= mode.dx
                mode.opponentPenY -= mode.dy
                mode.dx = random.choice(mode.directions)
                mode.dy = random.choice(mode.directions)
            else:
                if mode.drawingBlushL:
                    mode.drawnBlushL.pop()
                if mode.drawingBlushR:
                    mode.drawnBlushR.pop()
                mode.dx = random.choice(mode.directions)
                mode.dy = random.choice(mode.directions)
                mode.opponentPenX += mode.dx
                mode.opponentPenY += mode.dy
        
        #lipstick
        if mode.drawingLipstick:
            mode.centerx = 220
            mode.centery = 340
            mode.centerx2 = 210
            mode.centery2 = 365
            if mode.drawnLipstick == []:
                mode.opponentPenX = 220
                mode.opponentPenY = 365
            mode.drawnLipstick.append((mode.opponentPenX,mode.opponentPenY,3))
            
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
        
        GameMode.drawOpponentOpacity(mode)

    def hardAI(mode):
        #eyeshadow
        if mode.filledEyeshadowL == False:
            mode.drawingEyeshadowL = True
            GameMode.moveHardAI(mode)
        elif mode.filledEyeshadowL == True and mode.filledEyeshadowR == False: 
            mode.drawingEyeshadowL = False
            mode.drawingEyeshadowR = True
            GameMode.moveHardAI(mode)
        #blush
        elif mode.filledEyeshadowR == True and mode.filledBlushL == False:
            mode.drawingEyeshadowR = False
            mode.drawingBlushL = True
            GameMode.moveHardAI(mode)
        elif mode.filledBlushL == True and mode.filledBlushR == False:
            mode.drawingBlushL = False
            mode.drawingBlushR = True
            GameMode.moveHardAI(mode)
        #lipstick
        elif mode.filledBlushR == True and mode.filledLipstick == False:
            mode.drawingBlushR = False
            mode.drawingLipstick = True
            GameMode.moveHardAI(mode)
        
        #time is up
        if mode.timeLeft == 0:
            mode.drawingLipstick = False
    
    def moveHardAI(mode):
        #eyeshadow
        if mode.drawingEyeshadowL:
            mode.centerx = 160
            mode.centery = 313
            direction = 1
            eyeshadowList = mode.drawnEyeshadowL
            if mode.drawnEyeshadowL == []:
                mode.opponentPenX = 192
                mode.opponentPenY = 279
            mode.drawnEyeshadowL.append((mode.opponentPenX,mode.opponentPenY,3))
            if len(mode.drawnEyeshadowL) >= mode.eyeshadowMaxLen:
                mode.filledEyeshadowL = True
                
        elif mode.drawingEyeshadowR:
            mode.centerx = 160 + 120
            mode.centerx2 = 160 + 120
            direction = -1
            eyeshadowList = mode.drawnEyeshadowR
            if mode.drawnEyeshadowR == []:
                mode.opponentPenX = 248
                mode.opponentPenY = 279
            mode.drawnEyeshadowR.append((mode.opponentPenX,mode.opponentPenY,3))
            if len(mode.drawnEyeshadowR) >= mode.eyeshadowMaxLen:
                mode.filledEyeshadowR = True

        if mode.drawingEyeshadowL or mode.drawingEyeshadowR:

            if len(eyeshadowList) < mode.eyeshadowLen and GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 50:
                mode.opponentPenX -= mode.step * direction
                mode.opponentPenY -= mode.step
                
            elif len(eyeshadowList) < mode.eyeshadowLen and GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 50:
                mode.opponentPenY += mode.step
                mode.opponentPenX -= mode.step * direction
            
            if (mode.opponentPenX <= 150 or mode.opponentPenX >=290) and GameMode.distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) > 105:
                mode.opponentPenX += mode.step * direction
                mode.opponentPenY += 1.5 * mode.step
            
            if len(eyeshadowList) > mode.eyeshadowLen and GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 50: 
                mode.opponentPenX += mode.step * direction
                mode.opponentPenY += mode.step

            if len(eyeshadowList) > mode.eyeshadowLen and GameMode.distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) <= 105:
                mode.opponentPenX += mode.step * direction
                mode.opponentPenY -= mode.step
        #blush
        if mode.drawingBlushL:
            mode.centerx = 170
            mode.centery = 330
            if mode.drawnBlushL == []:
                mode.opponentPenX = 160
                mode.opponentPenY = 330
            mode.drawnBlushL.append((mode.opponentPenX,mode.opponentPenY,10))

            if len(mode.drawnBlushL) >= mode.blushMaxLen:
                mode.filledBlushL = True

            if GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 23:
                mode.drawnBlushL.pop()
                
        elif mode.drawingBlushR:
            mode.centerx = 265
            if mode.drawnBlushR == []:
                mode.opponentPenX = 255
                mode.opponentPenY = 330
            mode.drawnBlushR.append((mode.opponentPenX,mode.opponentPenY,10))
     
            if len(mode.drawnBlushR) >= mode.blushMaxLen:
                mode.filledBlushR = True

            if GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 23:
                mode.drawnBlushR.pop()

        if mode.drawingBlushL or mode.drawingBlushR:
            if GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 20 and mode.opponentPenY >= 330:
                mode.opponentPenY += mode.step
            elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 20 and mode.opponentPenY < 330:
                mode.opponentPenY -= mode.step
            elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) >= 20 and mode.opponentPenY >= 330:
                mode.opponentPenX += mode.step
                mode.opponentPenY -= mode.step
            elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) >= 20 and mode.opponentPenY < 330:
                mode.opponentPenX -= mode.step
        #lipstick
        if mode.drawingLipstick:
            mode.centerx = 220
            mode.centery = 340
            mode.centerx2 = 210
            mode.centery2 = 365
            mode.centerx3 = 230
            mode.centery3 = 365
            if mode.drawnLipstick == []:
                mode.opponentPenX = 202
                mode.opponentPenY = 360

            mode.drawnLipstick.append((mode.opponentPenX,mode.opponentPenY,3))

            if len(mode.drawnLipstick) >= 180:
                mode.filledLipstick = True

            if len(mode.drawnLipstick) >= 159 and GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 30:
                mode.opponentPenY = 360.25
                mode.opponentPenX += 2

            elif len(mode.drawnLipstick) >= 46 and GameMode.distance(mode, mode.centerx3, mode.centery3, mode.opponentPenX, mode.opponentPenY) < 15:
                mode.opponentPenX -= 1
                mode.opponentPenY -= 2
            
            elif len(mode.drawnLipstick) >= 60 and GameMode.distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) < 15:
                mode.opponentPenX -= 1
                mode.opponentPenY -= 2
 
            elif GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) <= 30:
                mode.opponentPenY += 1

            if len(mode.drawnLipstick) < 100 and GameMode.distance(mode, mode.centerx, mode.centery, mode.opponentPenX, mode.opponentPenY) > 30 and\
                (GameMode.distance(mode, mode.centerx2, mode.centery2, mode.opponentPenX, mode.opponentPenY) < 15 or \
                GameMode.distance(mode, mode.centerx3, mode.centery3, mode.opponentPenX, mode.opponentPenY) < 15):
                mode.opponentPenX += 1
                mode.opponentPenY -= 1

        GameMode.drawOpponentOpacity(mode)

    def drawOpponentOpacity(mode):
        img4 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw4 = ImageDraw.Draw(img4) 
        for (cx, cy, r) in mode.drawnEyeshadowL:
            colorR = mode.correctEyeshadowColor[0]
            colorG = mode.correctEyeshadowColor[1]
            colorB = mode.correctEyeshadowColor[2]
            draw4.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(colorR,colorG,colorB,210))
        img4 = img4.filter(ImageFilter.GaussianBlur(3))
        img4.save('images/draw/drawOpponentEyeshadowL.png')
        mode.drawOpponentEyeshadowL = mode.loadImage('images/draw/drawOpponentEyeshadowL.png')

        img42 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw42 = ImageDraw.Draw(img42) 
        for (cx, cy, r) in mode.drawnEyeshadowR:
            colorR = mode.correctEyeshadowColor[0]
            colorG = mode.correctEyeshadowColor[1]
            colorB = mode.correctEyeshadowColor[2]
            draw42.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(colorR,colorG,colorB,210))
        img42 = img42.filter(ImageFilter.GaussianBlur(3))
        img42.save('images/draw/drawOpponentEyeshadowR.png')
        mode.drawOpponentEyeshadowR = mode.loadImage('images/draw/drawOpponentEyeshadowR.png')

        img5 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw5 = ImageDraw.Draw(img5) 
        for (cx, cy, r) in mode.drawnBlushL:
            colorR = mode.correctBlushColor[0]
            colorG = mode.correctBlushColor[1]
            colorB = mode.correctBlushColor[2]
            draw5.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(colorR,colorG,colorB,100))
        img5 = img5.filter(ImageFilter.GaussianBlur(5))
        img5.save('images/draw/drawOpponentBlushL.png')
        mode.drawOpponentBlushL = mode.loadImage('images/draw/drawOpponentBlushL.png')

        img52 = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
        draw52 = ImageDraw.Draw(img52) 
        for (cx, cy, r) in mode.drawnBlushR:
            colorR = mode.correctBlushColor[0]
            colorG = mode.correctBlushColor[1]
            colorB = mode.correctBlushColor[2]
            draw52.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(colorR,colorG,colorB,100))
        img52 = img52.filter(ImageFilter.GaussianBlur(5))
        img52.save('images/draw/drawOpponentBlushR.png')
        mode.drawOpponentBlushR = mode.loadImage('images/draw/drawOpponentBlushR.png')

        img6 = Image.new('RGBA', (1000,500), (255, 102, 178, 0))
        draw6 = ImageDraw.Draw(img6) 
        for (cx, cy, r) in mode.drawnLipstick:
            colorR = mode.correctLipstickColor[0]
            colorG = mode.correctLipstickColor[1]
            colorB = mode.correctLipstickColor[2]
            draw6.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(colorR,colorG,colorB,210))
        img6 = img6.filter(ImageFilter.GaussianBlur(1))
        img6.save('images/draw/drawOpponentLipstick.png')
        mode.drawOpponentLipstick = mode.loadImage('images/draw/drawOpponentLipstick.png')
    
        GameMode.resizeDrawings(mode)

    def calculateOpponentScore(mode):
        eyeshadowLXValuesO = []
        eyeshadowLYValuesO = []
        for (x,y,r) in mode.drawnEyeshadowL:
            eyeshadowLXValuesO.append(x)
            eyeshadowLYValuesO.append(y)
        if len(eyeshadowLXValuesO) > 0:
            eyeshadowLMinXO = min(eyeshadowLXValuesO)
            eyeshadowLMaxXO = max(eyeshadowLXValuesO)
            eyeshadowLMinYO = min(eyeshadowLYValuesO)
            eyeshadowLMaxYO = max(eyeshadowLYValuesO)
            print(eyeshadowLMinYO, eyeshadowLMaxYO)
            print(f'len L eye {len(eyeshadowLXValuesO)}')

            if StartMode.easy:
                if (eyeshadowLMaxXO-eyeshadowLMinXO >= 45 and eyeshadowLMaxYO-eyeshadowLMinYO >= 15 and
                eyeshadowLMaxXO-eyeshadowLMinXO < 48 and eyeshadowLMaxYO-eyeshadowLMinYO < 17 and
                len(eyeshadowLXValuesO) > 200): 
                    mode.opponentEyeshadowLScore = 100
                if len(eyeshadowLXValuesO) <= 200:
                    mode.opponentEyeshadowLScore -= 10
                if len(eyeshadowLXValuesO) <= 100:
                    mode.opponentEyeshadowLScore -= 10
                if eyeshadowLMaxXO-eyeshadowLMinXO >= 48: 
                    mode.opponentEyeshadowLScore -= ((eyeshadowLMaxXO-eyeshadowLMinXO) - 48)
                if eyeshadowLMaxYO-eyeshadowLMinYO >= 17:
                    mode.opponentEyeshadowLScore -= ((eyeshadowLMaxYO-eyeshadowLMinYO) - 17)
                if eyeshadowLMaxYO-eyeshadowLMinYO < 15:
                    mode.opponentEyeshadowLScore -= (15 - (eyeshadowLMaxYO-eyeshadowLMinYO))
                if eyeshadowLMaxXO-eyeshadowLMinXO < 45: 
                    mode.opponentEyeshadowLScore -= (45 - (eyeshadowLMaxXO-eyeshadowLMinXO))
            
            elif StartMode.hard:
                if len(eyeshadowLXValuesO) == 70:
                    mode.opponentEyeshadowLScore = 100
                else:
                    mode.opponentEyeshadowLScore -= (70 - len(eyeshadowLXValuesO))
            
        elif eyeshadowLXValuesO == []:
            mode.opponentEyeshadowLScore = 0
        
        eyeshadowRXValuesO = []
        eyeshadowRYValuesO = []
        for (x,y,r) in mode.drawnEyeshadowR:
            eyeshadowRXValuesO.append(x)
            eyeshadowRYValuesO.append(y)
        if len(eyeshadowRXValuesO) > 0:
            eyeshadowRMinXO = min(eyeshadowRXValuesO)
            eyeshadowRMaxXO = max(eyeshadowRXValuesO)
            eyeshadowRMinYO = min(eyeshadowRYValuesO)
            eyeshadowRMaxYO = max(eyeshadowRYValuesO)
            print(eyeshadowRMinYO, eyeshadowRMaxYO)
            print(f'len R eye {len(eyeshadowRXValuesO)}')

            if StartMode.easy:
                if (eyeshadowRMaxXO-eyeshadowRMinXO >= 45 and eyeshadowRMaxYO-eyeshadowRMinYO >= 15 and
                    eyeshadowRMaxXO-eyeshadowRMinXO < 48 and eyeshadowRMaxYO-eyeshadowRMinYO < 17 and
                    len(eyeshadowLXValuesO) > 200): 
                    mode.opponentEyeshadowRScore = 100
                if len(eyeshadowRXValuesO) <= 200:
                    mode.opponentEyeshadowRScore -= 10
                if len(eyeshadowRXValuesO) <= 100:
                    mode.opponentEyeshadowRScore -= 10
                if eyeshadowRMaxXO-eyeshadowRMinXO >= 48: 
                    mode.opponentEyeshadowRScore -= ((eyeshadowRMaxXO-eyeshadowRMinXO) - 48)
                if eyeshadowRMaxYO-eyeshadowRMinYO >= 17:
                    mode.opponentEyeshadowRScore -= ((eyeshadowRMaxYO-eyeshadowRMinYO) - 17)
                if eyeshadowRMaxYO-eyeshadowRMinYO < 15:
                    mode.opponentEyeshadowRScore -= (15 - (eyeshadowRMaxYO-eyeshadowRMinYO))
                if eyeshadowRMaxXO-eyeshadowRMinXO < 45: 
                    mode.opponentEyeshadowRScore -= (45 - (eyeshadowRMaxXO-eyeshadowRMinXO))

            elif StartMode.hard:
                if len(eyeshadowRXValuesO) == 70:
                    mode.opponentEyeshadowRScore = 100
                else:
                    mode.opponentEyeshadowRScore -= (70 - len(eyeshadowRXValuesO))

        elif eyeshadowRXValuesO == []:
            mode.opponentEyeshadowRScore = 0
        
        blushLXValuesO = []
        blushLYValuesO = []
        for (x,y,r) in mode.drawnBlushL:
            blushLXValuesO.append(x)
            blushLYValuesO.append(y)
        if len(blushLXValuesO) > 0:
            blushLMinXO = min(blushLXValuesO)
            blushLMaxXO = max(blushLXValuesO)
            blushLMinYO = min(blushLYValuesO)
            blushLMaxYO = max(blushLYValuesO)
            print(f'len L blush {len(blushLXValuesO)}')
        
            if blushLMaxXO-blushLMinXO >= 22 and blushLMaxYO-blushLMinYO >= 21 and len(blushLXValuesO) >= 60: 
                mode.opponentBlushLScore = 100
            if len(blushLXValuesO) < 60:
                mode.opponentBlushLScore -= 10
            if len(blushLXValuesO) <= 50:
                mode.opponentBlushLScore -= 10
            if len(blushLXValuesO) <= 40:
                mode.opponentBlushLScore -= 10
            if blushLMaxYO-blushLMinYO < 21:
                mode.opponentBlushLScore -= (21 - (blushLMaxYO-blushLMinYO))
            if blushLMaxXO-blushLMinXO < 22:
                mode.opponentBlushLScore -= (22 - (blushLMaxXO-blushLMinXO))
            
        elif blushLXValuesO == []:
            mode.opponentBlushLScore = 0

        blushRXValuesO = []
        blushRYValuesO = []
        for (x,y,r) in mode.drawnBlushR:
            blushRXValuesO.append(x)
            blushRYValuesO.append(y)
        if len(blushRXValuesO) > 0:
            blushRMinXO = min(blushRXValuesO)
            blushRMaxXO = max(blushRXValuesO)
            blushRMinYO = min(blushRYValuesO)
            blushRMaxYO = max(blushRYValuesO)
            print(f'len R blush {len(blushRXValuesO)}')
            print(f'x-x: {blushRMaxXO-blushRMinXO}')
            print(f'y-y: {blushRMaxYO-blushRMinYO}')

            if blushRMaxXO-blushRMinXO >= 22 and blushRMaxYO-blushRMinYO >= 21 and len(blushRXValuesO) >= 60: 
                mode.opponentBlushRScore = 100
            if len(blushRXValuesO) < 60:
                mode.opponentBlushRScore -= 10
            if len(blushRXValuesO) <= 50:
                mode.opponentBlushRScore -= 10
            if len(blushRXValuesO) <= 40:
                mode.opponentBlushRScore -= 10
            if blushRMaxYO-blushRMinYO < 21:
                mode.opponentBlushRScore -= (21 - (blushRMaxYO-blushRMinYO))
            if blushRMaxYO-blushRMinXO < 22:
                mode.opponentBlushRScore -= (22 - (blushRMaxXO-blushRMinXO))
            
        elif blushRXValuesO == []:
            mode.opponentBlushRScore = 0

        lipstickXValuesO = []
        lipstickYValuesO = []
        for (x,y,r) in mode.drawnLipstick:
            lipstickXValuesO.append(x)
            lipstickYValuesO.append(y)
        if len(lipstickXValuesO) > 0:
            lipstickMinXO = min(lipstickXValuesO)
            lipstickMaxXO = max(lipstickXValuesO)
            lipstickMinYO = min(lipstickYValuesO)
            lipstickMaxYO = max(lipstickYValuesO)
            print(lipstickMinYO, lipstickMaxYO)
            print(f'len lip {len(lipstickXValuesO)}')

            if StartMode.easy:
                if (lipstickMaxXO-lipstickMinXO >= 37 and lipstickMaxYO-lipstickMinYO >= 13 and
                    lipstickMaxXO-lipstickMinXO < 39 and lipstickMaxYO-lipstickMinYO < 15 and
                    len(lipstickXValuesO) >= 250 ): 
                    mode.opponentLipstickScore = 100
                if len(lipstickXValuesO) < 250:
                    mode.opponentLipstickScore -= 20
                if len(lipstickXValuesO) < 200:
                    mode.opponentLipstickScore -= 10
                if len(lipstickXValuesO) < 100:
                    mode.opponentLipstickScore -= 10
                if lipstickMaxXO-lipstickMinXO >= 39: 
                    mode.opponentLipstickScore -= ((lipstickMaxXO-lipstickMinXO) - 39)
                if lipstickMaxYO-lipstickMinYO >= 15:
                    mode.opponentLipstickScore -= ((lipstickMaxYO-lipstickMinYO) - 15)
                if lipstickMaxYO-lipstickMinYO < 13:
                    mode.opponentLipstickScore -= (13 - (lipstickMaxYO-lipstickMinYO))
                if lipstickMaxXO-lipstickMinXO < 37: 
                    mode.opponentLipstickScore -= (37 - (lipstickMaxXO-lipstickMinXO))
            elif StartMode.hard:
                if len(lipstickXValuesO) >= 180:
                    mode.opponentLipstickScore = 100
                elif 100 <= len(lipstickXValuesO) < 180:
                    mode.opponentLipstickScore -= (180 - len(lipstickXValuesO))
                else:
                    mode.opponentLipstickScore -= (100 - len(lipstickXValuesO)//5)

        elif lipstickXValuesO == []:
            mode.opponentLipstickScore = 0
        
        mode.opponentScore = int(mode.opponentEyeshadowLScore + mode.opponentEyeshadowRScore \
                            + mode.opponentBlushLScore + mode.opponentBlushRScore \
                            + mode.opponentLipstickScore)//5

        if mode.opponentScore < 0:
            mode.opponentScore = 0

        print(mode.opponentEyeshadowLScore, mode.opponentEyeshadowRScore, \
            mode.opponentBlushLScore,mode.opponentBlushRScore, \
            mode.opponentLipstickScore)

    def calculateYourScore(mode):    
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
                eyeshadowLMinX > 610 and eyeshadowLMinY > 260 and len(eyeshadowLXValues) >= 35):
                mode.yourEyeshadowLScore = 100
            if len(eyeshadowLXValues) < 35:
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
                eyeshadowRMinX > 705 and eyeshadowRMinY > 260 and len(eyeshadowRXValues) >= 35):
                mode.yourEyeshadowRScore = 100
            if len(eyeshadowRXValues) < 35:
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
                blushLMaxX-blushLMinX <= 24 and blushLMaxY-blushLMinY <= 24 and
                blushLMinX > 625 and blushLMinY > 315): 
                mode.yourBlushLScore = 100
            if blushLMinX <= 625:
                mode.yourBlushLScore -= 10
            if blushLMinY <= 315:
                mode.yourBlushRScore -= 10
            if blushLMaxX-blushLMinX > 24: 
                mode.yourBlushLScore -= ((blushLMaxX-blushLMinX) - 24)
            if blushLMaxY-blushLMinY > 24:
                mode.yourBlushLScore -= ((blushLMaxY-blushLMinY) - 24)
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
                blushRMaxX-blushRMinX <= 24 and blushRMaxY-blushRMinY <= 24 and
                blushRMinX > 720 and blushRMinY > 315): 
                mode.yourBlushRScore = 100
            if blushRMinX <= 720:
                mode.yourBlushRScore -= 10
            if blushRMinY <= 315:
                mode.yourBlushRScore -= 10
            if blushRMaxX-blushRMinX > 24: 
                mode.yourBlushRScore -= ((blushRMaxX-blushRMinX) - 24)
            if blushRMaxY-blushRMinY > 24:
                mode.yourBlushRScore -= ((blushRMaxY-blushRMinY) - 24)
            if blushRMaxY-blushRMinY < 20:
                mode.yourBlushRScore -= (20 - (blushRMaxY-blushRMinY))
            if blushRMaxX-blushRMinX < 20: 
                mode.yourBlushRScore -= (20 - (blushRMaxX-blushRMinX))
           
        elif blushRXValues == []:
            mode.yourBlushRScore = 0

        for (cx, cy, r, color) in mode.drawnBlushRDots:
            if color != mode.correctBlushColor:
                mode.yourBlushRScore -= 10

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
                lipstickMinX > 665 and lipstickMinY > 350 and len(lipstickXValues) >= 50): 
                mode.yourLipstickScore = 100
            if len(lipstickXValues) < 50:
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
        
        mode.yourScore = int(mode.yourEyeshadowLScore+mode.yourEyeshadowRScore \
                        + mode.yourBlushLScore+mode.yourBlushRScore \
                        + mode.yourLipstickScore)//5

        if mode.yourScore < 0:
            mode.yourScore = 0

        print(f'your scores: {mode.yourEyeshadowLScore,mode.yourEyeshadowRScore,mode.yourBlushLScore,mode.yourBlushRScore,mode.yourLipstickScore}')

    def resizeDrawings(mode):
        mode.drawEyeshadowLScoringScreen = mode.scaleImage(mode.loadImage('images/draw/drawEyeshadowL.png'), 1/2)
        mode.drawEyeshadowRScoringScreen = mode.scaleImage(mode.loadImage('images/draw/drawEyeshadowR.png'), 1/2)
        mode.drawBlushRScoringScreen = mode.scaleImage(mode.loadImage('images/draw/drawBlushR.png'), 1/2)
        mode.drawLipstickScoringScreen = mode.scaleImage(mode.loadImage('images/draw/drawLipstick.png'), 1/2)
        mode.drawOpponentEyeshadowLScoringScreen = mode.scaleImage(mode.loadImage('images/draw/drawOpponentEyeshadowL.png'), 1/2)
        mode.drawOpponentEyeshadowRScoringScreen = mode.scaleImage(mode.loadImage('images/draw/drawOpponentEyeshadowR.png'), 1/2)
        mode.drawOpponentBlushLScoringScreen = mode.scaleImage(mode.loadImage('images/draw/drawOpponentBlushL.png'), 1/2)
        mode.drawOpponentBlushRScoringScreen = mode.scaleImage(mode.loadImage('images/draw/drawOpponentBlushR.png'), 1/2)
        mode.drawOpponentLipstickScoringScreen = mode.scaleImage(mode.loadImage('images/draw/drawOpponentLipstick.png'), 1/2)

    def drawCustomerScreen(mode, canvas):
        customer = GameMode.getCachedPhotoImage(mode, mode.customer)
        canvas.create_image(mode.cx - 150, mode.cy + 50, image = customer)

        canvas.create_text(mode.cx, 70, text = "A customer has arrived!", font = "Silom 50 bold", fill = "black")
        canvas.create_oval(mode.cx + 225 + 220, mode.cy + 100, mode.cx + 225 - 220, mode.cy - 100, fill = "white", outline = "powder blue")
        canvas.create_text(mode.cx + 225, mode.cy, text = f"\"I would like \n{mode.eyeshadowColor} eyeshadow, \nwith {mode.blushColor} blush, \nand {mode.lipstickColor} lipstick.\"",
                                font = "Arial 30 bold")
        canvas.create_rectangle(mode.cx + 175, mode.height - 125, mode.cx + 275, mode.height - 75, fill = "pink", outline = "")
        canvas.create_text(mode.cx + 225, mode.height - 100, text = "Go!", font = "Silom 30 bold", fill = "black")

        #instructions to open help
        canvas.create_rectangle(10, mode.height - 45, 180, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Press H for Help", font = "Arial 20 bold", fill = "black")

    def drawGameScreen(mode, canvas):
        #timer
        canvas.create_line(mode.cx - 30, 0, mode.cx - 30, mode.height, fill = "black", width = 5)
        canvas.create_rectangle(mode.cx - 80 - 30, 0, mode.cx + 80 - 30, 40, fill = "white", outline = "black")
        canvas.create_text(mode.cx - 30, 20, text=f'{int(mode.timeLeft)}s remaining', font="Arial 20 bold")

        #customer and order
        customer = GameMode.getCachedPhotoImage(mode, mode.customer)
        canvas.create_image(mode.cx // 2 - 30, mode.cy + 50, image = customer)
        canvas.create_image(mode.cx + mode.cx // 2 - 60, mode.cy + 50, image = customer)
        
        canvas.create_text(mode.cx // 2 - 30, 70, text=StartMode.name, font="Silom 30 bold")
        canvas.create_text(mode.cx + mode.cx // 2 - 60, 70, text= "".join(LoginScreen.username), font="Silom 30 bold")
        canvas.create_rectangle(mode.cx - 100 - 30, 50, mode.cx + 100 - 30, 160, fill = "white", outline = "powder blue")
        canvas.create_text(mode.cx - 30, 60, text = f"Check List:\n- {mode.eyeshadowColor} eyeshadow\n- {mode.blushColor} blush\n- {mode.lipstickColor} lipstick",
                                font = "Arial 20", anchor = "n")
        
        #submit button
        canvas.create_rectangle(mode.cx - 30 - 60, mode.cy + mode.cy//3 - 30, mode.cx - 30 + 60, mode.cy + mode.cy//3 + 30, fill = "pink", outline = "")
        canvas.create_text(mode.cx - 30, mode.cy + mode.cy//3, text = "SUBMIT", font = "Silom 22")

        #instructions to open help and pause
        canvas.create_rectangle(10, mode.height - 70, 190, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Press H for Help \nPress P to Pause", font = "Arial 20 bold", fill = "black")

    def timeIsUp(mode, canvas):
        if mode.timeEnd:
            canvas.create_rectangle(mode.cx - 200, mode.cy - 100, mode.cx + 200, mode.cy + 100, fill = "light gray", outline = "")
            canvas.create_text(mode.cx, mode.cy, text="Time is Up!", font="Silom 50 bold")

    def drawColorOptions(mode, canvas):
        boxHeight = mode.height // 4

        products = ["Eyeshadow", "Blush", "Lipstick", "Erase"]
        pictures = [mode.eyeshadow, mode.blush, mode.lipstick, mode.erase]

        for i in range(len(products)):
            canvas.create_rectangle(mode.width - 100, i * boxHeight, mode.width, (i+1) * boxHeight, fill = "pink", outline = "black")

        if mode.eyeshadowSelection:
            canvas.create_rectangle(mode.width - 100, 0 * boxHeight, mode.width, (0+1) * boxHeight, fill = "powder blue")
        if mode.blushSelection:
            canvas.create_rectangle(mode.width - 100, 1 * boxHeight, mode.width, (1+1) * boxHeight, fill = "powder blue")
        if mode.lipstickSelection:
            canvas.create_rectangle(mode.width - 100, 2 * boxHeight, mode.width, (2+1) * boxHeight, fill = "powder blue")
        if mode.eraserSelection:
            canvas.create_rectangle(mode.width - 100, 3 * boxHeight, mode.width, (3+1) * boxHeight, fill = "powder blue")

        for i in range(len(products)):
            product = GameMode.getCachedPhotoImage(mode, pictures[i])
            canvas.create_image(mode.width - 50, (i + 0.4) * boxHeight, image = product)
            canvas.create_text(mode.width - 50, (i + 0.8) * boxHeight, text = f'{products[i]}', font = "Arial 15 bold")

        if mode.eyeshadowSelection:
            #eyeshadow color options
            for i in range(len(mode.eyeshadowColors)):
                color = "#%02x%02x%02x" % mode.eyeshadowColorCodes[i]
                canvas.create_rectangle(mode.width - 150, i * 50, mode.width - 100, (i+1) * 50, fill = color)
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

        elif mode.blushSelection:
            #blush color options
            for i in range(len(mode.blushColors)):
                color = "#%02x%02x%02x" % mode.blushColorCodes[i]
                canvas.create_rectangle(mode.width - 150, 125 + i * 50, mode.width - 100, 125 + (i+1) * 50, fill = color)
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

        elif mode.lipstickSelection:
            #lipstick color options
            for i in range(len(mode.lipstickColors)):
                color = "#%02x%02x%02x" % mode.lipstickColorCodes[i]
                canvas.create_rectangle(mode.width - 150, 250 + i * 50, mode.width - 100, 250 + (i+1) * 50, fill = color)
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
        if mode.released == False:
            if mode.eyeshadowSelection:
                if mode.left:
                    for (cx, cy, r, color) in mode.drawnEyeshadowLDots[:-1]:
                        colorR = color[0]
                        colorG = color[1]
                        colorB = color[2]
                        color = "#%02x%02x%02x" % (colorR, colorG, colorB)
                        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '') 
                else: 
                    for (cx, cy, r, color) in mode.drawnEyeshadowRDots[:-1]:
                        colorR = color[0]
                        colorG = color[1]
                        colorB = color[2]
                        color = "#%02x%02x%02x" % (colorR, colorG, colorB)
                        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')  
                            
            if mode.blushSelection:
                if mode.left:
                    for (cx, cy, r, color) in mode.drawnBlushLDots[:-1]:
                        colorR = color[0]
                        colorG = color[1]
                        colorB = color[2]
                        color = "#%02x%02x%02x" % (colorR, colorG, colorB)
                        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')
                else:
                    for (cx, cy, r, color) in mode.drawnBlushRDots[:-1]:
                        colorR = color[0]
                        colorG = color[1]
                        colorB = color[2]
                        color = "#%02x%02x%02x" % (colorR, colorG, colorB)
                        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')

            if mode.lipstickSelection:
                for (cx, cy, r, color) in mode.drawnLipstickDots[:-1]:
                    colorR = color[0]
                    colorG = color[1]
                    colorB = color[2]
                    color = "#%02x%02x%02x" % (colorR, colorG, colorB)
                    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')

        if mode.drawnEyeshadowLDots != []:
            canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.drawEyeshadowL))
        if mode.drawnEyeshadowRDots != []:
            canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.drawEyeshadowR))
        if mode.drawnBlushLDots != []:
            canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.drawBlushL))
        if mode.drawnBlushRDots != []:
            canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.drawBlushR))
        if mode.drawnLipstickDots != []:
            canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.drawLipstick))

        if mode.colorShow == True:
            cx = mode.penX
            cy = mode.penY
            r = mode.penR
            color = "#%02x%02x%02x" % mode.selectedColor
            #current dot that is being dragged has an outline
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color) 

    def opponentDrawing(mode, canvas):
        if mode.filledEyeshadowL:
            canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.drawOpponentEyeshadowL))
        if mode.filledEyeshadowR:
            canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.drawOpponentEyeshadowR))
        if mode.filledBlushL:
            canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.drawOpponentBlushL))
        if mode.filledBlushR:   
            canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.drawOpponentBlushR))
        if mode.filledLipstick:
            canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.drawOpponentLipstick))
        
        if mode.filledBlushL == False:
            for (cx, cy, r) in mode.drawnBlushL:
                mode.opponentR = r
                color = "#%02x%02x%02x" % mode.correctBlushColor
                canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')  
        
        if mode.filledBlushR == False: 
            for (cx, cy, r) in mode.drawnBlushR:
                mode.opponentR = r
                color = "#%02x%02x%02x" % mode.correctBlushColor
                canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')  

        if mode.filledEyeshadowL == False:
            for (cx, cy, r) in mode.drawnEyeshadowL:
                mode.opponentR = r
                color = "#%02x%02x%02x" % mode.correctEyeshadowColor
                canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')  

        if mode.filledEyeshadowR == False:
            for (cx, cy, r) in mode.drawnEyeshadowR:
                mode.opponentR = r
                color = "#%02x%02x%02x" % mode.correctEyeshadowColor
                canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')  
        
        if mode.filledLipstick == False:
            for (cx, cy, r) in mode.drawnLipstick:
                mode.opponentR = r
                color = "#%02x%02x%02x" % mode.correctLipstickColor
                canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')  

    def drawScoringScreen(mode, canvas):
        #labels
        canvas.create_rectangle(mode.cx // 2 - 150, 90 - 45, mode.cx // 2 + 150, 90 + 45, fill = 'white', outline = '')
        canvas.create_rectangle(mode.cx + mode.cx // 2 - 150, 90 - 45, mode.cx + mode.cx // 2 + 150, 90 + 45, fill = 'white', outline = '')
        canvas.create_text(mode.cx // 2, 70, text=StartMode.name, font="Silom 30 bold")
        canvas.create_text(mode.cx // 2, 110, text=f'Score: {mode.opponentScore}%', font="Silom 30 ")
        canvas.create_text(mode.cx + mode.cx // 2, 70, text="".join(LoginScreen.username), font="Silom 30 bold")
        canvas.create_text(mode.cx + mode.cx // 2, 110, text=f'Score: {mode.yourScore}%', font="Silom 30 ")

        canvas.create_rectangle(0, mode.cy - 65 - 40, mode.width, mode.cy - 65 + 40, fill = 'white', outline = '')
        if mode.yourScore > mode.opponentScore:
            canvas.create_text(mode.cx, mode.cy - 65, text='You Win! Congrats on getting hired!', font="Silom 40 bold")
        elif mode.yourScore < mode.opponentScore:
            canvas.create_text(mode.cx, mode.cy - 65, text=f'Better luck next time, {StartMode.name} beat you.', font="Silom 40 bold")
        elif mode.yourScore == mode.opponentScore:
            canvas.create_text(mode.cx, mode.cy - 65, text=f"It's a tie... try to beat {StartMode.name} next time.", font="Silom 40 bold")
    
        canvas.create_rectangle(mode.cx // 2 - 90, mode.cy + mode.cy//3 - 100, mode.cx // 2 + 90, mode.cy + mode.cy//3 + 100, fill = 'white')
        canvas.create_rectangle(mode.cx + mode.cx // 2 - 90, mode.cy + mode.cy//3 - 100, mode.cx + mode.cx // 2 + 90, mode.cy + mode.cy//3 + 100, fill = 'white')

        customer = GameMode.getCachedPhotoImage(mode, mode.customerScoringScreen)
        canvas.create_image(mode.cx // 2, mode.cy + mode.cy//3, image = customer)
        canvas.create_image(mode.cx + mode.cx // 2, mode.cy + mode.cy//3, image = customer)
    
        canvas.create_image(mode.cx + mode.cx//4 + 30, mode.cy + 58, image = ImageTk.PhotoImage(mode.drawEyeshadowLScoringScreen))
        canvas.create_image(mode.cx + mode.cx//4 + 30, mode.cy + 58, image = ImageTk.PhotoImage(mode.drawEyeshadowRScoringScreen))
        canvas.create_image(mode.cx + mode.cx//4 + 30, mode.cy + 58, image = ImageTk.PhotoImage(mode.drawBlushLScoringScreen))
        canvas.create_image(mode.cx + mode.cx//4 + 30, mode.cy + 58, image = ImageTk.PhotoImage(mode.drawBlushRScoringScreen))
        canvas.create_image(mode.cx + mode.cx//4 + 30, mode.cy + 58, image = ImageTk.PhotoImage(mode.drawLipstickScoringScreen))

        canvas.create_image(mode.cx - mode.cx//4 + 15, mode.cy + 58, image = ImageTk.PhotoImage(mode.drawOpponentEyeshadowLScoringScreen))
        canvas.create_image(mode.cx - mode.cx//4 + 15, mode.cy + 58, image = ImageTk.PhotoImage(mode.drawOpponentEyeshadowRScoringScreen))
        canvas.create_image(mode.cx - mode.cx//4 + 15, mode.cy + 58, image = ImageTk.PhotoImage(mode.drawOpponentBlushLScoringScreen))
        canvas.create_image(mode.cx - mode.cx//4 + 15, mode.cy + 58, image = ImageTk.PhotoImage(mode.drawOpponentBlushRScoringScreen))
        canvas.create_image(mode.cx - mode.cx//4 + 15, mode.cy + 58, image = ImageTk.PhotoImage(mode.drawOpponentLipstickScoringScreen))

        #restart button
        canvas.create_rectangle(mode.cx - 100, mode.height - 80 - 40, mode.cx + 100, mode.height - 80 + 40, fill = "pink", outline = "")
        canvas.create_text(mode.cx, mode.height - 80, text = "Try Again", font = "Silom 30 bold", fill = "black")

        #show leaderboard option
        canvas.create_rectangle(10, mode.height - 45, 210, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Show Leaderboard", font = "Arial 20 bold", fill = "black")
        
        #log out
        canvas.create_rectangle(mode.width - 110, mode.height - 45, mode.width - 10, mode.height - 10, fill = "white", outline = "powder blue")
        canvas.create_text(mode.width - 20, mode.height - 15, anchor = 'se', text = "Log Out", font = "Arial 20 bold", fill = "black")

    def redrawAll(mode, canvas):
        #background
        bg = GameMode.getCachedPhotoImage(mode, mode.background)
        canvas.create_image(mode.cx, mode.cy, image = bg)

        if mode.customerScreen:
            GameMode.drawCustomerScreen(mode, canvas)

        elif mode.gameScreen:
            GameMode.drawGameScreen(mode,canvas)
            GameMode.drawing(mode, canvas)
            GameMode.drawColorOptions(mode, canvas)
            GameMode.timeIsUp(mode, canvas)
            GameMode.opponentDrawing(mode, canvas)

        elif mode.scoringScreen:
            GameMode.drawScoringScreen(mode, canvas)
