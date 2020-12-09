from cmu_112_graphics import *
from tkinter import *
from loginScreen import LoginScreen
import pygame

class StartMode(Mode):
    name = ""
    easy = False
    medium = False
    hard = False

    login = False
    selection = None

    timeDuration = 60

    def appStarted(mode):
        mode.cx, mode.cy = mode.width // 2, mode.height // 2
        # Background image: https://cdn4.vectorstock.com/i/1000x1000/85/23/beauty-background-with-icons-cosmetics-vector-1998523.jpg 
        mode.background = mode.loadImage("images/background.jpg")

        #to zoom in the title screen
        mode.time = 0
        mode.size = 25

        mode.fill = 'white'
        StartMode.timeDuration = 60
        mode.changeDurationPressed = False

        StartMode.opponentOptions(mode)
        StartMode.music()

    def music():
        #Music by Gil Wanders - Dreams - https://thmatc.co/?l=02A22A1F
        if StartMode.login == False:
            pygame.mixer.init()
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play(-1)

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
            #clicks challenge button
            if mode.challengeButton == True and (320 <= event.x <= 680) and (440 <= event.y < 480): 
                StartMode.selection = StartMode.name
                mode.app.gameMode.setTime()
                mode.app.setActiveMode(mode.app.gameMode)
            
            #clicks change duration
            if ((mode.width - 100) - 90 <= event.x <= (mode.width - 100) + 90) and (70 - 20 <= event.y <= 70 + 20):
                mode.changeDurationPressed = not mode.changeDurationPressed
            
            if mode.changeDurationPressed:
                if ((mode.width - 100) - 30 <= event.x <= (mode.width - 100) + 30):
                    if (100 + 0*50 <= event.y <= 150 + 0*50):
                        StartMode.timeDuration = 30 
                    elif (100 + 1*50 <= event.y <= 150 + 1*50):
                        StartMode.timeDuration = 60
                    elif (100 + 2*50 <= event.y <= 150 + 2*50):
                        StartMode.timeDuration = 90
                        
            #clicks leaderboard
            if (10 <= event.x <= 210) and (mode.height - 45 <= event.y <= mode.height - 10):
                #mode.app.leaderboard.appStarted()
                mode.app.setActiveMode(mode.app.leaderboard)

            #logs out
            if (mode.width - 110 <= event.x <= mode.width - 10) and (mode.height - 45 <= event.y <= mode.height - 10):
                StartMode.login = False
                mode.app.startMode.appStarted()
                mode.app.loginScreen.appStarted()
                mode.app.setActiveMode(mode.app.startMode)

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
        mode.time += 1
        if mode.size < 100:
            mode.size += 5

        #automatically shows the login screen after 2 seconds
        if StartMode.login == False and mode.time > 20:
            StartMode.login = True
            mode.app.setActiveMode(mode.app.loginScreen)
        

    def drawTimeSelection(mode, canvas):
        if mode.changeDurationPressed:
            mode.fill = 'pink'
        else:
            mode.fill = 'white'
        canvas.create_rectangle((mode.width - 100) - 90, 70 - 20, (mode.width - 100) + 90, 70 + 20, fill = mode.fill, outline = '')
        canvas.create_text((mode.width - 100), 70, text = "Change Duration", font = "Chicago 18", fill = 'black')
        if mode.changeDurationPressed:
            for i in range(3):
                canvas.create_rectangle((mode.width - 100) - 30, 100 + i*50, (mode.width - 100) + 30, 150 + i*50, fill = 'white', outline = 'pink')
                canvas.create_text((mode.width - 100), 125 + i*50, text = f"{(i+1)*3}0s", font = "Chicago 20", fill = 'black')
                if StartMode.timeDuration == 30:
                    canvas.create_text((mode.width - 100), 125 + 0*50, text = f"30s", font = "Chicago 20", fill = 'DeepPink2')
                elif StartMode.timeDuration == 60:
                    canvas.create_text((mode.width - 100), 125 + 1*50, text = f"60s", font = "Chicago 20", fill = 'DeepPink2')
                elif StartMode.timeDuration == 90:
                    canvas.create_text((mode.width - 100), 125 + 2*50, text = f"90s", font = "Chicago 20", fill = 'DeepPink2')        

    def drawButtons(mode, canvas):
        #show leaderboard option
        canvas.create_rectangle(10, mode.height - 45, 210, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Show Leaderboard", font = "Arial 20 bold", fill = "black")

        #log out
        canvas.create_rectangle(mode.width - 110, mode.height - 45, mode.width - 10, mode.height - 10, fill = "white", outline = "powder blue")
        canvas.create_text(mode.width - 20, mode.height - 15, anchor = 'se', text = "Log Out", font = "Arial 20 bold", fill = "black")
        
        #show challenge button after selection
        if mode.challengeButton:
            canvas.create_rectangle(mode.cx - 180, mode.height - 60, mode.cx + 180, mode.height - 20, fill = "pink", outline = "")
            if StartMode.name == "Professional":
                canvas.create_text(mode.cx, mode.height - 40, text = f"Challenge {StartMode.name}", font = "Chicago 25", fill = "black")
            else:
                canvas.create_text(mode.cx, mode.height - 40, text = f"Challenge {StartMode.name}", font = "Chicago 30", fill = "black")

    def showOptions(mode, canvas):
        #show options
        amateur = StartMode.getCachedPhotoImage(mode, mode.amateur)
        canvas.create_image(mode.cx - 200, mode.cy + 50, image = amateur)
        canvas.create_text(mode.cx - 200, 150, text = "Amateur", fill = "black", font = "Chicago 20")
        pro = StartMode.getCachedPhotoImage(mode, mode.professional)
        canvas.create_image(mode.cx, mode.cy + 50, image = pro)
        canvas.create_text(mode.cx, 150, text = "Professional", fill = "black", font = "Chicago 20")
        expert = StartMode.getCachedPhotoImage(mode, mode.expert)
        canvas.create_image(mode.cx + 200, mode.cy + 50, image = expert)
        canvas.create_text(mode.cx + 200, 150, text = "Expert", fill = "black", font = "Chicago 20")

    def redrawAll(mode, canvas):
        #background
        bg = StartMode.getCachedPhotoImage(mode, mode.background)
        canvas.create_image(mode.cx, mode.cy, image = bg)

        #title text
        if StartMode.login == False:
            text = "Beauty\n    Battle"
            canvas.create_text(mode.cx, mode.cy, text = text, fill = 'pink', font = f"Chicago {mode.size+2}")
            canvas.create_text(mode.cx, mode.cy, text = text, fill = 'black', font = f"Chicago {mode.size}")
        
        else:
            canvas.create_text(mode.cx, 70, text = "Select an Opponent", font = "Chicago 50", fill = "black")
              
            StartMode.showOptions(mode, canvas)
            StartMode.drawButtons(mode, canvas)
            StartMode.drawTimeSelection(mode, canvas)
            