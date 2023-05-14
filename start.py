from pynput import keyboard
import os
import board
import generate as gen
import random as rnd
import pathfinding as path
import enemy
import player as ply
import fight as fgt


x = rnd.randint(15, 18)
y = rnd.randint(18, 24)
cords = [[1 for i in range(x)] for j in range(y)]
cords = gen.generation(cords, x, y)

player = ply.player()
player.spawn(x, y, cords)

moves = 8
turn = True
left = 3
rooms = 0
en1 = enemy.enemy("en1", 0)
cords = en1.mapadd(cords, x, y)
en2 = enemy.enemy("en2", 0)
cords = en2.mapadd(cords, x, y)
en3 = enemy.enemy("en3", 0)
cords = en3.mapadd(cords, x, y)
 
def next():
    global x, y, cords, moves, left, en1, en2, en3

    left = 3
    moves = 8
    player.rooms += 1
    x = rnd.randint(15, 18)
    y = rnd.randint(18, 24)
    cords = [[1 for i in range(x)] for j in range(y)]
    cords = gen.generation(cords, x, y)

    player.spawn(x, y, cords)

    en1 = enemy.enemy("en1", 0)
    cords = en1.mapadd(cords, x, y)
        
    en2 = enemy.enemy("en2", 0)
    cords = en2.mapadd(cords, x, y)
        
    en3 = enemy.enemy("en3", 0)
    cords = en3.mapadd(cords, x, y)

help = cords[0].index(4)
punkt1 = [0, help]
punkt2 = player.pcords
notspawned = True


board.plansza(x, y, cords, moves, en1, en2, en3, player)
    
frop = 0
cursor = 0
types = 0
eq = 0  
selected = -1
list_types = []

def  on_key_release(Key):
    global eq, types, moves, turn, left, en1, en2, en3, frop, cursor, selected, list_types
    if player.state in [0, 4, 6, 7, 8]:
        if moves == 0:
            if en1 != None:
                e1 = en1.tura(cords, player.pcords, x, y, moves, en1, en2, en3, player)
                if e1 == "fight":
                    frop = en1
                    return None
            if en2 != None:
                e2 = en2.tura(cords, player.pcords, x, y, moves, en1, en2, en3, player)
                if e2 == "fight":
                    frop = en2
                    return None
            if en3 != None:
                e3 = en3.tura(cords, player.pcords, x, y, moves, en1, en2, en3, player)
                if e3 == "fight":
                    frop = en3
                    return None
            if en1 != None:    
                en1.moves = 4
            if en2 != None:
                en2.moves = 4
            if en3 != None:    
                en3.moves = 4
            moves += 8
            os.system('cls')
            board.plansza(x, y, cords, moves, en1, en2, en3, player)
 

        else:
            if Key == Key.right:
                cords[player.pcords[0]][player.pcords[1]] = left
                if player.pcords[1] + 1 >= x or cords[player.pcords[0]][player.pcords[1] + 1 ] == 1:
                    print("nope")
                elif cords[player.pcords[0]][player.pcords[1] + 1 ] == 5:
                    frop = en1
                    fgt.fight(player)
                elif cords[player.pcords[0]][player.pcords[1] + 1 ] == 6:
                    frop = en2
                    fgt.fight(player)
                elif cords[player.pcords[0]][player.pcords[1] + 1 ] == 7:
                    frop = en3
                    fgt.fight(player)
                elif cords[player.pcords[0]][player.pcords[1] + 1 ] == 4:
                    next()
                    os.system('cls')
                    board.plansza(x, y, cords, moves, en1, en2, en3, player)
                else:
                    if cords[player.pcords[0]][player.pcords[1] + 1] == 8:
                        player.itemfound()
                        cords[player.pcords[0]][player.pcords[1] + 1] = 0
                    elif cords[player.pcords[0]][player.pcords[1] + 1] == 9:
                        player.hp += 25
                        if player.hp > player.maxhp:
                            player.hp = player.maxhp
                        cords[player.pcords[0]][player.pcords[1] + 1] = 0
                    left = cords[player.pcords[0]][player.pcords[1] + 1]
                    player.pcords[1] += 1
                    cords[player.pcords[0]][player.pcords[1]] = 2
                    os.system('cls')
                    moves -= 1
                    board.plansza(x, y, cords, moves, en1, en2, en3, player)
            elif Key == Key.left:
                cords[player.pcords[0]][player.pcords[1]] = left
                if player.pcords[1] - 1 < 0 or cords[player.pcords[0]][player.pcords[1] - 1 ] == 1:
                    print("nope")
                elif cords [player.pcords[0]][player.pcords[1] - 1 ] == 5:
                    frop = en1
                    fgt.fight(player)
                elif cords[player.pcords[0]][player.pcords[1] - 1 ] == 6:
                    frop = en2
                    fgt.fight(player)
                elif cords[player.pcords[0]][player.pcords[1] - 1 ] == 7:
                    frop = en3
                    fgt.fight(player)
                elif cords[player.pcords[0]][player.pcords[1] - 1 ] == 4:
                    next( )
                    os.system('cls')
                    board.plansza(x, y, cords, moves, en1, en2 ,en3, player)
                else:
                    if cords[player.pcords[0]][player.pcords[1] - 1 ] == 8:
                        player.itemfound()
                        cords[player.pcords[0]][player.pcords[1] - 1 ] = 0
                    elif cords[player.pcords[0]][player.pcords[1] - 1 ] == 9:
                        player.hp += 25
                        cords[player.pcords[0]][player.pcords[1] - 1 ] = 0
                        if player.hp > player.maxhp:
                            player.hp = player.maxhp
                    left = cords[ player.pcords[0]][player.pcords[1] - 1]
                    player.pcords[1] -= 1
                    cords[player.pcords[0]][player.pcords[1]] = 2
                    os.system('cls')
                    moves -= 1
                    board.plansza(x, y, cords, moves, en1, en2, en3, player)
            elif Key == Key.up:
                if player.state == 0:
                    cords[player.pcords[0]][player.pcords[1]] = left
                    if player.pcords[0] - 1 < 0 or cords[player.pcords[0] - 1][player.pcords[1]] == 1:
                        print("nope")
                    elif cords[player.pcords[0] - 1][player.pcords[1]] == 5:
                        frop = en1
                        fgt.fight(player)
                    elif cords[player.pcords[0] - 1][player.pcords[1]] == 6:
                        frop = en2
                        fgt.fight(player)
                    elif cords[player.pcords[0] - 1][player.pcords[1]] == 7:
                        frop = en3
                        fgt.fight(player)
                    elif cords[player.pcords[0] - 1][player.pcords[1]] == 4:
                        next()
                        os.system('cls')
                        board.plansza(x, y, cords, moves, en1, en2, en3, player)
                    else:
                        if cords[player.pcords[0] - 1][player.pcords[1]] == 8:
                            player.itemfound()
                            cords[player.pcords[0] - 1][player.pcords[1]] = 0
                        elif cords[player.pcords[0] - 1][player.pcords[1]] == 9:
                            player.hp += 25
                            cords[player.pcords[0] - 1][player.pcords[1]] = 0
                            if player.hp > player.maxhp:
                                player.hp = player.maxhp
                        left = cords[player.pcords[0] - 1][player.pcords[1]]
                        player.pcords[0] -= 1
                        cords[player.pcords[0]][player.pcords[1]] = 2
                        os.system('cls')
                        moves -= 1
                        board.plansza(x, y, cords, moves, en1, en2, en3, player)
                elif player.state == 4:
                    cursor = 0 
                    os.system('cls')
                    board.menu(cursor) 
                elif player.state == 6:
                    if cursor != 0:
                        cursor -= 1
                        os.system('cls')
                        board.menueq(player, cursor)
                elif player.state == 8:
                    if cursor != 0:  
                        cursor -= 1
                        selected = list_types[cursor]
                        os.system('cls')
                        board.equ(player, cursor, types)
            elif Key == Key.down: 
                if player.state == 0:
                    cords[player.pcords[0]][player.pcords[1]] = left
                    if  player.pcords[0] + 1 >= y or cords[player.pcords[0] + 1][player.pcords[1]] == 1:
                        print("nope")
                    elif cords[player.pcords[0] + 1][player.pcords[1]] == 5:
                        frop = en1
                        fgt.fight(player)
                    elif cords[player.pcords[0] + 1][player.pcords[1]] == 6:
                        frop = en2
                        fgt.fight(player)
                    elif cords[player.pcords[0] + 1][player.pcords[1]] == 7:
                        frop = en3
                        fgt.fight(player)
                    elif cords[player.pcords[0] + 1][player.pcords[1]] == 4:
                        next()
                        os.system('cls')
                        board.plansza(x, y, cords, moves, en1, en2, en3, player)
                    else:
                        if cords[player.pcords[0] + 1][player.pcords[1]] == 8:
                            player.itemfound()
                            cords[player.pcords[0] + 1][player.pcords[1]] = 0
                        elif cords[player.pcords[0] + 1][player.pcords[1]] == 9:
                            player.hp += 25
                            cords[player.pcords[0] + 1][player.pcords[1]] = 0
                            if player.hp > player.maxhp:
                                player.hp = player.maxhp
                        left = cords[player.pcords[0] + 1][player.pcords[1]]
                        player.pcords[0] += 1
                        cords[player.pcords[0]][player.pcords[1]] = 2
                        os.system('cls')
                        moves -= 1
                        board.plansza(x, y, cords, moves, en1, en2, en3, player)
                elif player.state == 4:
                    cursor = 1
                    os.system('cls')
                    board.menu(cursor)
                elif player.state == 6:
                    if cursor != 2:
                        cursor += 1
                        os.system('cls')
                        board.menueq(player, cursor)
                elif player.state ==    8:
                    if cursor != len(list_types) - 1:
                        cursor += 1
                        selected = list_types[cursor]
                        os.system('cls')
                        board.equ(player, cursor, types)
            elif Key == Key.space:
                if player.state == 0:
                    player.state = 4
                    cursor = 0
                    os.system('cls')
                    board.menu(cursor)
                elif player.state == 4:
                    if cursor == 0:
                        player.state = 6
                        os.system('cls')
                        board.menueq(player, cursor)
                    elif cursor == 1:
                        player.state = 7
                        os.system('cls')
                        board.inv(player)
                elif player.state == 6:
                    player.state = 8
                    if cursor == 0 or cursor == 1:
                        os.system('cls')
                        types = 0
                        list_types = []
                        for i in player.inventory:
                            if player.item_types[i] == types:
                                list_types.append(i) 
                        eq = cursor
                        selected = list_types[0]
                        cursor = 0
                        board.equ(player, cursor, types)
                    elif cursor == 2:
                        os.system('cls')
                        types = 1
                        list_types = []
                        for i in player.inventory:
                            if player.item_types[i] == types:
                                list_types.append(i) 
                        eq = cursor
                        selected = list_types[0]
                        cursor = 0
                        board.equ(player, cursor, types)
                elif player.state == 8:
                    if eq == 0:
                        if player.eq2 != selected:
                            player.eq1 = selected
                    elif eq == 1:
                        if player.eq1 != selected:
                            player.eq2 = selected
                    elif eq == 2:
                        player.eq3 = selected
            elif Key == keyboard.Key.ctrl_l:
                if player.state == 7 or player.state == 6:
                    player.state = 4
                    os.system('cls')
                    board.menu(cursor)
                elif player.state == 4:
                    player.state = 0
                    os.system('cls')
                    board.plansza(x, y, cords, moves, en1, en2, en3, player)
                elif player.state == 8:
                    player.state = 6
                    os.system('cls')
                    cursor = 0
                    board.menueq(player, cursor)
                
    else:
        fgt.fightupdate(player, frop, cords, Key)
          
 
with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()