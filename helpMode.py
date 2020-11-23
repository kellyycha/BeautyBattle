from cmu_112_graphics import *

class HelpMode(Mode):
    def appStarted(mode):
        parentDir = os.path.abspath("..")
        img_dir = os.path.join(parentDir, "termProject/images/splashBG.jpg")
        mode.background = mode.loadImage(img_dir)

    def redrawAll(mode, canvas):
        cx, cy = mode.width // 2, mode.height // 2
        canvas.create_image(cx, cy, image = ImageTk.PhotoImage(mode.background))

        canvas.create_text(cx, 100, text='This is the help screen!', font='Arial 30 bold')
        canvas.create_text(cx, 200, text='(Insert helpful message here)', font='Arial 20')
        canvas.create_text(cx, 375, text='Press H return to the game', font='Arial 20 bold')
        canvas.create_text(cx, 400, text='Press S return to the start screen', font='Arial 20 bold')

    def keyPressed(mode, event):
        if event.key == "h":
            mode.app.setActiveMode(mode.app.gameMode)
        if event.key == "s":
            mode.app.setActiveMode(mode.app.startMode)
            #want to make it reset
