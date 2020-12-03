from cmu_112_graphics import *
from startMode import StartMode
from helpMode import HelpMode
from gameMode import GameMode

class MyModalApp(ModalApp):
    def appStarted(app):
        app.startMode = StartMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.startMode)
        app.timerDelay = 10

MyModalApp(width=1000, height=500)