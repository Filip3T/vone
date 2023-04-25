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