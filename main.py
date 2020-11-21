from cmu_112_graphics import *
import random

class SplashScreenMode(Mode):
    def appStarted(mode):
        mode.splashBG = mode.loadImage('images/splashBG.jpg')
        
    def redrawAll(mode, canvas):
        canvas.create_image(mode.width/2, mode.height/2, image = ImageTk.PhotoImage(mode.splashBG))
        canvas.create_text(mode.width/2, 150, text='Welcome to the KC Beauty Studio!', font='Arial 26 bold')
        canvas.create_text(mode.width/2, 250, text='Click to Begin', font='Arial 26 bold')

    def mousePressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)

class GameMode(Mode):
    def keyPressed(mode, event):
        if (event.key == 'h'):
            mode.app.setActiveMode(mode.app.helpMode)

class HelpMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 150, text='This is the help screen!', font=font)
        canvas.create_text(mode.width/2, 250, text='(Insert helpful message here)', font=font)
        canvas.create_text(mode.width/2, 350, text='Press any key to return to the game!', font=font)

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)

class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=1000, height=500)