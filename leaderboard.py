from cmu_112_graphics import *
from tkinter import *
from gameMode import GameMode
import os
from loginScreen import LoginScreen

class Leaderboard(Mode):
    def appStarted(mode):
        mode.cx, mode.cy = mode.width // 2, mode.height // 2
        mode.background = mode.loadImage("images/background.jpg")
        #if new user (no previous data)
        if os.path.isfile(f'data/{"".join(LoginScreen.username)}.txt'):
            mode.hasData = True
        if not os.path.isfile(f'data/{"".join(LoginScreen.username)}.txt'):
            mode.hasData = False
    
    def mousePressed(mode, event):
        if (10 <= event.x <= 110) and (mode.height - 45 <= event.y <= mode.height - 10):
            if GameMode.fromGame:
                mode.app.setActiveMode(mode.app.gameMode)
            else:
                GameMode.selection = None
                mode.app.setActiveMode(mode.app.startMode)

        if GameMode.selection == None:
            if (mode.width//4 - 100 <= event.x <= mode.width//4 + 100) and (mode.cy <= event.y <= mode.cy + 60):
                GameMode.selection = 'Amateur'
            if (mode.cx - 100 <= event.x <= mode.cx + 100) and (mode.cy <= event.y <= mode.cy + 60):
                GameMode.selection = 'Professional'
            if (mode.width//4 + mode.cx - 100 <= event.x <= mode.width//4 + mode.cx + 100) and (mode.cy <= event.y <= mode.cy + 60):
                GameMode.selection = 'Expert'
        
        if GameMode.selection != None:
            if (mode.cx - 100 <= event.x <= mode.cx + 100) and (mode.height - 45 <= event.y <= mode.height - 10):
               GameMode.selection = None 

    def easyLeaderboard(mode, canvas):
        pass

    def mediumLeaderboard(mode, canvas):
        pass

    def hardLeaderboard(mode, canvas):
        pass

    def easyProgress(mode, canvas):
        pass

    def mediumProgress(mode, canvas):
        pass

    def hardProgress(mode, canvas):
        pass

    def noProgress(mode, canvas):
        canvas.create_text(mode.cx + mode.cx//2, mode.cy, text = 'No Data Available')

    def otherOptionsButton(mode, canvas):
        canvas.create_rectangle(mode.cx - 100, mode.height - 45, mode.cx + 100, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(mode.cx, mode.height - 15, anchor = 's', text = "See Other levels", font = "Arial 20 bold", fill = "black")
    
    def redrawAll(mode, canvas):
        #background
        canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.background))
        
        #go back
        canvas.create_rectangle(10, mode.height - 45, 110, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Go Back", font = "Arial 20 bold", fill = "black")


        if GameMode.selection == None:
            canvas.create_text(mode.cx, 100, text = "Leaderboards & Progress", font = "Silom 50 bold", fill = "black")
            canvas.create_text(mode.cx, 190, text = "Choose a level to view", font = "Silom 40 bold", fill = "black")

            canvas.create_rectangle(mode.width//4 - 100, mode.cy, mode.width//4 + 100, mode.cy + 60, fill = 'pink', outline = '')
            canvas.create_text(mode.width//4, mode.cy + 30, text = "Amateur", font = "Silom 30", fill = "black")

            canvas.create_rectangle(mode.cx - 100, mode.cy, mode.cx + 100, mode.cy + 60, fill = 'pink', outline = '')
            canvas.create_text(mode.cx, mode.cy + 30, text = "Professional", font = "Silom 27", fill = "black")

            canvas.create_rectangle(mode.width//4 + mode.cx - 100, mode.cy, mode.width//4 + mode.cx + 100, mode.cy + 60, fill = 'pink', outline = '')
            canvas.create_text(mode.width//4 + mode.cx, mode.cy + 30, text = "Expert", font = "Silom 30", fill = "black")
            #print('none')
        
        if GameMode.selection != None:
            canvas.create_text(mode.cx, 80, text = f"{GameMode.selection} Leaderboard & Progress", font = "Silom 40 bold", fill = "black")
            canvas.create_line(mode.cx, 110, mode.cx, mode.height, fill = "black", width = 4)
            Leaderboard.otherOptionsButton(mode, canvas)
            canvas.create_text(mode.cx//2, 130, text = "HIGH SCORES", font = "Silom 30", fill = "black")
            canvas.create_text(mode.cx + mode.cx//2, 130, text = "YOUR PROGRESS", font = "Silom 30", fill = "black")

            if mode.hasData == False:
                Leaderboard.noProgress(mode, canvas)
        
        if GameMode.selection == 'Amateur':
            Leaderboard.easyLeaderboard(mode, canvas)
            if mode.hasData:
                Leaderboard.easyProgress(mode, canvas)
            #print('ama')
        
        if GameMode.selection == 'Professional':
            Leaderboard.mediumLeaderboard(mode, canvas)
            if mode.hasData:
                Leaderboard.mediumProgress(mode, canvas)
            #print('pro')
        
        if GameMode.selection == 'Expert':
            Leaderboard.hardLeaderboard(mode, canvas)
            if mode.hasData:
                Leaderboard.hardProgress(mode, canvas)
            #print('exp')

        


