from cmu_112_graphics import *
from tkinter import *
import random
import os

class StartMode(Mode):
    def appStarted(mode):
        parentDir = os.path.abspath("..")
        img_dir = os.path.join(parentDir, "termProject/images/splashBG.jpg")
        mode.background = mode.loadImage(img_dir)
        mode.time = 0
        mode.size = 0
        mode.showOptions = False
        mode.textCX = mode.width

    def mousePressed(mode, event):
        if mode.showOptions:
            pass

    def keyPressed(mode, event):
        if event.key == "h":
            mode.app.setActiveMode(mode.app.helpMode)

    def timerFired(mode):
        mode.time += mode.timerDelay
        if mode.textCX > mode.width//2:
            mode.size += 5
            mode.textCX -= 40

        if mode.showOptions == False and mode.time > 2000:
            mode.showOptions = True

    def redrawAll(mode, canvas):
        cx, cy = mode.width//2, mode.height//2
        #background
        canvas.create_image(cx, cy, image = ImageTk.PhotoImage(mode.background))

        if mode.showOptions == False:
            text = "  Welcome to the\nKC Beauty Studio"
            font = f"Arial {mode.size} bold"
            canvas.create_text(cx, cy - 100, text = text, fill = 'black', font = font)
        else:
            canvas.create_text(cx, 90, text = "Select an Opponent", font = "Arial 70 bold", fill = "black")
            canvas.create_rectangle(10, mode.height - 45, 180, mode.height - 10, fill = "white", outline = "")
            canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Press H for help!", font = "Arial 20", fill = "black")
