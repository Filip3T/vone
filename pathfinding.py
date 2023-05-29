import numpy as num
from heapq import heappush, heappop

def neighboring(a, cords, complex):
    lista = []
    for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        x = a[0] + i
        y =a[1] + j
        if 0 <= x < len(cords) and 0 <= y < len(cords[0]):
            if complex:
                if cords[x][y] not in [1, 5, 5, 7, 8, 9]:
                    lista.append((x, y))
            else:
                lista.append((x, y))
    return lista

def simplepathfinding(a, z, cords):
    score = [0, 0, 0, 0]
    #points = [[0, 0], [0, 0], [0, 0], [0, 0]]
    kroki = []
    while a != z:
        points = neighboring(a, cords, False)
        scoreind = 0
        for i in points:
            score[scoreind] = int(num.sqrt((i[1] - z[1])**2 + (i[0]- z[0])**2))
            scoreind += 1
        scoreind = 0
        minindex = score.index(min(score))
        a[0] = points[minindex][0]
        a[1] = points[minindex][1]
        #print("a: ",a)
        kroki.extend(a)
        #print("a: ",a, "z: ", z)


    for i in range(0, len(kroki)):
        if i % 2 == 0:
            kroki[i] = [kroki[i], kroki[i + 1]]
    
    krokicopy = kroki

    for i in range(0, int((len(krokicopy) / 2) + 1)):
        if type(krokicopy[i]) is int:
            del kroki[i]

    return kroki

def heuristic(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def complexpath(p, z):
    path = [z]
    while z in p:
        z = p[z]
        path.append(z)

    return path[::-1]

def complexpathfinding(a, z, cords): # A*
    open = []
    closed = set()
    heappush(open, (0, a))
    p = {}
    scoreG = {a: 0}
    scoreF = {a: heuristic(a, z)}
    
    while open:
        i = heappop(open)[1]
        if i == z:
            return complexpath(p, z)
    
        closed.add(i)
        for j in neighboring(i, cords, True):
            if j in closed:
                continue

            scorePG = scoreG[i] + 1
            if j not in scoreG or scorePG < scoreG[j]:
                p[j] = i
                scoreG[j] = scorePG
                scoreF[j] = scorePG + heuristic(j, z)
                heappush(open, (scoreF[j], j))
    