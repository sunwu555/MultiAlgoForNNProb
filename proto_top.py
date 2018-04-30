import tkinter as tk
# import skimage.io
import PIL
from PIL import Image, ImageTk, ImageDraw  
from tkinter.filedialog import askopenfilename 
import numpy as np
from skimage import transform
import time
import os

import kd_renew
import lsh_find
import naive

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
    global KdResult0 
    global KdResult1 
    global KdResult2 
    global LSHResult0
    global LSHResult1
    global LSHResult2
    global photo_input
    global NaiveTime
    global NaiveTiming
    
    global find_lsh
    global lsh

    root = tk.Tk()
    root.geometry('410x660')
    root.title('Writing Board')
    
    LSHResult = tk.StringVar()
    LSHTime = tk.StringVar()
    KdTreeResult = tk.StringVar()
    KdTreeTime = tk.StringVar()
    NaiveTime = tk.StringVar()

    PicPath = tk.StringVar()
    path_get = tk.StringVar()
    PathInput = ''

    lsh = lsh_find.LSHash(6,2500)
    find_lsh = lsh_find.LSH("./dataset",lsh)
#show title image here
#-----------------------------------------------------------------
    im = Image.open("./UI_Image/title.png")  
    # im = im.resize((400, 50), Image.ANTIALIAS)
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
    im1 = im1.resize((50, 50), Image.ANTIALIAS)
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
    
    label2 = tk.Label(root, text = 'Kd-tree', height = 2, font = '-size 18', bg = 'Cyan')
    label2.grid(row = 5, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')
    
    label3 = tk.Label(root, text = 'LSH', height = 2, font = '-size 18', bg = 'Beige')
    label3.grid(row = 5, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')
    
    label4 = tk.Label(root, text = 'Result', height = 1, font = '-size 12', bg = 'LightCyan')
    label4.grid(row = 6, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    Kd_result = tk.Label(root, textvariable = KdTreeResult, height = 2, font = '-size 22', bg = 'LightCyan')
    Kd_result.grid(row = 7, column = 1, columnspan = 2, padx = 15, sticky = 'NSEW')
    
    label5 = tk.Label(root, text = 'Result', height = 1, font = '-size 12', bg = 'LightGoldenrodYellow')
    label5.grid(row = 6, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    LSH_result = tk.Label(root, textvariable = LSHResult, height = 2,  font = '-size 22', bg = 'LightGoldenrodYellow')
    LSH_result.grid(row = 7, column = 3, columnspan = 2, padx = 15, sticky = 'NSEW')
    
#show Nearest 3 items
#---------------------------------------------------------------------------------
    label6 = tk.Label(root, text = 'Nearest Items', height = 1, font = '-size 12', bg = 'Cyan')
    label6.grid(row = 8, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    label7 = tk.Label(root, text = 'Nearest Items', height = 1, font = '-size 12', bg = 'Beige')
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

    KdTiming = tk.Label(root, textvariable = KdTreeTime, height = 2, font = '-size 18', bg = 'LightCyan')
    KdTiming.grid(row = 13, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    LSHTiming = tk.Label(root, textvariable = LSHTime, height = 2, font = '-size 18', bg = 'LightGoldenrodYellow')
    LSHTiming.grid(row = 13, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    label10 = tk.Label(root, text = 'Made by Tong Ye, Weixuan Jiang, Wu Sun, Yujia Wang',
                        height = 1, font = '-size 12')
    label10.grid(row = 14, column = 1, columnspan = 4, padx = 15, pady = 5, sticky = 'NSEW')

    label11 = tk.Label(root, text = 'Naive Time', height = 1, font = '-size 12', bg = 'LightCyan')
    label11.grid(row = 15, column = 1, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

    NaiveTiming = tk.Label(root, textvariable = NaiveTime, height = 2, font = '-size 18', bg = 'LightGoldenrodYellow')
    NaiveTiming.grid(row = 15, column = 3, columnspan = 2, padx = 15, pady = 1, sticky = 'NSEW')

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
    global KdResult0 
    global KdResult1 
    global KdResult2 
    global LSHResult0
    global LSHResult1
    global LSHResult2
    global photo_input
    global NaiveTime
    global NaiveTiming

    global find_lsh
    global lsh

    WritePic1 = WritePic.resize((50, 50), Image.ANTIALIAS)
    pix = np.array(WritePic1)
    a = []
    for i in pix:
        for k in i:
            if k [0] > 100:
                a.append(0)
            else:
                a.append(1)
    #print(a)
    #set kd tree result variable
    #---------------------------------------------------------

    # kdname = ['0_0.png', '0_1.png', '0_3.png', '+1s']
    kdname = kd_renew.kd_package(a)

    im_kd0 = Image.open('./dataset/' + kdname[0])  
    photo_kd0 = ImageTk.PhotoImage(im_kd0) 
    KdResult0.config(image = photo_kd0)
    KdResult0.image = photo_kd0
    im_kd1 = Image.open('./dataset/' + kdname[1])  
    photo_kd1 = ImageTk.PhotoImage(im_kd1) 
    KdResult1.config(image = photo_kd1)
    KdResult1.image = photo_kd1
    im_kd2 = Image.open('./dataset/' + kdname[2])  
    photo_kd2 = ImageTk.PhotoImage(im_kd2) 
    KdResult2.config(image = photo_kd2)
    KdResult2.image = photo_kd2
    if kdname[1][0] == kdname[2][0]:
        KdTreeResult.set(kdname[1][0])
    else:
        KdTreeResult.set(kdname[0][0])
    KdTreeTime.set(round(kdname[3], 6))
    #set LSH result variable
    #---------------------------------------------------------
    lshname,lsh_time = find_lsh.query(a, lsh)

    if len(lshname) == 3:
        im_lsh0 = Image.open('./dataset/' + lshname[0])  
        photo_lsh0 = ImageTk.PhotoImage(im_lsh0) 
        LSHResult0.config(image = photo_lsh0)
        LSHResult0.image = photo_lsh0
        im_lsh1 = Image.open('./dataset/' + lshname[1])  
        photo_lsh1 = ImageTk.PhotoImage(im_lsh1) 
        LSHResult1.config(image = photo_lsh1)
        LSHResult1.image = photo_lsh1
        im_lsh2 = Image.open('./dataset/' + lshname[2])  
        photo_lsh2 = ImageTk.PhotoImage(im_lsh2) 
        LSHResult2.config(image = photo_lsh2)
        LSHResult2.image = photo_lsh2
        if lshname[1][0] == lshname[2][0]:
            LSHResult.set(lshname[1][0])
        else:
            LSHResult.set(lshname[0][0])
        LSHTime.set(round(lsh_time[0],6))
    elif len(lshname) == 2:
        im_lsh0 = Image.open('./dataset/' + lshname[0])  
        photo_lsh0 = ImageTk.PhotoImage(im_lsh0) 
        LSHResult0.config(image = photo_lsh0)
        LSHResult0.image = photo_lsh0
        im_lsh1 = Image.open('./dataset/' + lshname[1])  
        photo_lsh1 = ImageTk.PhotoImage(im_lsh1) 
        LSHResult1.config(image = photo_lsh1)
        LSHResult1.image = photo_lsh1
        LSHResult.set(lshname[0][0])
        LSHTime.set(round(lsh_time[0], 6))
    elif len(lshname) == 1:
        im_lsh0 = Image.open('./dataset/' + lshname[0])  
        photo_lsh0 = ImageTk.PhotoImage(im_lsh0) 
        LSHResult0.config(image = photo_lsh0)
        LSHResult0.image = photo_lsh0
        LSHResult.set(lshname[0][0])
        LSHTime.set(round(lsh_time[0], 6))
    elif len(lshname) == 0:
        LSHResult0.config(image = photo_input)
        LSHResult0.image = photo_input
        LSHResult1.config(image = photo_input)
        LSHResult1.image = photo_input
        LSHResult2.config(image = photo_input)
        LSHResult2.image = photo_input
        LSHResult.set('null')
        LSHTime.set('null')

    NaiveTime.set(str(round(naive.NaiveAlgo(a), 6)))

if __name__ == '__main__':
    main()
