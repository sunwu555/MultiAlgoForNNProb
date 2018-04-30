import sys
sys.path.append(r"./LSHash")
from lshash import LSHash
import numpy as np
import os
import time

class LSH():
    def __init__(self,path,lsh):
        #lsh = LSHash(7,2500)
        pathDir = os.listdir(path)
        txt_list = []
        filename = ""
        for file in pathDir:
            if file.endswith('txt'):
                txt_list.append(file)

        for i in txt_list:
            filename = ""
            filename += path
            filename += "//"
            filename += i
            #print(filename)
            f = open(filename)
            c = f.read().strip('[').strip(']').split(r',')
            c = list(map(int, c))
            #print(type(c))
            lsh.index(c,i)
    def query(self, _list,lsh):
        ss = "./dataset"
        
        cost_time = float()
        st = time.time()
        result = lsh.query(_list)
        cost_time = [time.time() - st]
        print(cost_time)
        result_file_name = []


        if len(result) == 0:
            return [],cost_time
        elif len(result) <=3:
            for i in result:
                tmp = str(i[0][1].split('.')[0]) + ".png"
                result_file_name.append(tmp)
        else:
            for i in range(3):
                tmp = str(result[i][0][1].split('.')[0]) + ".png"
                result_file_name.append(tmp)

        return result_file_name, cost_time