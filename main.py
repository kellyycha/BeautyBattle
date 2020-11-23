from cmu_112_graphics import *
from startScreen import StartMode
from helpMode import HelpMode
from gameMode import GameMode

class MyModalApp(ModalApp):
    def appStarted(app):
        app.startMode = StartMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.startMode)
        app.timerDelay = 50

MyModalApp(width=1000, height=500)