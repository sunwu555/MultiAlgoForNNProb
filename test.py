from skimage import transform
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
import numpy as np

width = 100
height = 100　
center = height//2
white = (255, 255, 255)
green = (0,128,0)

def save():
    global 
    pix = np.array(WritePic)
    ans = []
    a = []
    for i in pix:
        a = []
        for k in i:
            if k [0] > 100:
                a.append(0)
            else:
                a.append(1)
        ans.append(a)
    for i in ans:
        print(i)

def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=12)
    draw.line([x1, y1, x2, y2],fill="black",width=12)

root = Tk()

# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
# image1.save(filename)
button=Button(text="save",command=save)
button.pack()
root.mainloop()