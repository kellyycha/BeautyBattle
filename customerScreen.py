from cmu_112_graphics import *
from tkinter import *
import random
import os

class CustomerMode(Mode):
    def appStarted(mode):
        customers = ["customer1.png", "customer2.png", "customer3.png","customer4.png","customer5.png","customer6.png"]
        customer = random.choice(customers)
        parentDir = os.path.abspath("..")
        img_dir = os.path.join(parentDir, f"termProject/images/customers/{customer}")
        mode.customer = mode.scaleImage(mode.loadImage(img_dir), 2/3)
        mode.customerScreen = True
        mode.colorPicker()

    def colorPicker(mode):
        eyeshadowColors = ["pink", "orange", "yellow", "green", "blue", "purple"]
        mode.eyeshadowColor = random.choice(eyeshadowColors)
        blushColors = ["pink", "red", "peach", "orange"]
        mode.blushColor = random.choice(blushColors)
        lipstickColors = ["pink", "red", "nude", "purple"]
        mode.lipstickColor = random.choice(lipstickColors)
    
    def mousePressed(mode, event):
        if (700 <= event.x <= 800) and (350 <= event.y < 400):
            mode.app.setActiveMode(mode.app.gameMode)

    def redrawAll(mode, canvas):
        cx,cy = mode.width//2,mode.height//2
        if mode.customerScreen:
            canvas.create_text(cx, 70, text = "A customer has arrived!", font = "Arial 50 bold", fill = "black")
            canvas.create_image(cx - 100, cy + 50, image = ImageTk.PhotoImage(mode.customer))
            canvas.create_text(cx + 250, cy, text = f"\"I would like \n{mode.eyeshadowColor} eyeshadow, \nwith {mode.blushColor} blush, \nand {mode.lipstickColor} lipstick.\"",
                                font = "Arial 30 bold")
            canvas.create_rectangle(cx + 200, mode.height - 150, cx + 300, mode.height - 100, fill = "pink", outline = "")
            canvas.create_text(cx + 250, mode.height - 125, text = "Go!", font = "Arial 30 bold", fill = "black")