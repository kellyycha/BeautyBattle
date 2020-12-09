from cmu_112_graphics import *
from tkinter import *
import string

class LoginScreen(Mode):
    username = []

    def appStarted(mode):
        mode.cx, mode.cy = mode.width // 2, mode.height // 2
        mode.background = mode.loadImage("images/background.jpg")
        LoginScreen.username = []
        mode.isTyping = False

    def mousePressed(mode, event):
        if (mode.cx - 50 <= event.x <= mode.cx + 50) and (mode.cy + 60 - 20 <= event.y <= mode.cy + 60 + 20):
            if LoginScreen.username != []:
                mode.app.setActiveMode(mode.app.startMode)
        if (mode.cx - 110 <= event.x <= mode.cx + 110) and (mode.cy - 20 <= event.y <= mode.cy + 20):
            mode.isTyping = True
        else:
            if LoginScreen.username != []:
                mode.isTyping = True
            else:
                mode.isTyping = False

    def keyPressed(mode, event):
        alphabet = string.ascii_letters
        digits = string.digits
        if mode.isTyping:
            if (event.key == "Delete" or event.key == "Backspace") and LoginScreen.username != []:
                LoginScreen.username.pop()
            elif len(LoginScreen.username) >= 7:
                return
            elif event.key == "Space":
                LoginScreen.username.append(" ")
            elif (event.key in alphabet) or (event.key in digits):
                LoginScreen.username.append(event.key)

    def redrawAll(mode, canvas):
        #background
        canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.background))

        canvas.create_text(mode.cx, mode.cy - 60, text = "Enter Username:", font = "Chicago 40 bold")
        canvas.create_rectangle(mode.cx - 110, mode.cy - 20, mode.cx + 110, mode.cy + 20, fill = "white")
        if mode.isTyping == False:
            canvas.create_text(mode.width//2, mode.height//2, text = "Click to start typing...", font = "Arial 20", fill = 'gray')
        else:
            canvas.create_text(mode.width//2, mode.height//2, text = "".join(LoginScreen.username), font = "Arial 20")

        #enter box
        canvas.create_rectangle(mode.cx - 50, mode.cy + 60 - 20, mode.cx + 50, mode.cy + 60 + 20, fill = "pink", outline = '')
        canvas.create_text(mode.cx, mode.cy + 60, text = "ENTER", font = "Chicago 20")
