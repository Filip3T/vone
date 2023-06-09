import random as rnd
import time

class player:
    hp = 100
    maxhp = 100
    rooms = 1
    lv = 1
    exp = 0
    lvlup = 100
    dmg_mlt = 1
    def_mlt = 1
    
    eq1 = 7
    eq2 = 8
    eq3 = 1
    eq4 = 9

    state = 0

    """
    0 - mapa
    1 - walka
    2 - ?
    3 - atak
    4 - inventory - menu
    5 - inventory - walka
    6 - equip
    7 - inventory look through
    8 - equip weapon
    9 - use weapon

    1 - phoenix
    2 - water nymph
    3 - harpy
    4 - gryph
    5 - dryad
    6 - golem
    7 - ice golem
    8 - pegasus
    9 - dragon
    10 - unicorn
    """

    pcords = [0, 0]

    inventory = [1, 7, 8, 9]

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
        0 : "fire sword",
        1 : "basic bow",
        2 : "water sword",
        3 : "wind sword",
        4 : "thunder sword",
        5 : "sword of darkness",
        6 : "sword of light",
        7 : "basic left sword",
        8 : "basic right sword",
        9 : "armor",
        10: "light spear",
        11: "spear of darkness",
        12: "fire canon",
        13: "water gun",
        14: "thunder hammer"
    }

    item_elements = {
        0 : 2,
        1 : 1,
        2 : 3,
        3 : 4,
        4 : 5,
        5 : 6,
        6 : 7,
        7 : 0,
        8 : 0,
        9 : 0,
        10: 7,
        11: 6,
        12: 2,
        13: 3,
        14: 5
    }

    item_types = {
        0 : 0,
        1 : 1,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 2,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0
    }

    item_damage = {
        0 : 50,
        1 : 30,
        2 : 50,
        3 : 40,
        4 : 50,
        5 : 60,
        6 : 60,
        7 : 40,
        8 : 40,
        9 : [1, 1, 1, 1, 1, 1, 1, 1],
        10: 30,
        11: 35,
        12: 40,
        13: 20,
        14: 50
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
        j = 0
        while added:
            item = rnd.randint(0, 14)
            if item not in list(self.inventory):
                self.inventory.append(item)
                added = False
                j = 0
            else:
                j += 1
                if j == 3:
                    added = -1
                    break
        
        if added != -1:
            print(self.items[item], "found!")
        else: 
            print("sadly the chest was empty.")
        time.sleep(2)

    def level_up(self):
        print("Level up!")
        self.maxhp = int(self.maxhp * 1.2)
        self.hp = int(self.hp * 1.2)
        self.lv += 1
        self.exp -= self.lvlup
        self.lvlup = int(self.lvlup * 1.2)
        self.dmg_mlt *= 1.1
        self.def_mlt *= 0.9
        