from cmu_112_graphics import *
from tkinter import *
import random
import os

class GameMode(Mode):
    def redrawAll(mode, canvas):
        canvas.create_text(mode.width//2, 150, text='Game', font="Arial 30 bold")