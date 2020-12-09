from cmu_112_graphics import *

class HelpMode(Mode):
    def appStarted(mode):
        mode.cx, mode.cy = mode.width // 2, mode.height // 2
        mode.background = mode.loadImage("images/background.jpg")
    
    #from 15112 PIL Notes
    def getCachedPhotoImage(mode, image):
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

    def keyPressed(mode, event):
        #resumes where left off
        if event.key == "h":
            mode.app.setActiveMode(mode.app.gameMode)
        #restarts
        if event.key == "s":
            mode.app.gameMode.appStarted()
            mode.app.setActiveMode(mode.app.startMode)

    def redrawAll(mode, canvas):
        bg = HelpMode.getCachedPhotoImage(mode, mode.background)
        canvas.create_image(mode.cx, mode.cy, image = bg)

        canvas.create_text(mode.cx, 100, text='This is the help screen!', font='Chicago 30 bold')
        canvas.create_rectangle(0, mode.cy - 100, mode.width, mode.cy + 100, fill = 'white', outline = '')
        canvas.create_text(mode.cx + 150, mode.cy, text='You want a spot as an employee at the KC Beauty Studio,\
                                            \nbut there is only one spot available.\n\
                                            \n- Fill in the dotted lines with the correct products and colors.\
                                            \n- Coloring outside the lines & not filling in completely will deduct points.\
                                            \n- Complete before time runs out! You have the opportunity to submit early\
                                            \n  to stop your opponent from finishing.', 
                                            font='Arial 20')
        canvas.create_text(mode.cx, 375, text='Press H return to the game', font='Chicago 20')
        canvas.create_text(mode.cx, 400, text='Press S return to the start screen', font='Chicago 20')

    
