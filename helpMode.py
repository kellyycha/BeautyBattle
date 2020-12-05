from cmu_112_graphics import *

class HelpMode(Mode):
    def appStarted(mode):
        mode.cx, mode.cy = mode.width // 2, mode.height // 2
        mode.background = mode.loadImage("images/background.jpg")

    def redrawAll(mode, canvas):
        canvas.create_image(mode.cx, mode.cy, image = ImageTk.PhotoImage(mode.background))

        canvas.create_text(mode.cx, 100, text='This is the help screen!', font='Arial 30 bold')
        canvas.create_rectangle(0, mode.cy - 100, mode.width, mode.cy + 100, fill = 'white', outline = '')
        canvas.create_text(mode.cx + 150, mode.cy, text='You want a spot as an employee at the KC Beauty Studio,\
                                            \nbut there is only one spot available.\n\
                                            \n- Fill in the dotted lines with the correct products and colors.\
                                            \n- Coloring outside the lines & not filling in completely will deduct points.\
                                            \n- Complete before time runs out! You have the opportunity to submit early\
                                            \n  to stop your opponent from finishing.', 
                                            font='Arial 20')
        canvas.create_text(mode.cx, 375, text='Press H return to the game', font='Arial 20 bold')
        canvas.create_text(mode.cx, 400, text='Press S return to the start screen', font='Arial 20 bold')

    def keyPressed(mode, event):
        if event.key == "h":    #resumes where left off
            mode.app.setActiveMode(mode.app.gameMode)
        if event.key == "s":    #restarts
            mode.app.gameMode.appStarted()
            mode.app.setActiveMode(mode.app.startMode)
