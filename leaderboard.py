from cmu_112_graphics import *
from tkinter import *
from gameMode import GameMode
from loginScreen import LoginScreen
from startMode import StartMode
import sqlite3
import string

class Leaderboard(Mode):
    def appStarted(mode):
        mode.cx, mode.cy = mode.width // 2, mode.height // 2
        mode.background = mode.loadImage("images/background.jpg")
        mode.ordered = ''
        mode.opponent = ''

    def mousePressed(mode, event):
        print(f'{(event.x,event.y)},')
        if (10 <= event.x <= 110) and (mode.height - 45 <= event.y <= mode.height - 10):
            if GameMode.fromGame:
                mode.app.setActiveMode(mode.app.gameMode)
            else:
                mode.app.setActiveMode(mode.app.startMode)

        if GameMode.showAmateur == False and GameMode.showProfessional == False and GameMode.showExpert == False:
            if (mode.width//4 - 100 <= event.x <= mode.width//4 + 100) and (mode.cy <= event.y <= mode.cy + 60):
                GameMode.showAmateur = True
                GameMode.showProfessional = False
                GameMode.showExpert = False
            if (mode.cx - 100 <= event.x <= mode.cx + 100) and (mode.cy <= event.y <= mode.cy + 60):
                GameMode.showAmateur = False
                GameMode.showProfessional = True
                GameMode.showExpert = False
            if (mode.width//4 + mode.cx - 100 <= event.x <= mode.width//4 + mode.cx + 100) and (mode.cy <= event.y <= mode.cy + 60):
                GameMode.showAmateur = False
                GameMode.showProfessional = False
                GameMode.showExpert = True
        
        if GameMode.showAmateur == True or GameMode.showProfessional == True or GameMode.showExpert == True:
            if (mode.cx - 100 <= event.x <= mode.cx + 100) and (mode.height - 45 <= event.y <= mode.height - 10):
                GameMode.showAmateur = False
                GameMode.showProfessional = False
                GameMode.showExpert = False
    
    def displayData(mode, canvas):
        i = 0
        num = 1
        for row in mode.ordered:
            if row == GameMode.yourData:
                color = 'DeepPink2'
            else:
                color = 'black'
            if i <= 204:
                canvas.create_text(mode.cx//2 - 100, mode.cy - 50 + i, text = f"{num}. {row[0]}", anchor = 'w', font = "Arial 25", fill = color)
                canvas.create_text(mode.cx//2 + 100, mode.cy - 50 + i, text = row[1], anchor = 'e', font = "Arial 25 bold", fill = color)
                i += 51
                num += 1

    def drawLeaderboard(mode, canvas):
        boxHeight = ((mode.cy + 180) - (mode.cy - 80))/ 5
        for i in range(5):
            canvas.create_rectangle(mode.cx//2 - 120, (mode.cy - 80) + i * boxHeight, mode.cx//2 + 120, (mode.cy - 80) + (i+1) * boxHeight, fill = "pink", outline = "black")
        canvas.create_line(290,170,290,430, fill = 'black')

        if GameMode.showAmateur:
            conn = sqlite3.connect('data/easyLeaderboard.db')
            cursor = conn.cursor()
            mode.ordered = cursor.execute("SELECT * FROM easyLeaderboard ORDER BY Score DESC")
            Leaderboard.displayData(mode, canvas)
            conn.close()
        
        if GameMode.showProfessional:
            conn = sqlite3.connect('data/mediumLeaderboard.db')
            cursor = conn.cursor()
            mode.ordered = cursor.execute("SELECT * FROM mediumLeaderboard ORDER BY Score DESC")
            Leaderboard.displayData(mode, canvas)
            conn.close()

        if GameMode.showExpert:
            conn = sqlite3.connect('data/hardLeaderboard.db')
            cursor = conn.cursor()
            mode.ordered = cursor.execute("SELECT * FROM hardLeaderboard ORDER BY Score DESC")
            Leaderboard.displayData(mode, canvas)
            conn.close()

    def drawGraph(mode, canvas):
        boxHeight = ((mode.cy + 180) - (mode.cy - 80))/ 5
        for i in range(5):
            canvas.create_rectangle(mode.cx//2 + mode.cx - 120, (mode.cy - 80) + i * boxHeight, mode.cx//2  + mode.cx + 120, (mode.cy - 80) + (i+1) * boxHeight, fill = "pink", outline = "black")
        canvas.create_line(290 + mode.cx,170,290 + mode.cx,430, fill = 'black')

        if GameMode.showAmateur == True:
            i = 0
            for row in GameMode.easyProgress:
                if i <= 204:
                    canvas.create_text(mode.cx//2 + mode.cx - 100, mode.cy - 50 + i, text = row[2][:11], anchor = 'w', font = "Arial 25")
                    canvas.create_text(mode.cx//2 + mode.cx + 100, mode.cy - 50 + i, text = row[1], anchor = 'e', font = "Arial 25 bold")
                    i += 51
        
        if GameMode.showProfessional == True:
            i = 0
            for row in GameMode.mediumProgress:
                if i <= 204:
                    canvas.create_text(mode.cx//2 + mode.cx - 100, mode.cy - 50 + i, text = row[2][:11], anchor = 'w', font = "Arial 25")
                    canvas.create_text(mode.cx//2 + mode.cx + 100, mode.cy - 50 + i, text = row[1], anchor = 'e', font = "Arial 25 bold")
                    i += 51

        if GameMode.showExpert == True:
            i = 0
            for row in GameMode.hardProgress:
                if i <= 204:
                    canvas.create_text(mode.cx//2 + mode.cx - 100, mode.cy - 50 + i, text = row[2][:11], anchor = 'w', font = "Arial 25")
                    canvas.create_text(mode.cx//2 + mode.cx + 100, mode.cy - 50 + i, text = row[1], anchor = 'e', font = "Arial 25 bold")
                    i += 51

    def otherOptionsButton(mode, canvas):
        canvas.create_rectangle(mode.cx - 100, mode.height - 45, mode.cx + 100, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(mode.cx, mode.height - 15, anchor = 's', text = "See Other levels", font = "Arial 20 bold", fill = "black")
    
    def redrawAll(mode, canvas):
        #background
        canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.background))
        
        #go back
        canvas.create_rectangle(10, mode.height - 45, 110, mode.height - 10, fill = "white", outline = "")
        canvas.create_text(20, mode.height - 15, anchor = 'sw', text = "Go Back", font = "Arial 20 bold", fill = "black")

        if GameMode.showAmateur == False and GameMode.showProfessional == False and GameMode.showExpert == False:
            canvas.create_text(mode.cx, 100, text = "Leaderboards & Progress", font = "Silom 50 bold", fill = "black")
            canvas.create_text(mode.cx, 190, text = "Choose a level to view", font = "Silom 40 bold", fill = "black")

            canvas.create_rectangle(mode.width//4 - 100, mode.cy, mode.width//4 + 100, mode.cy + 60, fill = 'pink', outline = '')
            canvas.create_text(mode.width//4, mode.cy + 30, text = "Amateur", font = "Silom 30", fill = "black")

            canvas.create_rectangle(mode.cx - 100, mode.cy, mode.cx + 100, mode.cy + 60, fill = 'pink', outline = '')
            canvas.create_text(mode.cx, mode.cy + 30, text = "Professional", font = "Silom 27", fill = "black")

            canvas.create_rectangle(mode.width//4 + mode.cx - 100, mode.cy, mode.width//4 + mode.cx + 100, mode.cy + 60, fill = 'pink', outline = '')
            canvas.create_text(mode.width//4 + mode.cx, mode.cy + 30, text = "Expert", font = "Silom 30", fill = "black")
            #print('none')
        
        else:
            if GameMode.showAmateur == True:
                mode.opponent = 'Amateur'
            elif GameMode.showProfessional == True:
                mode.opponent = 'Professional'
            elif GameMode.showExpert == True:
                mode.opponent = 'Expert'
            
            canvas.create_text(mode.cx, 80, text = f"{mode.opponent} Leaderboard & Progress", font = "Silom 40 bold", fill = "black")
            canvas.create_line(mode.cx, 110, mode.cx, mode.height, fill = "black", width = 4)
            Leaderboard.otherOptionsButton(mode, canvas)
            canvas.create_text(mode.cx//2, 130, text = "HIGH SCORES", font = "Silom 30", fill = "black")
            canvas.create_text(mode.cx + mode.cx//2, 130, text = f"{''.join(LoginScreen.username)}'s PROGRESS", font = "Silom 30", fill = "black")
        
            Leaderboard.drawLeaderboard(mode, canvas)
            Leaderboard.drawGraph(mode, canvas)
            