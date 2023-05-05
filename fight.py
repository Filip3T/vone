import os
import random as rnd
import board
from pynput import keyboard

class enemies:

    name = {
        0: "none",
        1: "phoenix"
    }

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

    weaknesses = {
        0: "weak",
        1: "nrml",
        2: "strg"
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
                    self.rec1 = [1, 0, 2, 0, 0, 2, 1, 1, 0]

            if i == 1:
                j = rnd.randint(1, 1)
                self.enemy2 = j
                if j == 1:
                    self.hp2 = 120
                    self.maxhp2 = 120
                    self.rec2 = [1, 0, 2, 0, 0, 2, 1, 1, 0]

            if i == 2:
                j = rnd.randint(1, 1)
                self.enemy3 = j
                if j == 1:
                    self.hp3 = 120
                    self.maxhp3 = 120
                    self.rec3 = [1, 0, 2, 0, 0, 2, 1, 1, 1]

enemy = 0
cursor = 0

def fight(player):
    global enemy
    enemy = enemies()
    player.state = 1
    os.system('cls')
    board.battleUI(player, enemy, 0)
    

def fightupdate(player, prop, cords, Key):
    global cursor
    global enemy
    if Key == keyboard.Key.up:
        if player.state == 1:
            if cursor == 3 and enemy.enemy3 == 0:
                cursor -= 1
            if cursor == 2 and enemy.enemy2 == 0:
                cursor -= 1
            if cursor == 1 and enemy.enemy1 == 0:
                cursor += 2
            else:
                if cursor != 0:
                    cursor -= 1
        elif player.state == 3:
            if cursor == 2 and enemy.enemy2 == 0:
                cursor -= 2
            else:
                if cursor != 0:
                    cursor -= 1
    elif Key == keyboard.Key.down:
        if player.state == 1:
            if cursor == 0 and enemy.enemy2 == 0:
                cursor += 1
            if cursor == 1 and enemy.enemy3 == 0:
                cursor = 3
            else:
                if cursor != 6:
                    cursor += 1
        elif player.state == 3:
            if cursor == 0 and enemy.enemy2 == 0:
                cursor += 1
                if enemy.enemy3 == 0:
                    cursor = 0
                else:
                    cursor +=1
            elif cursor == 1 and enemy.enemy3 == 0:
                None
            else:
                cursor += 1 

    elif Key == keyboard.Key.space:
        if player.state == 1:
            if cursor < 3:
                player.state = 2
            if cursor == 3:
                if enemy.enemy1 != 0:
                    cursor = 0
                elif enemy.enemy2 != 0:
                    cursor = 1
                if enemy.enemy3 != 0:
                    cursor = 2
                player.state = 3
        elif player.state == 3:
            if cursor == 0:
                if enemy.rec1[0] == 0:
                    enemy.hp1 -= 40
                elif enemy.rec1[0] == 1:
                    enemy.hp1 -= 30
                elif enemy.rec1[0] == 2:
                    enemy.hp1 -= 15
                if enemy.hp1 <= 0:
                    enemy.enemy1 = 0
                    cursor = 3
                    if enemy.enemy3 == 0 and enemy.enemy2 == 0:
                        print("win")
                        player.state = 0
                        prop.death(cords)
                    else:
                        player.state = 1
                else:
                        player.state = 1
            elif cursor == 1:
                if enemy.rec2[0] == 0:
                    enemy.hp2 -= 40
                elif enemy.rec2[0] == 1:
                    enemy.hp2 -= 30
                elif enemy.rec2[0] == 2:
                    enemy.hp2 -= 15
                if enemy.hp2 <= 0:
                    enemy.enemy2 = 0
                    cursor = 3
                    if enemy.enemy1 == 0 and enemy.enemy3 == 0:
                        print("win")
                        player.state = 0
                        prop.death(cords)
                    else:
                        player.state = 1
                else:
                        player.state = 1
            elif cursor == 2:
                if enemy.rec3[0] == 0:
                    enemy.hp3 -= 40
                elif enemy.rec3[0] == 1:
                    enemy.hp3 -= 30
                elif enemy.rec3[0] == 2:
                    enemy.hp3 -= 15
                if enemy.hp3 <= 0:
                    enemy.enemy3 = 0
                    cursor = 3
                    if enemy.enemy1 == 0 and enemy.enemy2 == 0:
                        print("win")
                        player.state = 0
                        prop.death(cords)
                    else:
                        player.state = 1
                else:
                        player.state = 1
                
        #print("C")
    elif Key == keyboard.Key.ctrl_l:
        player.state = 1

    os.system('cls')
    board.battleUI(player, enemy, cursor)
