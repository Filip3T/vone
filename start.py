from pynput import keyboard
#from pynput.keyboard import Key
import os
import board
import generate as gen
import random as rnd
import pathfinding as path
import enemy

x = 18
y = 24
cords = [[1 for i in range(x)] for j in range(y)]
cords = gen.generation(cords, x, y)
print(cords)

pcords = [y - 1, 0]

notspawned = True
while notspawned:
    spawntryX = rnd.randint(0, x - 1)
    # print(cords[spawntryY][spawntryX])
    if cords[y - 1][spawntryX] == 0:
        pcords[1] = spawntryX
        cords[y - 1][spawntryX] = 3
        #pcords[1] = cords[spawntryX]
        notspawned = False



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
    global rooms
    global x
    global y
    global cords
    global pcords
    global moves
    global left
    global en1
    global en2
    global en3
    left = 3
    moves = 8
    rooms += 1
    x = 18
    y = 24
    cords = [[1 for i in range(x)] for j in range(y)]
    cords = gen.generation(cords, x, y)

    pcords = [y - 1, 0]

    notspawned = True
    while notspawned:
        spawntryX = rnd.randint(0, x - 1)
        #print(cords[spawntryY][spawntryX])
        if cords[y - 1][spawntryX] == 0:
            pcords[1] = spawntryX
            cords[y - 1][spawntryX] = 3
            #pcords[1] = cords[spawntryX]
            notspawned = False
    
    en1 = enemy.enemy("en1", 0)
    cords = en1.mapadd(cords, x, y)
        
    en2 = enemy.enemy("en2", 0)
    cords = en2.mapadd(cords, x, y)
        
    en3 = enemy.enemy("en3", 0)
    cords = en3.mapadd(cords, x, y)

help = cords[0].index(4)
punkt1 = [0, help]
punkt2 = pcords
notspawned = True

#board.plansza(x, y, cords, moves)

#check = path.complexpathfinding(tuple(punkt1), tuple(punkt2), cords)
#print(check)
#for i in check:
#    cords[i[0]][i[1]] = 3


#print(cords)

board.plansza(x, y, cords, moves, en1, en2, en3)

#path.complexpathfinding([0,0], [2, 2], cords)

def on_key_release(Key):
    global moves
    global turn
    global left
    global en1
    global en2
    global en3
    global pcords
    if moves <= 0:
        
        en1.tura(cords, pcords, x, y, moves, en1, en2, en3)
        
        en2.tura(cords, pcords, x, y, moves, en1, en2, en3)
        
        en3.tura(cords, pcords, x, y, moves, en1, en2, en3)
        moves += 8
        os.system('cls')
        board.plansza(x, y, cords, moves, en1, en2, en3)
    else:
        if Key == Key.right:
            cords[pcords[0]][pcords[1]] = left
            if pcords[1] + 1 >= x or cords[pcords[0]][pcords[1] + 1 ] == 1:
                print("nope")
            elif cords[pcords[0]][pcords[1] + 1 ] == 4:
                next()
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2, en3)
            else:
                left = cords[pcords[0]][pcords[1] + 1]
                pcords[1] += 1
                cords[pcords[0]][pcords[1]] = 2
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2, en3)
                moves -= 1
        elif Key == Key.left:
            cords[pcords[0]][pcords[1]] = left
            if pcords[1] - 1 < 0 or cords[pcords[0]][pcords[1] - 1 ] == 1:
                print("nope")
            elif cords[pcords[0]][pcords[1] - 1 ] == 4:
                next()
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2 ,en3)
            else:
                left = cords[pcords[0]][pcords[1] - 1]
                pcords[1] -= 1
                cords[pcords[0]][pcords[1]] = 2
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2, en3)
                moves -= 1
        elif Key == Key.up:
            cords[pcords[0]][pcords[1]] = left
            if pcords[0] - 1 < 0 or cords[pcords[0] - 1][pcords[1]] == 1:
                 print("nope")
            elif cords[pcords[0] - 1][pcords[1]] == 4:
                next()
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2, en3)
            else:
                left = cords[pcords[0] - 1][pcords[1]]
                pcords[0] -= 1
                cords[pcords[0]][pcords[1]] = 2
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2, en3)
                moves -= 1
        elif Key == Key.down:
            cords[pcords[0]][pcords[1]] = left
            if pcords[0] + 1 >= y or cords[pcords[0] + 1][pcords[1]] == 1:
                print("nope")
            elif cords[pcords[0] + 1][pcords[1]] == 4:
                next()
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2, en3)
            else:
                left = cords[pcords[0] + 1][pcords[1]]
                pcords[0] += 1
                cords[pcords[0]][pcords[1]] = 2
                os.system('cls')
                board.plansza(x, y, cords, moves, en1, en2, en3)
                moves -= 1
            

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()

