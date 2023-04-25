from pynput import keyboard
#from pynput.keyboard import Key
import os
import board
import generate as gen
import random as rnd
import pathfinding as path

x = 15
y = 15
cords = [[1 for i in range(x)] for j in range(y)]
cords = gen.generation(cords, x, y)
print(cords)

pcords = [y - 1, 0]

notspawned = True
while notspawned:
    spawntryX = rnd.randint(0, x - 1)
    #print(cords[spawntryY][spawntryX])
    if cords[y - 1][spawntryX] == 0:
        pcords[1] = spawntryX
        #pcords[1] = cords[spawntryX]
        notspawned = False

#print(pcords)

pomoc = path.simplepathfinding([1, 1], [4, 6])

moves = 20
turn = True

#print(cords)

board.plansza(x, y, cords, moves)

def on_key_release(Key):
    global moves
    global turn
    if moves < 0:
        turn = False
        print("brak")
    else:
        if Key == Key.right:
            cords[pcords[0]][pcords[1]] = 0
            if pcords[1] + 1 >= x or cords[pcords[0]][pcords[1] + 1 ] == 1:
                print("nope")
            else:
                pcords[1] +=1
                cords[pcords[0]][pcords[1]] = 2
                os.system('cls')
                board.plansza(x, y, cords, moves)
                moves -= 1
        elif Key == Key.left:
            cords[pcords[0]][pcords[1]] = 0
            if pcords[1] - 1 < 0 or cords[pcords[0]][pcords[1] - 1 ] == 1:
                print("nope")
            else:
                pcords[1] -= 1
                cords[pcords[0]][pcords[1]] = 2
                os.system('cls')
                board.plansza(x, y, cords, moves)
                moves -= 1
        elif Key == Key.up:
            cords[pcords[0]][pcords[1]] = 0
            if pcords[0] - 1 < 0 or cords[pcords[0] - 1][pcords[1]] == 1:
                print("nope")
            else:
                pcords[0] -= 1
                cords[pcords[0]][pcords[1]] = 2
                os.system('cls')
                board.plansza(x, y, cords, moves)
                moves -= 1
        elif Key == Key.down:
            cords[pcords[0]][pcords[1]] = 0
            if pcords[0] + 1 >= y or cords[pcords[0] + 1][pcords[1]] == 1:
                print("nope")
            else:
                pcords[0] += 1
                cords[pcords[0]][pcords[1]] = 2
                os.system('cls')
                board.plansza(x, y, cords, moves)
                moves -= 1
            

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()

