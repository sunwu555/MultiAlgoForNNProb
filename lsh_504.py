from lshash import LSHash
import time

def get_lshash(filename):
    lsh = LSHash(30,8)
    try:
        with open(filename) as f:
            content = f.readlines()
            content = [x.strip('\n') for x in content]
    except Exception as e:
        print("Cannot find the file.")
    
    for row in content:
        row = row.split(",")
        row = list(map(int,row))
        tmp = row[:8]
        lsh.index(tmp,str(row[8]))
    
    return lsh

def lsh_query(q,lsh):
    q = q.split(",")
    print(q)
    q = list(map(float,q))
    print(q)
    try:
        start_time = time.time()
        f = lsh.query(q,1)
        stop_time = time.time()
        str1 = "The nearest neighbor point's coordinate is :\n" + str(f[0][0][0])
        str2 = "" + str(stop_time - start_time) + " seconds"
        str3 = "The distance is : " + str(f[0][1])
        return [str1,str2,str3]
    except Exception as e:
        print(str(e))
#print("The input format is not legitimate.")
