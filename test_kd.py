import random
import time
import kdtree

# This class emulates a tuple, but contains a useful payload
empty = kdtree.create(dimensions=8)


class Item(object):
    def __init__(self, x, y, z, o, a, b, c, d, name):
        self.coords = (x, y, z, o, a, b, c, d)
        self.name = name

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, i):
        return self.coords[i]

    def __repr__(self):
        return 'Item({},{},{},{}, {},{},{},{},{})'.format(self.coords[0], self.coords[1], self.coords[2],
                                                          self.coords[3],
                                                          self.coords[4], self.coords[5], self.coords[6],
                                                          self.coords[7], self.name)


# point1 = Item(2, 3,4.5,5.5,6,7,8,9 ,'First')
# tree = kdtree.create([point1])
# print(tree.search_nn([1, 2,3,4,5,7,8,9]))

fileObject = open('itemset.txt', 'w')
for i in range(500):
    x = str(random.randint(1, 500) * 100)
    y = str(random.randint(1, 500) * 100)
    z = str(random.randint(1, 500) * 100)
    o = str(random.randint(1, 500) * 100)
    a = str(random.randint(1, 500) * 100)
    b = str(random.randint(1, 500) * 100)
    c = str(random.randint(1, 500) * 100)
    d = str(random.randint(1, 500) * 100)
    #     li = [x,y,z,d,i]
    _str = "" + x + ',' + y + ',' + z + ',' + o + ',' + a + ',' + b + ',' + c + ',' + d + ',' + str(i)
    fileObject.write(_str)
    #     file.write(str(list_data));
    fileObject.write('\n')
fileObject.close()

empty = kdtree.create(dimensions=8)
with open('itemset.txt') as f:
    content = f.readlines()
    content = [x.strip('\n') for x in content]
for row in content:
    row = row.split(",")
    point = Item(int(row[0]), int(row[1]), int(row[2]), int(row[3]),
                 int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]))
    empty.add(point)

start_time = time.time()
result = empty.search_nn([40010, 35000, 38740, 1500, 2104, 5100, 31708, 34319])
time = "%s seconds" % (time.time() - start_time)
print(result)
a = str(result)
b = a.split('(')
distance = b[2].split(',')[9].split(')')[0]
print(distance)
d = b[2].split(')')[0].split(',')[0:8]
coordinate = "" + d[0] + ',' + d[1] + ',' + d[2] + ',' + d[3] + ',' + d[4] + ',' + d[5] + ',' + d[6] + ',' + d[7]
index = b[2].split(')')[0].split(',')[8]
print(coordinate)
print(index)
print(time)
empty = kdtree.create(dimensions=8)


class Item(object):
    def __init__(self, x, y, z, o, a, b, c, d, name):
        self.coords = (x, y, z, o, a, b, c, d)
        self.name = name

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, i):
        return self.coords[i]

    def __repr__(self):
        return 'Item({},{},{},{}, {},{},{},{},{})'.format(self.coords[0], self.coords[1], self.coords[2],
                                                          self.coords[3],
                                                          self.coords[4], self.coords[5], self.coords[6],
                                                          self.coords[7], self.name)


def kdtree(filename):
    #     empty = kdtree.create(dimensions = 8)
    with open(filename) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    for row in content:
        row = row.split(",")
        point = Item(int(row[0]), int(row[1]), int(row[2]), int(row[3]),
                     int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]))
        empty.add(point)
    return empty


def result(string, empty):
    _input = []
    query = string.split(',')
    for i in range(8):
        _input.append(int(query[i]))

    start_time = time.time()
    result = empty.search_nn([_input[0], _input[1], _input[2], _input[3], _input[4], _input[5], _input[6], _input[7]])

    T = "%s seconds" % (time.time() - start_time)
    a = str(result)
    b = a.split('(')
    distance = b[2].split(',')[9].split(')')[0]
    d = b[2].split(')')[0].split(',')[0:8]
    coordinate = "" + d[0] + ',' + d[1] + ',' + d[2] + ',' + d[3] + ',' + d[4] + ',' + d[5] + ',' + d[6] + ',' + d[7]
    index = b[2].split(')')[0].split(',')[8]
    str1 = "The nearest neighbor point's coordinate is : " + coordinate
    str2 = "The time cost of kdtree is : " + T
    str3 = "The distance between query point and neareast point is : " + distance
    return [str1, str2, str3]


kdtree('itemset.txt')
result('1,2,3,4,5,6,7,8')
