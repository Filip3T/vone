import numpy as num

def simplepathfinding(a, z):
    score = [0, 0, 0, 0]
    points = [[0, 0], [0, 0], [0, 0], [0, 0]]
    kroki = []
    while a != z:
        points[0] = [(a[0] - 1),(a[1])]
        points[1] = [(a[0]),(a[1] + 1)]
        points[2] = [(a[0] + 1),(a[1])]
        points[3] = [(a[0]),(a[1] - 1)]
        scoreind = 0
        for i in points:
            score[scoreind] = int(num.sqrt((i[1] - z[1])**2 + (i[0]- z[0])**2))
            scoreind += 1
        scoreind = 0
        maxindex = score.index(min(score))
        a[0] = points[maxindex][0]
        a[1] = points[maxindex][1]
        kroki.append(a)
        #print("a: ",a, "z: ", z)
    return kroki