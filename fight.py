import os
import random as rnd
import board
from pynput import keyboard
import time


class enemies:

    name = {
        0: "none",
        1: "phoenix"
    }


    weaknesses = {
        0: "weak",
        1: "nrml",
        2: "strg"
    }

    enemy_attacks = {
        0 : "fire ball",
        1 : "blazing hell",
        2 : "fire from the sky",
        3 : "bite"
    }

    enemy_attacks_damage = {
        0 : 3,
        1 : 5,
        2 : 4,
        3 : 2
    }

    enemy_attacks_elements = {
        0 : 2,
        1 : 2,
        2 : 2,
        3 : 0,
    }

    exp_pull = 0

    enemy1 = 0
    hp1 = 0
    maxhp1 = 0
    rec1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    attacks1 = []

    enemy2 = 0
    hp2 = 0
    maxhp2 = 0
    rec2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    attacks2 = []

    enemy3 = 0
    hp3 = 0
    maxhp3 = 0
    rec3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    attacks3 = []

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
                    self.attacks1 = [0, 1, 2]
                    self.exp_pull += 10


            if i == 1:
                j = rnd.randint(1, 1)
                self.enemy2 = j
                if j == 1:
                    self.hp2 = 120
                    self.maxhp2 = 120
                    self.rec2 = [1, 0, 2, 0, 0, 2, 1, 1, 0]
                    self.attacks2 = [0, 1, 2]
                    self.exp_pull += 10

            if i == 2:
                j = rnd.randint(1, 1)
                self.enemy3 = j
                if j == 1:
                    self.hp3 = 120
                    self.maxhp3 = 120
                    self.rec3 = [1, 0, 2, 0, 0, 2, 1, 1, 1]
                    self.attacks3 = [0, 1, 2]
                    self.exp_pull += 10

enemy = 0
cursor = 0
selected = 0
weapon = 0
used = []

def fight(player):
    global enemy
    enemy = enemies()
    player.state = 1
    os.system('cls')
    board.battleUI(player, enemy, 0)

def enemy_turn(player):
    for i in [1, 2, 3]:
        do = False
        if i == 1:
            if enemy.enemy1 != 0:
                attack = rnd.choice(enemy.attacks1)
                do = True
                print(enemy.name[enemy.enemy1], "uses", enemy.enemy_attacks[attack], "dealing",
                      (enemy.enemy_attacks_damage[attack] * player.def_mlt), "DMG.", end=" ")
        elif i == 2:
            if enemy.enemy2 != 0:
                attack = rnd.choice(enemy.attacks2)
                do = True
                print(enemy.name[enemy.enemy2], "uses", enemy.enemy_attacks[attack], "dealing",
                      (enemy.enemy_attacks_damage[attack] * player.def_mlt), "DMG.", end=" ")
        elif i == 3:
            if enemy.enemy3 != 0:
                attack = rnd.choice(enemy.attacks3)
                do = True
                print(enemy.name[enemy.enemy3], "uses", enemy.enemy_attacks[attack], "dealing",
                      (enemy.enemy_attacks_damage[attack] * player.def_mlt), "DMG.", end=" ")
        if do:
            if player.item_damage[player.eq4][enemy.enemy_attacks_elements[attack]] == 0:
                player.hp -= enemy.enemy_attacks_damage[attack] * 1.5
                print("This attack was super effective boosting damage to ", 
                    (enemy.enemy_attacks_damage[attack] * player.def_mlt) * 1.5, "DMG.")
            if player.item_damage[player.eq4][enemy.enemy_attacks_elements[attack]] == 1:
                player.hp -= enemy.enemy_attacks_damage[attack]
            if player.item_damage[player.eq4][enemy.enemy_attacks_elements[attack]] == 2:
                player.hp -= enemy.enemy_attacks_damage[attack] * 0.5
                print("This attack wass't effective at all lowering the damage to",
                      (enemy.enemy_attacks_damage[attack] * player.def_mlt) * 0.5, "DMG")
            if player.hp <= 0:
                while True:
                    print("śmierć")
                    os.system('cls')
        time.sleep(1)
    time.sleep(5)
    


def fightupdate(player, prop, cords, Key):
    global cursor, enemy, selected, weapon, used
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
        elif player.state == 3 or player.state == 9:
            if cursor == 2 and enemy.enemy2 == 0:
                cursor -= 2
            elif cursor == 1 and enemy.enemy1 == 0:
                print("")
            else:
                if cursor != 0:
                    cursor -= 1
        elif player.state == 5:
            if cursor != 0:
                cursor -= 1
                os.system('cls')
                board.invfgt(player, cursor)
    elif Key == keyboard.Key.down:
        if player.state == 1:
            if cursor == 0 and enemy.enemy2 == 0:
                cursor += 1
            if cursor == 1 and enemy.enemy3 == 0:
                cursor = 3
            else:
                if cursor != 5:
                    cursor += 1
        elif player.state == 3 or player.state == 9:
            if cursor == 0 and enemy.enemy2 == 0:
                cursor += 1
                if enemy.enemy3 == 0:
                    cursor = 0
                else:
                    cursor +=1
            elif cursor == 1 and enemy.enemy3 == 0:
                None
            elif cursor == 2:
                None
            else:
                cursor += 1 
        elif player.state == 5:
            if cursor != 2:
                cursor += 1
                os.system('cls')
                board.invfgt(player, cursor)
        

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
            elif cursor == 4:
                player.state = 5
                os.system('cls')
                cursor = 0
                board.invfgt(player, cursor)
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
                        #win
                        player.state = 0
                        prop.death(cords)
                        print("You won gaining", enemy.exp_pull, "EXP. You feel your wounds magically healing themselves. You gained",
                              player.maxhp * 0.3, "HP back.")
                        player.exp += enemy.exp_pull
                        player.hp += player.maxhp * 0.3
                        if player.hp > player.maxhp:
                            player.hp = player.maxhp
                        if player.exp >= player.lvlup:
                            player.level_up()
                    else:
                        player.state = 1
                        enemy_turn(player)
                else:
                        player.state = 1
                        enemy_turn(player)
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
                        #win
                        player.state = 0
                        prop.death(cords)
                        print("You won gaining", enemy.exp_pull, "EXP. You feel your wounds magically healing themselves. You gained",
                              player.maxhp * 0.3, "HP back.")
                        player.exp += enemy.exp_pull
                        player.hp += player.maxhp * 0.3
                        if player.hp > player.maxhp:
                            player.hp = player.maxhp
                        if player.exp >= player.lvlup:
                            player.level_up()
                    else:
                        player.state = 1
                        enemy_turn(player)
                else:
                        player.state = 1
                        enemy_turn(player)
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
                        #win
                        player.state = 0
                        prop.death(cords)
                        print("You won gaining", enemy.exp_pull, "EXP. You feel your wounds magically healing themselves. You gained",
                              player.maxhp * 0.3, "HP back.")
                        player.exp += enemy.exp_pull
                        player.hp += player.maxhp * 0.3
                        if player.hp > player.maxhp:
                            player.hp = player.maxhp
                        if player.exp >= player.lvlup:
                            player.level_up()
                    else:
                        player.state = 1
                        enemy_turn(player)
                else:
                        player.state = 1
                        enemy_turn(player)
        elif player.state == 5:
            selected = cursor
            if selected == 0:
                weapon = player.eq1
            elif selected == 1:
                weapon = player.eq2
            elif selected == 2:
                weapon = player.eq3
            if weapon == -1 or weapon in used:
                if weapon in used:
                    print("you've already used this weapon in this combo.")
                    time.sleep(3)
                cursor = 1
                player.state = 1
                os.system('cls')
                board.battleUI(player, enemy, cursor)
                return None
            if enemy.enemy1 != 0:
                cursor = 0
            elif enemy.enemy2 != 0:
                cursor = 1
            else:
                cursor = 2
            player.state = 9
            os.system('cls')
            board.battleUI(player, enemy, cursor)
        elif player.state == 9:
            if cursor == 0:
                if enemy.rec1[player.item_elements[weapon]] == 0:
                    print("You used", player.items[weapon], "dealing", player.item_damage[weapon] * 1.5, 
                          "DMG. It was super effective granting you an additional turn.")
                    effect = 1
                    used.append(weapon)
                    time.sleep(3)
                    enemy.hp1 -= (player.item_damage[weapon] * 1.5)
                if enemy.rec1[player.item_elements[weapon]] == 1:
                    print("You used", player.items[weapon], "dealing", player.item_damage[weapon], "DMG.")
                    enemy.hp1 -= player.item_damage[weapon]
                    effect = 0
                    used = []
                if enemy.rec1[player.item_elements[weapon]] == 2:
                    print("You used", player.items[weapon], "dealing", player.item_damage[weapon] * 0.5, "DMG. It wasn't effective at all")
                    enemy.hp1 -= (player.item_damage[weapon] * 0.5)
                    effect = 0
                    used = []
                if enemy.hp1 <= 0:
                    enemy.enemy1 = 0
                    cursor = 3
                    if enemy.enemy3 == 0 and enemy.enemy2 == 0:
                        #win
                        player.state = 0
                        prop.death(cords)
                        print("You won gaining", enemy.exp_pull, "EXP. You feel your wounds magically healing themselves. You gained",
                              player.maxhp * 0.3, "HP back.")
                        player.exp += enemy.exp_pull
                        player.hp += player.maxhp * 0.3
                        if player.hp > player.maxhp:
                            player.hp = player.maxhp
                        if player.exp >= player.lvlup:
                            player.level_up()
                        return None
                    else:
                        player.state = 1
                        if effect != 1:
                            enemy_turn(player)
                else:
                        player.state = 1
                        if effect != 1:
                            enemy_turn(player)
            if cursor == 1:
                if enemy.rec2[player.item_elements[weapon]] == 0:
                    print("You used", player.items[weapon], "dealing", player.item_damage[weapon] * 1.5, 
                          "DMG. It was super effective granting you an additional turn.")
                    effect = 1
                    used.append(weapon)
                    time.sleep(3)
                    enemy.hp2 -= (player.item_damage[weapon] * 1.5)
                if enemy.rec2[player.item_elements[weapon]] == 1:
                    print("You used", player.items[weapon], "dealing", player.item_damage[weapon], "DMG.")
                    enemy.hp2 -= player.item_damage[weapon]
                    effect = 0
                    used = []
                if enemy.rec2[player.item_elements[weapon]] == 2:
                    print("You used", player.items[weapon], "dealing", player.item_damage[weapon] * 0.5, "DMG. It wasn't effective at all")
                    enemy.hp2 -= (player.item_damage[weapon] * 0.5)
                    effect = 0
                    used = []
                if enemy.hp2 <= 0:
                    enemy.enemy2 = 0
                    cursor = 3
                    if enemy.enemy1 == 0 and enemy.enemy3 == 0:
                        #win
                        player.state = 0
                        prop.death(cords)
                        print("You won gaining", enemy.exp_pull, "EXP. You feel your wounds magically healing themselves. You gained",
                              player.maxhp * 0.3, "HP back.")
                        player.exp += enemy.exp_pull
                        player.hp += player.maxhp * 0.3
                        if player.hp > player.maxhp:
                            player.hp = player.maxhp
                        if player.exp >= player.lvlup:
                            player.level_up()
                        return None
                    else:
                        player.state = 1
                        if effect != 1:
                            enemy_turn(player)
                else:
                        player.state = 1
                        if effect != 1:
                            enemy_turn(player)
            if cursor == 2:
                if enemy.rec3[player.item_elements[weapon]] == 0:
                    print("You used", player.items[weapon], "dealing", player.item_damage[weapon] * 1.5, 
                          "DMG. It was super effective granting you an additional turn.")
                    effect = 1
                    used.append(weapon)
                    time.sleep(3)
                    enemy.hp3 -= (player.item_damage[weapon] * 1.5)
                if enemy.rec3[player.item_elements[weapon]] == 1:
                    print("You used", player.items[weapon], "dealing", player.item_damage[weapon], "DMG.")
                    enemy.hp3 -= player.item_damage[weapon]
                    effect = 0
                    used = []
                if enemy.rec3[player.item_elements[weapon]] == 2:
                    print("You used", player.items[weapon], "dealing", player.item_damage[weapon] * 0.5, "DMG. It wasn't effective at all")
                    enemy.hp3 -= (player.item_damage[weapon] * 0.5)
                    effect = 0
                    used = []
                if enemy.hp3 <= 0:
                    enemy.enemy3 = 0
                if enemy.hp3 <= 0:
                    enemy.enemy3 = 0
                    cursor = 3
                    if enemy.enemy1 == 0 and enemy.enemy2 == 0:
                        #win
                        player.state = 0
                        prop.death(cords)
                        print("You won gaining", enemy.exp_pull, "EXP. You feel your wounds magically healing themselves. You gained",
                              player.maxhp * 0.3, "HP back.")
                        player.exp += enemy.exp_pull
                        player.hp += player.maxhp * 0.3
                        if player.hp > player.maxhp:
                            player.hp = player.maxhp
                        if player.exp >= player.lvlup:
                            player.level_up()
                        return None
                    else:
                        player.state = 1
                        if effect != 1:
                            enemy_turn(player)
                else:
                        player.state = 1
                        if effect != 1:
                            enemy_turn(player)
            os.system('cls')
            board.battleUI(player, enemy, cursor)
            
        #print("C")
    elif Key == keyboard.Key.ctrl_l:
        player.state = 1

    if player.state not in [0, 5]:
        os.system('cls')
        board.battleUI(player, enemy, cursor)
