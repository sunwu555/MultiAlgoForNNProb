import numpy as np
#import skimage.io
from PIL import Image
import os

import kdtree
import time


def TransToVector(filename, F):
    imgs = Image.open(filename)
    imgs = np.array(imgs)
    ans = []
    a = []
    for i in imgs:
        for k in i:
            if k[0] > 254:
                a.append(0)
            else:
                a.append(1)
    name = filename.split('/')[-1]
    a.append(name)
    F.append(a)


class Item(object):
    def __init__(self, _list):
        self.coords = _list[:len(_list) - 1]
        self.name = _list[-1]

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, i):
        return self.coords[i]

    def __repr__(self):
        s = "("
        for i in range(len(self.coords)):
            s += str(self.coords[i])
            if i != len(self.coords) - 1:
                s += ","
        s += ")"
        s += ","
        s += str(self.name)
        return s


def output(D, Q, empty):
    r = []
    for i in D:
        point = Item(i)
        empty.add(point)
    start_time = time.time()
    result = empty.search_knn(Q, 3)
    for i in result:
        r.append(i[0].data.name)
    r.append(time.time() - start_time)
    return (r)


def kd_package(Q):
    D = []
    for root, dirs, files in os.walk('./dataset'):
        for file in files:
            if file.endswith(".png"):
                filename = (root + '/' + file)
                TransToVector(filename, D)
    empty = kdtree.create(dimensions=2500)
    return output(D, Q, empty)

'''
a = []
for i in range(2500):
    a .append(0)
print(kd_package(a))
'''