import random as rnd

class player:
    hp = 100
    maxhp = 100
    rooms = 1
    lv = 1
    exp = 0
    lvlup = 100

    state = 0

    """
    0 - mapa
    1 - walka
    2 - ?
    3 - atak
    4 - inventory
    """

    pcords = [0, 0]

    inventory = [1, 2, 3, 4]

    elements = {
        0: "physical",
        1: "bow",
        2: "fire",
        3: "water",
        4: "wind",
        5: "thunder",
        6: "dark",
        7: "light",
    }

    items = {
        0: "fire sword",
        1: "bow",
        2: "water sword",
        3: "wind sword",
        4: "thunder sword",
        5: "sword of darkness",
        6: "sword of light"
    }

    item_types = {
        0 : 2,
        1 : 1,
        2 : 3,
        3 : 4,
        4 : 5,
        5 : 6,
        6 : 7
    }

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
    def itemfound(self):
        added = True
        while added:
            item = rnd.randint(0, 6)
            if item not in list(self.inventory):
                self.inventory.append(item)
                added = False