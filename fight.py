import os
import random as rnd
import board

class enemies:

    name = {
        0: "none",
        1: "phoenix"
    }

    elements = {
        0: "physical",
        1: "air",
        2: "fire",
        3: "water",
        4: "wind",
        5: "thunder",
        6: "magic",
        7: "night",
    }

    enemy1 = 0
    hp1 = 0
    maxhp1 = 0
    rec1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    enemy2 = 0
    hp2 = 0
    maxhp2 = 0
    rec2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    enemy3 = 0
    hp3 = 0
    maxhp3 = 0
    rec3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        x = rnd.randint(1, 3)
        for i in range(0, x):
            if i == 0:
                j = rnd.randint(1, 1)
                self.enemy1 = j
                if j == 1:
                    self.hp1 = 120
                    self.maxhp1 = 120
                    self.rect1 = [1, 0, 2, 0, 0, 2, 1, 1, 0]

            if i == 1:
                j = rnd.randint(1, 1)
                self.enemy2 = j
                if j == 1:
                    self.hp2 = 120
                    self.maxhp2 = 120
                    self.rect2 = [1, 0, 2, 0, 0, 2, 1, 1, 0]

            if i == 2:
                j = rnd.randint(1, 1)
                self.enemy3 = j
                if j == 1:
                    self.hp3 = 120
                    self.maxhp3 = 120
                    self.rect3 = [1, 0, 2, 0, 0, 2, 1, 1, 1]

enemy = 0
cursor = 0

def fight(player):
    global enemy
    enemy = enemies()
    player.state = 1
    board.battleUI(player, enemy, 0)
    
def fightupdate(player, Key):
    global cursor
    global enemy
    if Key == Key.up:
        if cursor == 3 and enemy.enemy3 == 0:
            if cursor == 3 and enemy.enemy2 == 0:
                cursor = 0
            else:
                cursor = 1
        else:
            if cursor != 0:
                cursor -= 1
    elif Key == Key.down:
        if enemy.enemy1 == 1 and enemy.enemy2 == 0 and cursor == 0:
            cursor = 3
        elif enemy.enemy2 == 1 and enemy.enemy3 == 0 and cursor == 1:
            cursor = 3
        else:
            if cursor != 6:
                cursor += 1
    if Key == Key.space:
        print(":D")
    #os.system('cls')
    board.battleUI(player, enemy, cursor)
