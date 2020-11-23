from cmu_112_graphics import *
import random
from startScreen import StartMode
from gameMode import GameMode


class HelpMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 150, text='This is the help screen!', font=font)
        canvas.create_text(mode.width/2, 250, text='(Insert helpful message here)', font=font)
        canvas.create_text(mode.width/2, 350, text='Press any key to return to the home page!', font=font)

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.startMode)

class MyModalApp(ModalApp):
    def appStarted(app):
        app.startMode = StartMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.startMode)
        app.timerDelay = 50
        

MyModalApp(width=1000, height=500)