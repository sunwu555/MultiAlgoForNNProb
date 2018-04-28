import numpy as np
from PIL import Image
import skimage.io
from skimage import transform,data

imgs = skimage.io.imread('./dataset/0_0.png')
ans = []
a = []
for i in imgs:
    a = []
    for k in i:
        if k [0] > 100:
            a.append(0)
        else:
            a.append(1)
    ans.append(a)
for i in ans:
    print(i)