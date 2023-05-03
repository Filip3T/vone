import random as rnd

class player:
    hp = 100
    maxhp = 100
    rooms = 1
    lv = 1
    pcords = [0, 0]

    def spawn(self, x, y, cords):
        self.pcords = [y - 1, 0]

        notspawned = True
        while notspawned:
            spawntryX = rnd.randint(0, x - 1)
            # print(cords[spawntryY][spawntryX])
            if cords[y - 1][spawntryX] == 0:
                self.pcords[1] = spawntryX
                cords[y - 1][spawntryX] = 3
                #pcords[1] = cords[spawntryX]
                notspawned = False
        #print(self.pcords)