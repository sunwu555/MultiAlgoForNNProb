import tkinter as tk
import lsh_504
import kd_tree
import PIL
from PIL import Image, ImageTk, ImageDraw  
from tkinter.filedialog import askopenfilename 
import numpy as np
from skimage import transform

def main():
    global InputFile
    global InputQuery
    global InputQuery
    global LSHResult
    global LSHTime
    global KdTreeResult
    global KdTreeTime
    global lsh2
    global kdtree2
    global path_get
    global InputPic
    global WriteArea
    global draw
    global root
    global WritePic
    
    root = tk.Tk()
    root.geometry('600x800')
    root.title('test')
    
    LSHResult = tk.StringVar()
    LSHTime = tk.StringVar()
    KdTreeResult = tk.StringVar()
    KdTreeTime = tk.StringVar()
    PicPath = tk.StringVar()
    path_get = tk.StringVar()
    PathInput = ''
    
#show title image here
#-----------------------------------------------------------------
    im = Image.open("./UI_Image/title.png")  
    im = im.resize((400, 50), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(im) 
    titlepic = tk.Label(root, image = photo)
    titlepic.grid(row = 1, column = 1, columnspan = 4, pady = 1)
#-----------------------------------------------------------------

    InputFile = tk.Entry(root, width = 20, textvariable = path_get)
    InputFile.grid(row = 2, column = 1, columnspan = 2, padx = 5, sticky = '')

    SelectButton = tk.Button(root, width = 7, height = 2, text = 'Select',
                           command = choosepic)
    SelectButton.grid(row = 3, column = 1)
    
    InputButton = tk.Button(root, width = 7, height = 2, text = 'Input',
                           command = get_input)
    InputButton.grid(row = 3, column = 2,)

#show input image here
#-----------------------------------------------------------------    
    
    im1=Image.open('./UI_Image/InputPic.png')  
    im1 = im1.resize((180, 102), Image.ANTIALIAS)
    photo_input=ImageTk.PhotoImage(im1) 

    '''
    InputPic = tk.Label(root, image = photo_input)
    InputPic.grid(row = 2, column = 3, rowspan = 2, columnspan = 2)
    '''

    WritePic = PIL.Image.new("RGB", (100, 100), (255,255,255))
    draw = ImageDraw.Draw(WritePic)

    WriteArea = tk.Canvas(root, width = 100, height = 100, bg='gray90')
    WriteArea.grid(row = 2, column = 3, rowspan = 2, columnspan = 2)
    WriteArea.bind("<B1-Motion>", paint)

    ClearButton = tk.Button(root, width = 7, height = 2, text = 'Clear',
                           command = clear_input)
    ClearButton.grid(row = 4, column = 4, pady = 10)

#-----------------------------------------------------------------

    label0 = tk.Label(root, text = 'Data set path: ./dataset', height = 2,)
    label0.grid(row = 4, column = 1, columnspan = 2, sticky = 'NSEW', pady = 10)
    
    QueryButton = tk.Button(root, width = 7, height = 2, text = 'Query',
                           command = get_query)
    QueryButton.grid(row = 4, column = 3, pady = 10)
    
    label2 = tk.Label(root, text = 'LSH', height = 2, font = '-size 18', bg = 'Cyan')
    label2.grid(row = 5, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')
    
    label3 = tk.Label(root, text = 'Kd-tree', height = 2, font = '-size 18', bg = 'Beige')
    label3.grid(row = 5, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')
    
    label4 = tk.Label(root, text = 'Result', height = 1, font = '-size 12', bg = 'LightCyan')
    label4.grid(row = 6, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    LSH_result = tk.Label(root, text = 'LSH Result', height = 2, font = '-size 18', bg = 'LightCyan')
    LSH_result.grid(row = 7, column = 1, columnspan = 2, padx = 15, sticky = 'NSEW')
    
    label5 = tk.Label(root, text = 'Result', height = 1, font = '-size 12', bg = 'LightGoldenrodYellow')
    label5.grid(row = 6, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    Kd_result = tk.Label(root, text = 'Kd-tree Result', height = 2,  font = '-size 18', bg = 'LightGoldenrodYellow')
    Kd_result.grid(row = 7, column = 3, columnspan = 2, padx = 15, sticky = 'NSEW')
    
#show nearst 3 items
#---------------------------------------------------------------------------------
    label6 = tk.Label(root, text = 'Nearst Items', height = 1, font = '-size 12', bg = 'Cyan')
    label6.grid(row = 8, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    label7 = tk.Label(root, text = 'Nearst Items', height = 1, font = '-size 12', bg = 'Beige')
    label7.grid(row = 8, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    KdResult0 = tk.Label(root, image = photo_input, bg = 'Cyan')
    KdResult0.grid(row = 9, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    KdResult1 = tk.Label(root, image = photo_input, bg = 'Cyan')
    KdResult1.grid(row = 10, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    KdResult2 = tk.Label(root, image = photo_input, bg = 'Cyan')
    KdResult2.grid(row = 11, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    LSHResult0 = tk.Label(root, image = photo_input, bg = 'Beige')
    LSHResult0.grid(row = 9, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    LSHResult1 = tk.Label(root, image = photo_input, bg = 'Beige')
    LSHResult1.grid(row = 10, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    LSHResult2 = tk.Label(root, image = photo_input, bg = 'Beige')
    LSHResult2.grid(row = 11, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')
#---------------------------------------------------------------------------------

    label8 = tk.Label(root, text = 'Running Time', height = 1, font = '-size 12', bg = 'LightCyan')
    label8.grid(row = 12, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')
    
    label9 = tk.Label(root, text = 'Running Time', height = 1, font = '-size 12', bg = 'LightGoldenrodYellow')
    label9.grid(row = 12, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    KdTiming = tk.Label(root, text = 'Kd-tree Time', height = 2, font = '-size 18', bg = 'LightCyan')
    KdTiming.grid(row = 13, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    LSHTiming = tk.Label(root, text = 'LSH Time', height = 2, font = '-size 18', bg = 'LightGoldenrodYellow')
    LSHTiming.grid(row = 13, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    '''
    show image
    '''
    '''
    im=Image.open("./png250px/ad.png")  
    im = im.resize((80, 60), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(im) 
    label8 = tk.Label(root, image = photo)
    label8.grid(row = 11, column = 2)
    '''
    root.mainloop()

#for writing number
#------------------------------------------------------------
def save():
    filename = "image.png"
    WritePic.save(filename)

def paint(event):
    global WriteArea
    global draw
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    WriteArea.create_oval(x1, y1, x2, y2, fill="black",width=12)
    draw.line([x1, y1, x2, y2],fill="black",width=12)

def clear_input():
    global draw
    global WriteArea
    global root
    global WritePic

    WritePic = PIL.Image.new("RGB", (100, 100), (255,255,255))
    draw = ImageDraw.Draw(WritePic)

    WriteArea = tk.Canvas(root, width = 100, height = 100, bg='gray90')
    WriteArea.grid(row = 2, column = 3, rowspan = 2, columnspan = 2)
    WriteArea.bind("<B1-Motion>", paint)

#-------------------------------------------------------------

def choosepic():  
    global path_get
    global PathInput
    PathInput = askopenfilename()     
    path_get.set(PathInput)

def get_input():
    global InputFile
    global InputQuery
    global LSHResult
    global LSHTime
    global KdTreeResult
    global KdTreeTime
    global lsh2
    global kdtree2
    #set new input pic
    #----------------------------------------------------------
    global InputPic
    global PathInput
    im0=Image.open(str(PathInput))  
    im0 = im0.resize((180, 102), Image.ANTIALIAS)
    photo0=ImageTk.PhotoImage(im0) 
    InputPic.config(image = photo0)
    InputPic.image = photo0
    #----------------------------------------------------------

    
def get_query():
    global InputQuery
    global LSHResult
    global LSHTime
    global KdTreeResult
    global KdTreeTime
    global lsh2
    global kdtree2
    global WritePic

    WritePic1 = WritePic.resize((50, 50), Image.ANTIALIAS)
    pix = np.array(WritePic1)
    a = []
    for i in pix:
        for k in i:
            if k [0] > 100:
                a.append(0)
            else:
                a.append(1)
    print(a)


if __name__ == '__main__':
    main()
