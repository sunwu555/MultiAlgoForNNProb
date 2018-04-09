# MultiAlgoForNNProb
A python program for implementing and comparing for multiple NN algorithm(kd-tree, LSH, etc) 

Introduction
---

The multi-algo-for-nn is an local application which could help user quickly using several different algorithms to search a large database for the nearest neighbor of a given sample. Also user could compare the performances of each algorithm by program outputs data of time/space consuming and accuracy of results.

Brief Instructions
---
---
### 04/09 Update
>The shell script has implemented, now program can run by 
    
    /bin/sh start.sh
---

1, Clone whole project into local computer.

    git clone https://github.com/sunwu555/MultiAlgoForNNProb.git
    
2, Go to LSHash_Master directory. 
    
    cd LSHash_Master
        
3, Install the LSHash library by

    pip install e .
    
4, Go to kd-tree directory.

    cd kd-tree
    
5, Install the kd-tree libarary by 

    pip install e .
    
6, Go to the MultiAlgoForNNProb-master directory.

    cd MultiAlgoForNNProb-master

7, Open the proto_top.py by

    python proto_top.py

8, The GUI will be like

![](https://github.com/sunwu555/MultiAlgoForNNProb/blob/master/UI.png)
    
8.1, First, enter the name of data file into the box from upper left(Arrow 1)e.g:"test.txt". The input format should be like the sample format.

8.2, Second, hit Input(Arrow 2).

8.3, Third, enter the query point into the box from upper right(Arrow 3, the format should be like the image shows. Now the program only support 8-dimensions vector).

8.4, Then, hit Query(Arrow 4).

8.5, Finally the results will be shown in the big box.(Arrow 5)

Reference
---

For the implementing of LSHash, 

>This function was built from (https://github.com/kayzhu/LSHash).

For the implementing of KD-TREE,, 

> function was built from (https://github.com/stefankoegl/kdtree).
