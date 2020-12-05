from cmu_112_graphics import *
from PIL import Image, ImageDraw, ImageFilter


img = Image.new('RGBA', (1000,500), (255, 255, 255, 0))
draw = ImageDraw.Draw(img) 
draw.ellipse((150-20, 150-20, 150+20, 150+20), fill=(0,0,255,200))
img = img.filter(ImageFilter.GaussianBlur(3.5))

img.show()