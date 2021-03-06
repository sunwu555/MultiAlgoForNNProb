import kdtree
import collections
import time
empty = kdtree.create(dimensions = 8)
#empty = kdtree.create(dimensions = 7)
class Item(object):
    def __init__(self, _list):
        self.coords = _list[:len(_list)-1]
        self.name = _list[-1]

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, i):
        return self.coords[i]

    def __repr__(self):
        s = "("
        for i in range(len(self.coords)):
            s += str(self.coords[i])
            if i != len(self.coords)-1:
                s += ","

        s += ")"
        return s
        #return 'Item({},{},{},{}, {},{},{},{},{})'.format(self.coords[0], self.coords[1],self.coords[2],self.coords[3],
        #                                                  self.coords[4],self.coords[5],self.coords[6],self.coords[7],self.name)
def kdtree(filename):
#     empty = kdtree.create(dimensions = 8)
    with open(filename) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    for row in content:
        row = row.split(",")
        for i in range(len(row)):
            row[i] = int(row[i])
        print("!!!! ",row)
        point = Item( list(row) )
        print("**** ",point)
        empty.add(point)
    return empty


def result(string, empty):
    _input = []
    query = string.split(',')
    for i in range(len(query)):
        _input.append(int(query[i]))

    start_time = time.time()
    result = empty.search_nn(_input)

    T = "%s seconds" % (time.time() - start_time)
    
    distance = result[-1]

    coordinate = result[0].data

    str1 = "The nearest neighbor point's coordinate is : " + str(coordinate)
    str2 = "The time cost of kdtree is : " + T
    str3 = "The distance between query point and neareast point is : " + str(distance)
    return [str1, str2, str3]

#kdtree('itemset2.txt')
#print(result('1,2,3,4,5,6,7,8',empty))