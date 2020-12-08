from cmu_112_graphics import *
from startMode import StartMode
from helpMode import HelpMode
from gameMode import GameMode
from leaderboard import Leaderboard
from loginScreen import LoginScreen

class MyModalApp(ModalApp):
    def appStarted(app):
        app.startMode = StartMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.leaderboard = Leaderboard()
        app.loginScreen = LoginScreen()
        app.setActiveMode(app.startMode)
        app.timerDelay = 10
        
MyModalApp(width=1000, height=500)