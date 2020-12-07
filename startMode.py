from cmu_112_graphics import *
from tkinter import *
from loginScreen import LoginScreen

class StartMode(Mode):
    name = ""
    easy = False
    medium = False
    hard = False

    login = False

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
        mode.challengeButton = False
        # Amateur image: https://graphicmama.com/cartoon-character/cute-office-girl-cartoon-vector-character 
        mode.amateur = mode.scaleImage(mode.loadImage("images/amateur.png"), 1/4)
        # Professional image: https://graphicmama.com/cartoon-character/pretty-girl-with-long-hair-cartoon-vector-character 
        mode.professional = mode.scaleImage(mode.loadImage("images/professional.png"), 1/4)
        # Expert image: https://graphicmama.com/cartoon-character/cartoon-elegant-woman-vector-character 
        mode.expert = mode.scaleImage(mode.loadImage("images/expert.png"), 1/4)

    #from 15112 PIL Notes
    def getCachedPhotoImage(mode, image):
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

    def mousePressed(mode, event):
        if StartMode.login == True:
            if mode.challengeButton == True and (320 <= event.x <= 680) and (440 <= event.y < 480): #clicks challenge button
                mode.app.setActiveMode(mode.app.gameMode)

            #clicks leaderboard
            if (10 <= event.x <= 210) and (mode.height - 45 <= event.y <= mode.height - 10):
                mode.app.setActiveMode(mode.app.leaderboard)

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

        #automatically shows the login screen after 3 seconds
        if StartMode.login == False and mode.time > 3000:
            StartMode.login = True
            mode.app.setActiveMode(mode.app.loginScreen)

    def redrawAll(mode, canvas):
        #background
        bg = StartMode.getCachedPhotoImage(mode, mode.background)
        canvas.create_image(mode.cx, mode.cy, image = bg)

        #title text
        if StartMode.login == False:
            text = "Beauty\n    Battle"
            canvas.create_text(mode.cx, mode.cy, text = text, fill = 'pink', font = f"Silom {mode.size+2} bold")
            canvas.create_text(mode.cx, mode.cy, text = text, fill = 'black', font = f"Silom {mode.size} bold")
        
        else:
            canvas.create_text(mode.cx, 70, text = "Select an Opponent", font = "Silom 50 bold", fill = "black")
            #show options
            amateur = StartMode.getCachedPhotoImage(mode, mode.amateur)
            canvas.create_image(mode.cx - 200, mode.cy + 50, image = amateur)
            canvas.create_text(mode.cx - 200, 150, text = "Amateur", fill = "black", font = "Silom 20 bold")
            pro = StartMode.getCachedPhotoImage(mode, mode.professional)
            canvas.create_image(mode.cx, mode.cy + 50, image = pro)
            canvas.create_text(mode.cx, 150, text = "Professional", fill = "black", font = "Silom 20 bold")
            expert = StartMode.getCachedPhotoImage(mode, mode.expert)
            canvas.create_image(mode.cx + 200, mode.cy + 50, image = expert)
            canvas.create_text(mode.cx + 200, 150, text = "Expert", fill = "black", font = "Silom 20 bold")

            #show leaderboard option
            canvas.create_rectangle(10, mode.height - 45, 210, mode.height - 10, fill = "white", outline = "")
            canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Show Leaderboard", font = "Arial 20 bold", fill = "black")

            #show challenge button after selection
            if mode.challengeButton:
                canvas.create_rectangle(mode.cx - 180, mode.height - 60, mode.cx + 180, mode.height - 20, fill = "pink", outline = "")
                if StartMode.name == "Professional":
                    canvas.create_text(mode.cx, mode.height - 40, text = f"Challenge {StartMode.name}", font = "Silom 25 bold", fill = "black")
                else:
                    canvas.create_text(mode.cx, mode.height - 40, text = f"Challenge {StartMode.name}", font = "Silom 30 bold", fill = "black")