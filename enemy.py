import pathfinding as path
import random as rnd


class enemy:
    def __init__(self, name, type):
        self.type = type
        self.name = name
        if type == 0:
            self.moves = 4
        else:
            self.moves = 6
    
    def mapadd(self, cords, x, y):
        notspawned = True
        while notspawned:
            spawntryX = rnd.randint(0, x - 1)
            spawntryY = rnd.randint(0, y - 1)
            if cords[spawntryY][spawntryX] == 0:
                cords[spawntryY][spawntryX] = 5
                notspawned = False
        return cords
        
    def tura(self, cords, x, y, pcords):
        print("zrobie to kiedys")