from cmu_112_graphics import *
from tkinter import *
import random
import os

class GameMode(Mode):
    def appStarted(mode):
        parentDir = os.path.abspath("..")
        img_dir = os.path.join(parentDir, "termProject/images/splashBG.jpg")
        mode.background = mode.loadImage(img_dir)
        customers = ["customer1.png", "customer2.png", "customer3.png","customer4.png","customer5.png","customer6.png"]
        customer = random.choice(customers)
        parentDir = os.path.abspath("..")
        img_dir = os.path.join(parentDir, f"termProject/images/customers/{customer}")
        mode.customer = mode.scaleImage(mode.loadImage(img_dir), 2/3)
        mode.customerScreen = True
        mode.gameScreen = False
        mode.scoringScreen = False

        mode.timeLeft = 61
        mode.timerCount = 0
        mode.timeEnd = False

        mode.colorPicker()
        mode.productImages()
    
    def productImages(mode):
        parentDir = os.path.abspath("..")
        img_dir = os.path.join(parentDir, "termProject/images/eyeshadow.png")
        mode.eyeshadow = mode.scaleImage(mode.loadImage(img_dir), 1/6)
        img_dir = os.path.join(parentDir, "termProject/images/blush.png")
        mode.blush = mode.scaleImage(mode.loadImage(img_dir), 1/5)
        img_dir = os.path.join(parentDir, "termProject/images/lipstick.png")
        mode.lipstick = mode.scaleImage(mode.loadImage(img_dir), 1/9)
        img_dir = os.path.join(parentDir, "termProject/images/erase.png")
        mode.erase = mode.scaleImage(mode.loadImage(img_dir), 1/5)


    def colorPicker(mode):
        eyeshadowColors = ["pink", "orange", "yellow", "green", "blue", "purple"]
        mode.eyeshadowColor = random.choice(eyeshadowColors)
        blushColors = ["pink", "red", "peach", "orange"]
        mode.blushColor = random.choice(blushColors)
        lipstickColors = ["pink", "red", "nude", "purple"]
        mode.lipstickColor = random.choice(lipstickColors)
    
    def mousePressed(mode, event):
        if mode.customerScreen:
            if (700 <= event.x <= 800) and (350 <= event.y < 400):
                mode.customerScreen = False
                mode.gameScreen = True

    def timerFired(mode):
        if mode.gameScreen:
            if mode.timerCount % 10 == 0: 
                if mode.timeLeft > 0:
                    mode.timeLeft -= 1
                else:
                    mode.timeEnd = True
            mode.timerCount += 1

        if mode.timeEnd:
            mode.scoringScreen = True

    def redrawAll(mode, canvas):
        cx, cy = mode.width // 2, mode.height // 2

        if mode.customerScreen:
            #background
            canvas.create_image(cx, cy, image = ImageTk.PhotoImage(mode.background))

            canvas.create_text(cx, 70, text = "A customer has arrived!", font = "Arial 50 bold", fill = "black")
            canvas.create_image(cx - 150, cy + 50, image = ImageTk.PhotoImage(mode.customer))
            canvas.create_oval(cx + 225 + 220, cy + 100, cx + 225 - 220, cy - 100, fill = "white", outline = "pink")
            canvas.create_text(cx + 225, cy, text = f"\"I would like \n{mode.eyeshadowColor} eyeshadow, \nwith {mode.blushColor} blush, \nand {mode.lipstickColor} lipstick.\"",
                                font = "Arial 30 bold")
            canvas.create_rectangle(cx + 175, mode.height - 125, cx + 275, mode.height - 75, fill = "pink", outline = "")
            canvas.create_text(cx + 225, mode.height - 100, text = "Go!", font = "Arial 30 bold", fill = "black")

        elif mode.gameScreen:
            canvas.create_rectangle(cx - 110, 0, cx + 110, 40, fill = "white", outline = "black")
            canvas.create_text(cx, 20, text=f'Time Remaining : {mode.timeLeft}', font="Arial 20 bold")

            #customer
            canvas.create_image(cx, cy + 50, image = ImageTk.PhotoImage(mode.customer))
            canvas.create_text(10, 10, text = f"Check List:\n- {mode.eyeshadowColor} eyeshadow\n- {mode.blushColor} blush\n- {mode.lipstickColor} lipstick",
                                font = "Arial 20", anchor = "nw")
            
            #makeup
            products = ["Eyeshadow", "Blush", "Lipstick", "Erase"]
            pictures = [mode.eyeshadow, mode.blush, mode.lipstick, mode.erase]
            for i in range(len(products)):
                boxHeight = mode.height // 4
                canvas.create_rectangle(mode.width - 100, i * boxHeight, mode.width, (i+1) * boxHeight, fill = "pink", outline = "black")
                canvas.create_image(mode.width - 50, (i + 0.5) * boxHeight, image = ImageTk.PhotoImage(pictures[i]))
                canvas.create_text(mode.width - 50, (i + 0.8) * boxHeight, text = f'{products[i]}', font = "Arial 15 bold")
        
        if mode.timeEnd:
            canvas.create_rectangle(cx - 200, cy - 100, cx + 200, cy + 100, fill = "gray", outline = "black")
            canvas.create_text(cx, cy, text="Time is Up!", font="Arial 50 bold")