from cmu_112_graphics import *
from tkinter import *
import random
import os

class GameMode(Mode):
    def appStarted(mode):
        parentDir = os.path.abspath("..")
        img_dir = os.path.join(parentDir, "termProject/images/background.jpg")
        mode.background = mode.loadImage(img_dir)
        
        mode.customerScreen = True
        mode.gameScreen = False
        mode.scoringScreen = False

        mode.timeLeft = 61
        mode.timerCount = 0
        mode.timeEnd = False
        mode.pause = False

        mode.customer()
        mode.colorPicker()
        mode.productImages()

        mode.eyeshadowSelection = False
        mode.blushSelection = False
        mode.lipstickSelection = False
        mode.eraserSelection = False

        mode.penX = mode.penY = mode.penR = 0
        mode.selectedColor = '' 
        mode.colorShow = False
        mode.drawnDots = []

    def customer(mode):
        parentDir = os.path.abspath("..")
        # Customers generated with: https://www.cartoonify.de/#cartoonify
        customers = ["customer1.png", "customer2.png", "customer3.png","customer4.png","customer5.png","customer6.png"]
        customer = random.choice(customers)
        img_dir = os.path.join(parentDir, f"termProject/images/customers/{customer}")
        mode.customer = mode.scaleImage(mode.loadImage(img_dir), 2/3)
    
    def productImages(mode):
        parentDir = os.path.abspath("..")
        # Eyeshadow image: http://clipart-library.com/clipart/1401830.htm 
        img_dir = os.path.join(parentDir, "termProject/images/eyeshadow.png")
        mode.eyeshadow = mode.scaleImage(mode.loadImage(img_dir), 1/6)
        # Blush image: https://webstockreview.net/pict/getfirst 
        img_dir = os.path.join(parentDir, "termProject/images/blush.png")
        mode.blush = mode.scaleImage(mode.loadImage(img_dir), 1/5)
        # Lipstick image: https://pngriver.com/pink-lipstick-png-transparent-clipart-image-2-5461/women-lipstick-png-transparent-images-transparent-backgrounds-pink-lipstick-png-12/ 
        img_dir = os.path.join(parentDir, "termProject/images/lipstick.png")
        mode.lipstick = mode.scaleImage(mode.loadImage(img_dir), 1/9)
        # Eraser image: http://clipart-library.com/clipart/15308.htm 
        img_dir = os.path.join(parentDir, "termProject/images/erase.png")
        mode.erase = mode.scaleImage(mode.loadImage(img_dir), 1/5)

    def colorPicker(mode):
        mode.eyeshadowColors = ["pink", "orange", "gold", "green", "blue", "purple"]
        mode.eyeshadowColorNames = ["hot pink", "dark orange", "gold", "yellow green", "deep sky blue", "medium orchid"]
        mode.eyeshadowColor = random.choice(mode.eyeshadowColors)
        mode.blushColors = ["pink", "red", "peach", "orange"]
        mode.blushColorNames = ["hot pink", "red", "salmon", "dark orange"]
        mode.blushColor = random.choice(mode.blushColors)
        mode.lipstickColors = ["pink", "red", "nude", "purple"]
        mode.lipstickColorNames = ["hot pink", "red", "LightSalmon2", "medium orchid"]
        mode.lipstickColor = random.choice(mode.lipstickColors)   
    
    def mousePressed(mode, event):
        print(f'{(event.x,event.y)},')

        if mode.timeEnd:
            return

        if mode.pause == False:
            if mode.customerScreen:
                if (670 <= event.x <= 775) and (370 <= event.y < 425):
                    mode.customerScreen = False
                    mode.gameScreen = True
            
            if mode.gameScreen: 
                #eyeshadow selected
                if (mode.width - 100 <= event.x <= mode.width) and (0 <= event.y < 125):
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


    def mouseDragged(mode, event):
        if mode.pause == False:
            if (600 <= event.x <= 780) and (190 <= event.y < 390):
                mode.colorShow = True
                mode.penX = event.x
                mode.penY = event.y
                mode.drawnDots.append((event.x, event.y, mode.penR, mode.selectedColor))
            if mode.eraserSelection:
                GameMode.eraserIntersect(mode)

    def eraserIntersect(mode):
        for (cx, cy, r, color) in mode.drawnDots:
            distanceFormula = ((mode.penX - cx)**2 + (mode.penY - cy)**2)**0.5
            if (distanceFormula <= mode.penR + r):
                mode.drawnDots.remove((cx, cy, r, color))

    def keyPressed(mode, event):
        if event.key == "h":
            mode.pause = True
            mode.app.setActiveMode(mode.app.helpMode)
            mode.pause = False

        if event.key == "p":
            mode.pause = not mode.pause

    def timerFired(mode):
        if mode.pause == False:
            if mode.gameScreen:
                if mode.timerCount % 10 == 0: 
                    if mode.timeLeft > 0:
                        mode.timeLeft -= 1
                    else:
                        mode.timeEnd = True
                mode.timerCount += 1

        if mode.timeEnd:
            mode.scoringScreen = True

    def drawCustomerScreen(mode, canvas):
        cx, cy = mode.width // 2, mode.height // 2

        canvas.create_text(cx, 70, text = "A customer has arrived!", font = "Arial 50 bold", fill = "black")
        canvas.create_image(cx - 150, cy + 50, image = ImageTk.PhotoImage(mode.customer))
        canvas.create_oval(cx + 225 + 220, cy + 100, cx + 225 - 220, cy - 100, fill = "white", outline = "pink")
        canvas.create_text(cx + 225, cy, text = f"\"I would like \n{mode.eyeshadowColor} eyeshadow, \nwith {mode.blushColor} blush, \nand {mode.lipstickColor} lipstick.\"",
                                font = "Arial 30 bold")
        canvas.create_rectangle(cx + 175, mode.height - 125, cx + 275, mode.height - 75, fill = "pink", outline = "")
        canvas.create_text(cx + 225, mode.height - 100, text = "Go!", font = "Arial 30 bold", fill = "black")

        #instructions to open help
        canvas.create_rectangle(10, mode.height - 45, 180, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Press H for Help", font = "Arial 20 bold", fill = "black")

    def drawGameScreen(mode, canvas):
        cx, cy = mode.width // 2, mode.height // 2

        #timer
        canvas.create_line(cx - 30, 0, cx - 30, mode.height, fill = "black", width = 5)
        canvas.create_rectangle(cx - 80 - 30, 0, cx + 80 - 30, 40, fill = "white", outline = "black")
        canvas.create_text(cx - 30, 20, text=f'{mode.timeLeft}s remaining', font="Arial 20 bold")

        #customer and order
        canvas.create_text(cx // 2 - 30, 70, text='Opponent', font="Arial 30 bold")
        canvas.create_image(cx // 2 - 30, cy + 50, image = ImageTk.PhotoImage(mode.customer))
        canvas.create_text(cx + cx // 2 - 60, 70, text='You', font="Arial 30 bold")
        canvas.create_image(cx + cx // 2 - 60, cy + 50, image = ImageTk.PhotoImage(mode.customer))
        canvas.create_rectangle(cx - 100 - 30, 50, cx + 100 - 30, 160, fill = "white", outline = "black")
        canvas.create_text(cx - 30, 60, text = f"Check List:\n- {mode.eyeshadowColor} eyeshadow\n- {mode.blushColor} blush\n- {mode.lipstickColor} lipstick",
                                font = "Arial 20", anchor = "n")
            
        #makeup
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
        cx, cy = mode.width // 2, mode.height // 2
        if mode.timeEnd:
                canvas.create_rectangle(cx - 200, cy - 100, cx + 200, cy + 100, fill = "gray", outline = "black")
                canvas.create_text(cx, cy, text="Time is Up!", font="Arial 50 bold")

    def drawColorOptions(mode, canvas):
        cx, cy = mode.width // 2, mode.height // 2

        if mode.eyeshadowSelection == True:
            for i in range(len(mode.eyeshadowColors)):
                canvas.create_rectangle(mode.width - 150, i * 50, mode.width - 100, (i+1) * 50, fill = mode.eyeshadowColorNames[i])
                canvas.create_text(mode.width - 125, (i + 0.5) * 50, text = f'{mode.eyeshadowColors[i]}', font = "Arial 15")
            rightEyeBounds = [(711, 286),(713, 283),(715, 282),(718, 280),(721, 278),(725, 277),(731, 276),(735, 276),(738, 276),
                            (742, 275),(746, 275),(750, 275),(752, 275),(754, 275),(759, 276),(762, 272),(764, 270),(764, 268),
                            (763, 266),(760, 263),(755, 262),(750, 262),(744, 262),(736, 263),(728, 265),(721, 268),(716, 270),
                            (712, 273),(710, 276),(708, 279),(708, 284),(709, 287)]
            leftEyeBounds = []
            for (x,y) in rightEyeBounds:
                newX = (mode.width - 30 - x) + (cx - 90)
                leftEyeBounds.append((newX,y))
            for (x,y) in rightEyeBounds:
                canvas.create_text(x, y, text = '·')
            for (x,y) in leftEyeBounds:
                canvas.create_text(x, y, text = '·')

        elif mode.blushSelection == True:
            for i in range(len(mode.blushColors)):
                canvas.create_rectangle(mode.width - 150, 125 + i * 50, mode.width - 100, 125 + (i+1) * 50, fill = mode.blushColorNames[i])
                canvas.create_text(mode.width - 125, 125 + (i + 0.5) * 50, text = f'{mode.blushColors[i]}', font = "Arial 15")
            rightBlushBounds = [(715, 321),(721, 313),(731, 310),(742, 310),(754, 313),(760, 320),(762, 333),(754, 344),
                                (741, 348),(726, 344),(715, 339),(711, 330)]
            leftBlushBounds = []
            for (x,y) in rightBlushBounds:
                newX = (mode.width - 30 - x) + (cx - 90)
                leftBlushBounds.append((newX,y))
            for (x,y) in rightBlushBounds:
                canvas.create_text(x, y, text = '·')
            for (x,y) in leftBlushBounds:
                canvas.create_text(x, y, text = '·')

        elif mode.lipstickSelection == True:
            for i in range(len(mode.lipstickColors)):
                canvas.create_rectangle(mode.width - 150, 250 + i * 50, mode.width - 100, 250 + (i+1) * 50, fill = mode.lipstickColorNames[i])
                canvas.create_text(mode.width - 125, 250 + (i + 0.5) * 50, text = f'{mode.lipstickColors[i]}', font = "Arial 15")
            rightLipstickBounds = [(690, 355),(694, 354),(698, 353),(701, 354),(706, 355),(711, 358),
                                (690, 370),(694, 369),(698, 368),(703, 367),(707, 364), (710, 362)]
            leftLipstickBounds = []
            for (x,y) in rightLipstickBounds:
                newX = (mode.width - 30 - x) + (cx - 90)
                leftLipstickBounds.append((newX,y))
            for (x,y) in rightLipstickBounds:
                canvas.create_text(x, y, text = '·')
            for (x,y) in leftLipstickBounds:
                canvas.create_text(x, y, text = '·')

    def drawing(mode, canvas):
        for (cx, cy, r, color) in mode.drawnDots[:-1]:
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color, outline = '')
        if mode.colorShow == True:
            cx = mode.penX
            cy = mode.penY
            r = mode.penR
            color = mode.selectedColor
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color)


    def redrawAll(mode, canvas):
        cx, cy = mode.width // 2, mode.height // 2

        #background
        canvas.create_image(cx, cy, image = ImageTk.PhotoImage(mode.background))

        if mode.customerScreen:
            GameMode.drawCustomerScreen(mode, canvas)
        elif mode.gameScreen:
            GameMode.drawGameScreen(mode,canvas)
            GameMode.drawColorOptions(mode, canvas)
            GameMode.drawing(mode, canvas)
            GameMode.timeIsUp(mode, canvas)
        
