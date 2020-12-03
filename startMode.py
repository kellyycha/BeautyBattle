from cmu_112_graphics import *
from tkinter import *

class StartMode(Mode):
    #class attributes to carry over different AIs
    name = ""
    easy = False
    medium = False
    hard = False

    def appStarted(mode):
        mode.cx, mode.cy = mode.width // 2, mode.height // 2
        # Background image: https://cdn4.vectorstock.com/i/1000x1000/85/23/beauty-background-with-icons-cosmetics-vector-1998523.jpg 
        mode.background = mode.loadImage("images/background.jpg")
        
        #to zoom in the title screen
        mode.time = 0
        mode.size = 15
        mode.textcx = mode.width

        mode.opponentOptions()

    def opponentOptions(mode):
        mode.showOptions = False
        mode.challengeButton = False
        # Amateur image: https://graphicmama.com/cartoon-character/cute-office-girl-cartoon-vector-character 
        mode.amateur = mode.scaleImage(mode.loadImage("images/amateur.png"), 1/4)
        # Professional image: https://graphicmama.com/cartoon-character/pretty-girl-with-long-hair-cartoon-vector-character 
        mode.professional = mode.scaleImage(mode.loadImage("images/professional.png"), 1/4)
        # Expert image: https://graphicmama.com/cartoon-character/cartoon-elegant-woman-vector-character 
        mode.expert = mode.scaleImage(mode.loadImage("images/expert.png"), 1/4)

    def mousePressed(mode, event):
        if mode.showOptions:
            if mode.challengeButton == True and (320 <= event.x <= 680) and (440 <= event.y < 480): #clicks challenge button
                mode.app.setActiveMode(mode.app.gameMode)

            #clicks Amateur
            if (270 <= event.x <= 330) and (190 <= event.y < 420):
                StartMode.easy = True
                StartMode.name = "Amateur"
                StartMode.medium = False
                StartMode.hard = False
                mode.challengeButton = True

            #clicks Professional 
            elif (470 <= event.x <= 530) and (190 <= event.y < 420):
                StartMode.easy = False
                StartMode.medium = True
                StartMode.name = "Professional"
                StartMode.hard = False
                mode.challengeButton = True

            #clicks Expert
            elif (660 <= event.x <= 710) and (190 <= event.y < 420):
                StartMode.easy = False
                StartMode.medium = False
                StartMode.hard = True
                StartMode.name = "Expert"
                mode.challengeButton = True

            #clicks outside of the three options
            else:
                mode.challengeButton = False

    def timerFired(mode):
        #increases size of title text
        mode.time += mode.timerDelay
        if mode.textcx > mode.width//2:
            mode.size += 4
            mode.textcx -= 30

        #automatically shows the options screen after 3 seconds
        if mode.showOptions == False and mode.time > 3000:
            mode.showOptions = True

    def redrawAll(mode, canvas):
        #background
        canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.background))

        #title text
        if mode.showOptions == False:
            text = "  Welcome to the\nKC Beauty Studio"
            font = f"Arial {mode.size} bold"
            canvas.create_text(mode.cx, mode.cy, text = text, fill = 'black', font = font)
        
        else:
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
                canvas.create_text(mode.cx, mode.height - 40, text = f"Challenge {StartMode.name}", font = "Arial 30 bold", fill = "black")