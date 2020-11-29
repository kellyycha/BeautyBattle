from cmu_112_graphics import *
from tkinter import *
import random
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
        mode.timeLeft = 31
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
        mode.drawnBlushDots = []
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

        mode.yourScore = 0
        mode.opponentScore = 70

        mode.opponentDrawnEyeshadowDots = []
        mode.AmateurSolutionEyeshadowDots = [(242, 281), (248, 277), (250, 275), (253, 273), (255, 272), (261, 271), (263, 270), 
                                            (271, 268), (273, 268), (279, 268), (283, 268), (287, 268), (289, 268), (293, 268), 
                                            (295, 269), (297, 269), (295, 269), (291, 268), (288, 268), (285, 267), (282, 267),
                                            (276, 267), (272, 268), (267, 268), (265, 268), (259, 270), (257, 270), (253, 272),
                                            (251, 274), (248, 275), (246, 276), (245, 278), (244, 278), (204, 285), (204, 283), 
                                            (202, 281), (201, 281), (197, 279), (196, 278), (192, 276), (191, 275), (187, 274), 
                                            (186, 274), (184, 273), (182, 272), (178, 270), (177, 270), (174, 268), (172, 268), 
                                            (169, 267), (166, 266), (161, 265), (158, 265), (155, 264), (154, 264), (154, 265), 
                                            (153, 266), (151, 268), (151, 269), (152, 269), (154, 270), (160, 270), (163, 269),
                                            (170, 268), (174, 268), (180, 269), (182, 269), (186, 270), (189, 272), (197, 275), 
                                            (198, 276), (202, 279), (202, 280)]
        mode.opponentDrawnBlushDots = []
        mode.AmateurSolutionBlushDots = [(279, 323), (277, 319), (273, 317), (266, 317), (263, 318), (258, 321), (257, 322), (256, 326), 
                                        (256, 329), (257, 332), (258, 335), (260, 336), (261, 337), (265, 338), (270, 339), (274, 339), 
                                        (275, 339), (279, 337), (280, 336), (284, 332), (285, 330), (287, 326), (287, 324), (284, 323), 
                                        (282, 322), (277, 320), (276, 319), (274, 319), (272, 319), (268, 322), (267, 323), (267, 327), 
                                        (163, 316), (162, 317), (158, 322), (157, 324), (157, 329), (157, 332), (158, 334), (159, 335), 
                                        (162, 337), (165, 338), (169, 339), (173, 339), (178, 339), (181, 339), (185, 339), (187, 339), 
                                        (193, 337), (195, 335), (197, 333), (198, 331), (198, 327), (197, 326), (195, 325), (193, 324), 
                                        (190, 322), (188, 321), (185, 320), (183, 319), (180, 317), (178, 317), (173, 315), (172, 315), 
                                        (168, 316), (167, 318), (167, 320), (173, 322), (176, 323), (177, 323)]
        mode.opponentDrawnLipstickDots = []
        mode.AmateurSolutionLipstickDots = [(204, 362), (206, 361), (210, 359), (213, 359), (216, 359), (218, 359), (222, 359), 
                                            (225, 359), (227, 359), (230, 360), (237, 361), (236, 362), (232, 363), (229, 364), 
                                            (226, 365), (224, 365), (221, 365), (219, 365), (215, 365), (213, 365), (209, 364), 
                                            (208, 364), (206, 363), (203, 362), (202, 361), (201, 360), (202, 360), (207, 358), 
                                            (209, 358), (210, 356), (212, 356), (213, 357), (217, 358), (219, 358), (221, 357), 
                                            (223, 357), (224, 356), (226, 356), (229, 356), (231, 357), (232, 357), (238, 360), 
                                            (236, 360), (235, 361), (231, 364), (230, 365), (225, 367), (224, 367), (221, 367), 
                                            (219, 367), (215, 366), (214, 366), (213, 366), (211, 364), (211, 363), (213, 362)]
                                            
    def mousePressed(mode, event):
        #print(f'{(event.x,event.y)},')
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
                            mode.drawnBlushDots.append((event.x, event.y, mode.penR, mode.selectedColor))
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
                    if mode.timerCount < len(mode.AmateurSolutionEyeshadowDots):
                        mode.opponentDrawnEyeshadowDots.append(mode.AmateurSolutionEyeshadowDots[mode.timerCount])
                    if 20 + len(mode.AmateurSolutionEyeshadowDots) <= mode.timerCount < 20 + len(mode.AmateurSolutionEyeshadowDots) + len(mode.AmateurSolutionBlushDots):
                        mode.opponentDrawnBlushDots.append(mode.AmateurSolutionBlushDots[mode.timerCount - 20 -len(mode.AmateurSolutionEyeshadowDots)])
                    if 40 + len(mode.AmateurSolutionEyeshadowDots) + len(mode.AmateurSolutionBlushDots) <= mode.timerCount <40 + len(mode.AmateurSolutionLipstickDots) + len(mode.AmateurSolutionEyeshadowDots) + len(mode.AmateurSolutionBlushDots):
                        mode.opponentDrawnLipstickDots.append(mode.AmateurSolutionLipstickDots[mode.timerCount - 40 -(len(mode.AmateurSolutionEyeshadowDots) + len(mode.AmateurSolutionBlushDots))])

                mode.timerCount += 1

        #automatically shows the scoring screen 2 seconds after time ends
        if mode.scoringScreen == False and mode.timerCount > 33*10:
            mode.scoringScreen = True
            mode.gameScreen = False

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
            rightBlushBounds = [(715, 321),(721, 313),(731, 310),(742, 310),(754, 313),(760, 320),(762, 333),(754, 344),
                                (741, 348),(726, 344),(715, 339),(711, 330)]
            leftBlushBounds = []
            for (x,y) in rightBlushBounds:
                newX = (mode.width - 30 - x) + (mode.cx - 90)
                leftBlushBounds.append((newX,y))
            for (x,y) in rightBlushBounds:
                canvas.create_text(x, y, text = '·')
            for (x,y) in leftBlushBounds:
                canvas.create_text(x, y, text = '·')

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
        for (cx, cy) in mode.opponentDrawnEyeshadowDots:
            r = 5
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = mode.correctEyeshadowColor, outline = '')
        for (cx, cy) in mode.opponentDrawnBlushDots:
            r = 10
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = mode.correctBlushColor, outline = '')
        for (cx, cy) in mode.opponentDrawnLipstickDots:
            r = 5
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = mode.correctLipstickColor, outline = '')

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