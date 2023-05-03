from pynput import keyboard
#from pynput.keyboard import Key
import os
import board
import generate as gen
import random as rnd
import pathfinding as path
import enemy
import player as ply

x = rnd.randint(15, 18)
y = rnd.randint(18, 24)
cords = [[1 for i in range(x)] for j in range(y)]
cords = gen.generation(cords, x, y)
#print(cords)

player = ply.player()
player.spawn(x, y, cords)

#pcords = [y - 1, 0]
"""
notspawned = True
while notspawned:
    spawntryX = rnd.randint(0, x - 1)
    # print(cords[spawntryY][spawntryX])
    if cords[y - 1][spawntryX] == 0:
        pcords[1] = spawntryX
        cords[y - 1][spawntryX] = 3
        #pcords[1] = cords[spawntryX]
        notspawned = False
"""


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
    #global rooms
    global x
    global y
    global cords
    #global pcords
    global moves
    global left
    global en1
    global en2
    global en3
    left = 3
    moves = 8
    player.rooms += 1
    x = rnd.randint(15, 18)
    y = rnd.randint(18, 24)
    cords = [[1 for i in range(x)] for j in range(y)]
    cords = gen.generation(cords, x, y)

    #pcords = [y - 1, 0]
    player.spawn(x, y, cords)
    """
    notspawned = True
    while notspawned:
        spawntryX = rnd.randint(0, x - 1)
        #print(cords[spawntryY][spawntryX])
        if cords[y - 1][spawntryX] == 0:
            pcords[1] = spawntryX
            cords[y - 1][spawntryX] = 3
            #pcords[1] = cords[spawntryX]
            notspawned = False
    """

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

#board.plansza(x, y, cords, moves)

#check = path.complexpathfinding(tuple(punkt1), tuple(punkt2), cords)
#print(check)
#for i in check:
#    cords[i[0]][i[1]] = 3


#print(cords)

board.plansza(x, y, cords, moves, en1, en2, en3, player)

#path.complexpathfinding([0,0], [2, 2], cords)

def on_key_release(Key):
    global moves
    global turn
    global left
    global en1
    global en2
    global en3
    #global pcords
    if moves == 0:
        
        en1.tura(cords, player.pcords, x, y, moves, en1, en2, en3, player)
        
        en2.tura(cords, player.pcords, x, y, moves, en1, en2, en3, player)
        
        en3.tura(cords, player.pcords, x, y, moves, en1, en2, en3, player)
        moves += 8
        os.system('cls')
        board.plansza(x, y, cords, moves, en1, en2, en3, player)


    else:
        if Key == Key.right:
            cords[player.pcords[0]][player.pcords[1]] = left
            if player.pcords[1] + 1 >= x or cords[player.pcords[0]][player.pcords[1] + 1 ] == 1:
                print("nope")
            elif cords[player.pcords[0]][player.pcords[1] + 1 ] == 4:
                next()
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2, en3, player)
            else:
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
            elif cords[player.pcords[0]][player.pcords[1] - 1 ] == 4:
                next()
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2 ,en3, player)
            else:
                left = cords[player.pcords[0]][player.pcords[1] - 1]
                player.pcords[1] -= 1
                cords[player.pcords[0]][player.pcords[1]] = 2
                os.system('cls')
                moves -= 1
                board.plansza(x, y, cords, moves, en1, en2, en3, player)
        elif Key == Key.up:
            cords[player.pcords[0]][player.pcords[1]] = left
            if player.pcords[0] - 1 < 0 or cords[player.pcords[0] - 1][player.pcords[1]] == 1:
                 print("nope")
            elif cords[player.pcords[0] - 1][player.pcords[1]] == 4:
                next()
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2, en3, player)
            else:
                left = cords[player.pcords[0] - 1][player.pcords[1]]
                player.pcords[0] -= 1
                cords[player.pcords[0]][player.pcords[1]] = 2
                os.system('cls')
                moves -= 1
                board.plansza(x, y, cords, moves, en1, en2, en3, player)
        elif Key == Key.down:
            cords[player.pcords[0]][player.pcords[1]] = left
            if player.pcords[0] + 1 >= y or cords[player.pcords[0] + 1][player.pcords[1]] == 1:
                print("nope")
            elif cords[player.pcords[0] + 1][player.pcords[1]] == 4:
                next()
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2, en3, player)
            else:
                left = cords[player.pcords[0] + 1][player.pcords[1]]
                player.pcords[0] += 1
                cords[player.pcords[0]][player.pcords[1]] = 2
                os.system('cls')
                moves -= 1
                board.plansza(x, y, cords, moves, en1, en2, en3, player)
            

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()

