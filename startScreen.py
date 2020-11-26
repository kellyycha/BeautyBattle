from cmu_112_graphics import *
from tkinter import *
import os

name = "NOT CORRECT"

class StartMode(Mode):
    def appStarted(mode):
        parentDir = os.path.abspath("..")
        # Background image: https://cdn4.vectorstock.com/i/1000x1000/85/23/beauty-background-with-icons-cosmetics-vector-1998523.jpg 
        img_dir = os.path.join(parentDir, "termProject/images/background.jpg")
        mode.background = mode.loadImage(img_dir)
        mode.cx, mode.cy = mode.width // 2, mode.height // 2

        mode.time = 0
        mode.size = 0
        mode.textcx = mode.width

        mode.opponentOptions()

    def opponentOptions(mode):
        mode.showOptions = False
        mode.easy = False
        mode.medium = False
        mode.hard = False
        mode.challengeButton = False
        #images
        parentDir = os.path.abspath("..")
        # Amateur image: https://graphicmama.com/cartoon-character/cute-office-girl-cartoon-vector-character 
        img_dir = os.path.join(parentDir, "termProject/images/amateur.png")
        mode.amateur = mode.scaleImage(mode.loadImage(img_dir), 1/4)
        # Professional image: https://graphicmama.com/cartoon-character/pretty-girl-with-long-hair-cartoon-vector-character 
        img_dir = os.path.join(parentDir, "termProject/images/professional.png")
        mode.professional = mode.scaleImage(mode.loadImage(img_dir), 1/4)
        # Expert image: https://graphicmama.com/cartoon-character/cartoon-elegant-woman-vector-character 
        img_dir = os.path.join(parentDir, "termProject/images/expert.png")
        mode.expert = mode.scaleImage(mode.loadImage(img_dir), 1/4)

    def mousePressed(mode, event):
        global name
        if mode.showOptions:
            if mode.challengeButton == True and (320 <= event.x <= 680) and (440 <= event.y < 480):
                mode.app.setActiveMode(mode.app.gameMode)
                #GameMode.appStarted(mode) <-- restart when called
 
            if (270 <= event.x <= 330) and (190 <= event.y < 420):
                mode.easy = True
                name = "Amateur"
                mode.medium = False
                mode.hard = False
                mode.challengeButton = True
                
            elif (470 <= event.x <= 530) and (190 <= event.y < 420):
                mode.easy = False
                mode.medium = True
                name = "Professional"
                mode.hard = False
                mode.challengeButton = True

            elif (660 <= event.x <= 710) and (190 <= event.y < 420):
                mode.easy = False
                mode.medium = False
                mode.hard = True
                name = "Expert"
                mode.challengeButton = True

            else:
                mode.easy = False
                mode.medium = False
                mode.hard = False
                mode.challengeButton = False

    def timerFired(mode):
        mode.time += mode.timerDelay
        if mode.textcx > mode.width//2:
            mode.size += 5
            mode.textcx -= 40

        if mode.showOptions == False and mode.time > 2000:
            mode.showOptions = True

    def redrawAll(mode, canvas):
        #background
        canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.background))

        if mode.showOptions == False:
            text = "  Welcome to the\nKC Beauty Studio"
            font = f"Arial {mode.size} bold"
            canvas.create_text(mode.cx, mode.cy, text = text, fill = 'black', font = font)
        else:
            #title
            canvas.create_text(mode.cx, 70, text = "Select an Opponent", font = "Arial 50 bold", fill = "black")
            
            #show options
            canvas.create_image(mode.cx - 200, mode.cy + 50, image = ImageTk.PhotoImage(mode.amateur))
            canvas.create_text(mode.cx - 200, 150, text = "Amateur", fill = "black", font = "Arial 20 bold")
            canvas.create_image(mode.cx, mode.cy + 50, image = ImageTk.PhotoImage(mode.professional))
            canvas.create_text(mode.cx, 150, text = "Professional", fill = "black", font = "Arial 20 bold")
            canvas.create_image(mode.cx + 200, mode.cy + 50, image = ImageTk.PhotoImage(mode.expert))
            canvas.create_text(mode.cx + 200, 150, text = "Expert", fill = "black", font = "Arial 20 bold")
           
            #show challenge button after selection
            if mode.challengeButton:
                canvas.create_rectangle(mode.cx - 180, mode.height - 60, mode.cx + 180, mode.height - 20, fill = "pink", outline = "")
                canvas.create_text(mode.cx, mode.height - 40, text = f"Challenge {name}", font = "Arial 30 bold", fill = "black")

            if mode.challengeButton == False:
                canvas.create_rectangle(mode.cx - 180, mode.height - 60, mode.cx + 180, mode.height - 20, fill = "pink", outline = "")
                canvas.create_text(mode.cx, mode.height - 40, text = "No Selection Made", font = "Arial 30 bold", fill = "black")

