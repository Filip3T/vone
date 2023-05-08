import random as rnd
import pathfinding as path

def epaths(x, y, side, map):
    startpath = []
    starttry = rnd.randint(0, x - 1)
    flag = True
    if side == 1:
        run = list(reversed(range(0, y - 1)))
    else:
        run = list(range(0, y - 1))
    while flag:
        #print("tak", starttry, side)
        for i in run:
            #print(startpath)
            if map[i][starttry] == 0:
                #if side == 0:
                #    map[0][starttry] = 4
                startpath.extend([i, starttry])
                for k in range(0, len(startpath)):
                    if k % 2 == 0:
                        startpath[k] = [startpath[k], startpath[k + 1]]
                pathcopy = startpath
                for j in range(0, int(len(pathcopy) / 2)):
                    if type(pathcopy[j]) is int:
                        del startpath[j]
                del startpath[-1]
                #print(startpath)
                flag = False
                break

            else:
                startpath.extend([i, starttry])
        if flag:
            startpath = []
            starttry = rnd.randint(0, x - 1)

    
    for i in startpath:
        if side == 1:
            map[i[0] + 1][i[1]] = 0
        else:
            if i != startpath[0]:
                map[i[0]][i[1]] = 0
            else:
                map[i[0]][i[1]] = 4

    return map




def generation(map, x, y):
    copy = []
    for nothing in range(0, rnd.randint(4, 6)):
        rx = rnd.randint(0, int((x / 4) * 3))
        ry = rnd.randint(0, int((y/ 4) * 3))
        xd = rnd.randint(int(x / 4), int((x / 3)))
        yd = rnd.randint(int(x / 4), int((y / 3)))
        middle = [0, 0]
        middle[0] = int(yd / 2) + ry
        middle[1] = int(xd / 2) + rx
        copy.append(middle)
        for i in range(0, xd):
            for j in range(0, yd):
                if ry + j <= y - 1 and rx + i <= x - 1:
                    map[ry + j][rx + i] = 0

    pastpoint = copy[0]
    for a in copy:
        if a != copy[0]:
            for el in path.simplepathfinding(pastpoint, a, map):
                map[el[0]][el[1]] = 0

    map = epaths(x, y, 1, map)
    map = epaths(x, y, 0, map)

    trs = int(rnd.random() * 100) % 4 

    if trs == 1:
        flag = True
        while flag:
            trsxtry = rnd.randint(0, x - 1)
            trsytry = rnd.randint(0, y - 1)
            if map[trsytry][trsxtry] == 0:
                map[trsytry][trsxtry] = 8
                flag = False

    return map