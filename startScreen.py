from cmu_112_graphics import *
from tkinter import *
import os

class StartMode(Mode):
    def appStarted(mode):
        parentDir = os.path.abspath("..")
        img_dir = os.path.join(parentDir, "termProject/images/splashBG.jpg")
        mode.background = mode.loadImage(img_dir)

        mode.time = 0
        mode.size = 0
        mode.textCX = mode.width

        mode.opponentOptions()

    def opponentOptions(mode):
        mode.showOptions = False
        mode.easy = False
        mode.medium = False
        mode.hard = False
        mode.name = ""
        mode.challengeButton = False
        #images
        parentDir = os.path.abspath("..")
        img_dir = os.path.join(parentDir, "termProject/images/easyOpponent.png")
        mode.easyOpponent = mode.scaleImage(mode.loadImage(img_dir), 1/4)
        img_dir = os.path.join(parentDir, "termProject/images/mediumOpponent.png")
        mode.mediumOpponent = mode.scaleImage(mode.loadImage(img_dir), 1/4)
        img_dir = os.path.join(parentDir, "termProject/images/hardOpponent.png")
        mode.hardOpponent = mode.scaleImage(mode.loadImage(img_dir), 1/4)

    def mousePressed(mode, event):
        #print(f'mousePressed at {(event.x, event.y)}')
        if mode.showOptions:
            if mode.challengeButton == True and (320 <= event.x <= 680) and (440 <= event.y < 480):
                mode.app.setActiveMode(mode.app.gameMode)
 
            if (270 <= event.x <= 330) and (190 <= event.y < 420):
                mode.easy = True
                mode.name = "Amateur"
                mode.medium = False
                mode.hard = False
                mode.challengeButton = True
                
            elif (470 <= event.x <= 530) and (190 <= event.y < 420):
                mode.easy = False
                mode.medium = True
                mode.name = "Professional"
                mode.hard = False
                mode.challengeButton = True

            elif (660 <= event.x <= 710) and (190 <= event.y < 420):
                mode.easy = False
                mode.medium = False
                mode.hard = True
                mode.name = "Expert"
                mode.challengeButton = True

            else:
                mode.easy = False
                mode.medium = False
                mode.hard = False
                mode.challengeButton = False

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
            canvas.create_text(cx, cy, text = text, fill = 'black', font = font)
        else:
            #title
            canvas.create_text(cx, 70, text = "Select an Opponent", font = "Arial 50 bold", fill = "black")
            
            #show options
            canvas.create_image(cx - 200, cy + 50, image = ImageTk.PhotoImage(mode.easyOpponent))
            canvas.create_text(cx - 200, 150, text = "Amateur", fill = "black", font = "Arial 20 bold")
            canvas.create_image(cx, cy + 50, image = ImageTk.PhotoImage(mode.mediumOpponent))
            canvas.create_text(cx, 150, text = "Professional", fill = "black", font = "Arial 20 bold")
            canvas.create_image(cx + 200, cy + 50, image = ImageTk.PhotoImage(mode.hardOpponent))
            canvas.create_text(cx + 200, 150, text = "Expert", fill = "black", font = "Arial 20 bold")
           
            #show challenge button after selection
            if mode.challengeButton:
                canvas.create_rectangle(cx - 180, mode.height - 60, cx + 180, mode.height - 20, fill = "pink", outline = "")
                canvas.create_text(cx, mode.height - 40, text = f"Challenge {mode.name}", font = "Arial 30 bold", fill = "black")

            if mode.challengeButton == False:
                canvas.create_rectangle(cx - 180, mode.height - 60, cx + 180, mode.height - 20, fill = "pink", outline = "")
                canvas.create_text(cx, mode.height - 40, text = "No Selection Made", font = "Arial 30 bold", fill = "black")
