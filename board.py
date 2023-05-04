from termcolor import colored
import fight

def plansza(x, y, cords, moves, en1, en2, en3, player):
    i = 0

    print(colored("Room: ", "red"), colored(player.rooms, "red"))

    print("┌────", (x - 1) * "┬────", "┐", sep="")
    for row in cords:
        for a in row: 
            #print("│ ", end="")
            if a == 0:
                print("│    ", end="")
            elif a == 1:
                print("│████", end="")
            elif a == 2:
                if moves >= 10:
                    print("│ ",colored(moves, "blue"), end=" ", sep="")
                else:
                    print("│  ", colored(moves, "blue"), end=" ", sep="")
            elif a == 3:
                print("│", colored(" ██ ", "blue"), end="", sep="")
            elif a == 4:
                print("│", colored(" ██ ", "red"), end="", sep="")
            elif a == 5:
                if en1.moves >= 10:
                    print("│ ",colored(en1.moves, "red"), end=" ", sep="")
                else:
                    print("│  ", colored(en1.moves, "red"), end=" ", sep="")
            elif a == 6:
                if en2.moves >= 10:
                    print("│ ",colored(en2.moves, "red"), end=" ", sep="")
                else:
                    print("│  ", colored(en2.moves, "red"), end=" ", sep="")
            elif a == 7:
                if en3.moves >= 10:
                    print("│ ",colored(en3.moves, "red"), end=" ", sep="")
                else:
                    print("│  ", colored(en3.moves, "red"), end=" ", sep="")
                #print("│", colored(" 11 ", "red"), end="", sep="")
            
        print("│")
        i += 1
        if i == y:
            print("└────", (x - 1) * "┴────", "┘", sep="")
        else:
            print("├────", (x - 1) * "┼────", "┤", sep="")
    
  
    print(colored("HP: ", "green"), colored(player.hp, "green"), colored(" / ", "green"), colored(player.maxhp, "green"))
    print(colored("EXP: ", "yellow"), colored(player.exp, "yellow"), colored(" / ", "yellow"), colored(player.lvlup, "yellow"))
    print(colored("LVL: ", "cyan"), colored(player.lv, "cyan"))

def battleUI(player, enemy, cursor):
    if enemy.enemy1 == 1:
        if cursor == 0:
            print(colored("1: ", "red"), colored(enemy.name[enemy.enemy1], "red"), colored(": ", "red"), colored(enemy.maxhp1, "red"), colored("/", "red"), colored(enemy.hp1, "red"))
        else:
            print("1: ", enemy.name[enemy.enemy1], ": ", enemy.maxhp1, "/", enemy.hp1)
    if enemy.enemy2 == 1:
        if cursor == 1:
            print(colored("2: ", "red"), colored(enemy.name[enemy.enemy2], "red"), colored(": ", "red"), colored(enemy.maxhp2, "red"), colored("/", "red"), colored(enemy.hp2, "red"))
        else:
            print("2: ", enemy.name[enemy.enemy2], ": ", enemy.maxhp2, "/", enemy.hp2)
    if enemy.enemy3 == 1:
        if cursor == 2:
            print(colored("3: ", "red"), colored(enemy.name[enemy.enemy3], "red"), colored(": ", "red"), colored(enemy.maxhp3, "red"), colored("/", "red"), colored(enemy.hp3, "red"))
        else:
            print("3: ", enemy.name[enemy.enemy3], ": ", enemy.maxhp3, "/", enemy.hp3)
    if cursor == 3:
        print(colored("attack", "red"))
    else:
        print("attack")
    if cursor == 4:
        print(colored("weapon", "red"))
    else:
        print("weapon")
    if cursor == 5:
        print(colored("item", "red"))
    else:
        print("item")
    if cursor == 6:
        print(colored("defence", "red"))
    else:
        print("defence")