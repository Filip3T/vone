import random as rnd
import pathfinding as path

def generation(map, x, y):
    copy = []
    for nothing in range(0, rnd.randint(3, 6)):
        rx = rnd.randint(0, int((x / 4) * 3))
        ry = rnd.randint(0, int((y/ 4) * 3))
        xd = rnd.randint(int(x / 4), int((x / 2)))
        yd = rnd.randint(int(x / 4), int((y / 2)))
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
            
            for el in path.simplepathfinding(pastpoint, a):
                print(el)
                map[el[0]][el[1]] = 0



    return map