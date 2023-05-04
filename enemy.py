import pathfinding as path
import random as rnd
import numpy as num
import board
import time
import os
import fight as fgt


class enemy:

    px = 0
    py = 0
    moves = 4

    def __init__(self, name, type):
        self.type = type
        self.name = name
        self.moves = 4
    
    def mapadd(self, cords, x, y):
        notspawned = True
        while notspawned:
            spawntryX = rnd.randint(0, x - 1)
            spawntryY = rnd.randint(0, y - 1)
            if cords[spawntryY][spawntryX] == 0:
                if self.name == "en1":
                    cords[spawntryY][spawntryX] = 5
                if self.name == "en2":
                    cords[spawntryY][spawntryX] = 6
                if self.name == "en3":
                    cords[spawntryY][spawntryX] = 7
                self.px = spawntryX
                self.py = spawntryY
                notspawned = False
        return cords


    def tura(self, cords, pcords, x, y, moves, en1, en2, en3, player):
        aggressive = int(num.sqrt((self.px - pcords[1])**2 + (self.py - pcords[0])**2)) <= 4
        print(aggressive)
        if aggressive:
            go = path.complexpathfinding((self.py, self.px), tuple(pcords), cords)
            if go is None:
                found = True
                while found:
                    gotryX = rnd.randint(0, x - 1)
                    gotryY = rnd.randint(0, y - 1)
                    if int(num.sqrt((self.px - gotryX)**2 + (self.py - gotryY)**2)) >= 6:
                        if cords[gotryY][gotryX] == 0:
                            goX = gotryX
                            goY = gotryY
                            go = path.complexpathfinding((self.py, self.px), (goY, goX), cords)
                            if go is not None:
                                found = False
        else:
            found = True
            while found:
                gotryX = rnd.randint(0, x - 1)
                gotryY = rnd.randint(0, y - 1)
                if int(num.sqrt((self.px - gotryX)**2 + (self.py - gotryY)**2)) >= 6:
                    if cords[gotryY][gotryX] == 0:
                        goX = gotryX
                        goY = gotryY
                        go = path.complexpathfinding((self.py, self.px), (goY, goX), cords)
                        if go is not None:
                            found = False
        print(self.py, self.px)
        print(go)
        left = 0
        for i in range(1, self.moves + 1):
            cords[self.py][self.px] = left
            print(go)
            if cords[go[i][0]][go[i][1]] == 2:
                time.sleep(1) # dla dramatycznego efektu XD
                os.system('cls')
                fgt.fight(player)
                return "fight"
            left = cords[go[i][0]][go[i][1]]
            self.py = go[i][0]
            self.px = go[i][1]
            if self.name == "en1":
                cords[go[i][0]][go[i][1]] = 5
                en1.moves -= 1
            if self.name == "en2":
                cords[go[i][0]][go[i][1]] = 6
                en2.moves -= 1
            if self.name == "en3":
                cords[go[i][0]][go[i][1]] = 7
                en3.moves -= 1
            

            #cords[go[i][0]][go[i][1]] = 5
            time.sleep(1)
            os.system('cls')
            board.plansza(x, y, cords, moves, en1, en2, en3, player)
        
        