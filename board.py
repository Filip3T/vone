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
            elif a == 8:
                print("│", colored(" △△ ", "yellow"), end="", sep="")
            elif a == 9:
                print("│", colored(" ○○ ", "green"), end="", sep="")
            
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
    if player.state == 1:
        if enemy.enemy1 != 0:
            if cursor == 0:
                print(colored("1: ", "red"), colored(enemy.name[enemy.enemy1], "red"), colored(": ", "red"),
                       colored(enemy.hp1, "red"), colored("/", "red"), colored(enemy.maxhp1, "red"))
            else:
                print("1: ", enemy.name[enemy.enemy1], ": ", enemy.hp1, "/", enemy.maxhp1)
        if enemy.enemy2 != 0:
            if cursor == 1:
                print(colored("2: ", "red"), colored(enemy.name[enemy.enemy2], "red"), colored(": ", "red"),
                       colored(enemy.hp2, "red"), colored("/", "red"), colored(enemy.maxhp2, "red"))
            else:
                print("2: ", enemy.name[enemy.enemy2], ": ", enemy.hp2, "/", enemy.maxhp2)
        if enemy.enemy3 != 0:
            if cursor == 2:
                print(colored("3: ", "red"), colored(enemy.name[enemy.enemy3], "red"), colored(": ", "red"),
                       colored(enemy.hp3, "red"), colored("/", "red"), colored(enemy.maxhp3, "red"))
            else:
                print("3: ", enemy.name[enemy.enemy3], ": ", enemy.hp3, "/", enemy.maxhp3)
        if cursor == 3:
            print(colored("atak", "red"))
        else:
            print("atak")
        if cursor == 4:
            print(colored("bron magiczna", "red"))
        else:
            print("bron magiczna")
        if cursor == 5:
            print(colored("obrona", "red"))
        else:
            print("obrona")
        print(colored("HP: ", "green"), colored(player.hp, "green"), colored(" / ", "green"), colored(player.maxhp, "green"))
    if player.state == 2:
        if cursor == 0:
            print(enemy.name[enemy.enemy1], colored(enemy.hp1, "red"), colored(" / ", "red"),
                colored(enemy.maxhp1, "red"))
            print(colored("phys", "grey"), "│", colored("bow ", "grey"), "│", colored("fire", "red"), "│",
                colored("water", "light_blue"),"│", colored("wind", "green"),"│",
                colored("elec", "yellow"), "│",colored("dark", "magenta"),"│", colored("light", "white"))
            print("─────┼──────┼──────┼───────┼──────┼──────┼──────┼──────")
            print(enemy.weaknesses[enemy.rec1[0]],"│", enemy.weaknesses[enemy.rec1[1]],"│",
                enemy.weaknesses[enemy.rec1[2]],"│", enemy.weaknesses[enemy.rec1[3]], "","│",
                enemy.weaknesses[enemy.rec1[4]],"│", enemy.weaknesses[enemy.rec1[5]],"│",
                enemy.weaknesses[enemy.rec1[6]],"│", enemy.weaknesses[enemy.rec1[7]])
        if cursor == 1:
            print(enemy.name[enemy.enemy2], colored(enemy.hp2, "red"), colored(" / ", "red"),
                colored(enemy.maxhp2, "red"))
            print(colored("phys", "grey"), "│", colored("bow ", "grey"), "│", colored("fire", "red"), "│",
                colored("water", "light_blue"),"│", colored("wind", "green"),"│",
                colored("elec", "yellow"), "│",colored("dark", "magenta"),"│", colored("light", "white"))
            print("─────┼──────┼──────┼───────┼──────┼──────┼──────┼──────")
            print(enemy.weaknesses[enemy.rec2[0]],"│", enemy.weaknesses[enemy.rec2[1]],"│",
                enemy.weaknesses[enemy.rec2[2]],"│", enemy.weaknesses[enemy.rec2[3]], "","│",
                enemy.weaknesses[enemy.rec2[4]],"│", enemy.weaknesses[enemy.rec2[5]],"│",
                enemy.weaknesses[enemy.rec2[6]],"│", enemy.weaknesses[enemy.rec2[7]])
        if cursor == 2:
            print(enemy.name[enemy.enemy3], colored(enemy.hp3, "red"), colored(" / ", "red"),
                colored(enemy.maxhp3, "red"))
            print(colored("phys", "grey"), "│", colored("bow ", "grey"), "│", colored("fire", "red"), "│",
                colored("water", "light_blue"),"│", colored("wind", "green"),"│",
                colored("elec", "yellow"), "│",colored("dark", "magenta"),"│", colored("light", "white"))
            print("─────┼──────┼──────┼───────┼──────┼──────┼──────┼──────")
            print(enemy.weaknesses[enemy.rec3[0]],"│", enemy.weaknesses[enemy.rec3[1]],"│",
                enemy.weaknesses[enemy.rec3[2]],"│", enemy.weaknesses[enemy.rec3[3]], "","│",
                enemy.weaknesses[enemy.rec3[4]],"│", enemy.weaknesses[enemy.rec3[5]],"│",
                enemy.weaknesses[enemy.rec3[6]],"│", enemy.weaknesses[enemy.rec3[7]])
    if player.state == 3 or player.state == 9:
        if enemy.enemy1 != 0:
            if cursor == 0:
                print(colored("1: ", "red"), colored(enemy.name[enemy.enemy1], "red"), colored(": ", "red"),
                colored(enemy.hp1, "red"), colored("/", "red"), colored(enemy.maxhp1, "red"))
            else:
                print("1: ", enemy.name[enemy.enemy1], ": ", enemy.hp1, "/", enemy.maxhp1)
        if enemy.enemy2 != 0:
            if cursor == 1:
                print(colored("2: ", "red"), colored(enemy.name[enemy.enemy2], "red"), colored(": ", "red"),
                colored(enemy.hp2, "red"), colored("/", "red"), colored(enemy.maxhp2, "red"))
            else:
                print("2: ", enemy.name[enemy.enemy2], ": ", enemy.hp2, "/", enemy.maxhp2)
        if enemy.enemy3 != 0:
            if cursor == 2:
                print(colored("3: ", "red"), colored(enemy.name[enemy.enemy3], "red"), colored(": ", "red"),
                colored(enemy.hp3, "red"), colored("/", "red"), colored(enemy.maxhp3, "red"))
            else:
                print("3: ", enemy.name[enemy.enemy3], ": ", enemy.hp3, "/", enemy.maxhp3)
    

def menu(cursor):
    if cursor == 0:
        print(colored("equip", "red"))
    else:
        print("equip")
    if cursor == 1:
        print(colored("items", "red"))
    else:
        print("items")

def menueq(player, cursor):
    if cursor == 0:
        print(colored("sword 1:", "red"), end=" ")
        if player.eq1 != -1:
            print(player.items[player.eq1])
        else:
            print("")
    else:
        print("sword 1:", end=" ")
        if player.eq1 != -1:
            print(player.items[player.eq1])
        else:
            print("")
    if cursor == 1:
        print(colored("sword 2:", "red"), end=" ")
        if player.eq2 != -1:
            print(player.items[player.eq2])
        else:
            print("")
    else:
        print("sword 2:", end=" ")
        if player.eq2 != -1:
            print(player.items[player.eq2])
        else:
            print("")
    if cursor == 2:
        print(colored("bow:", "red"), end=" ")
        if player.eq3 != -1:
            print(player.items[player.eq3])
        else:
            print("")
    else:
        print("bow:", end=" ")
        if player.eq3 != -1:
            print(player.items[player.eq3])
        else:
            print("")

def equ(player, cursor, type):
    j = 0
    for i in player.inventory:
        if player.item_types[i] == type:
            if j == cursor:
                if player.item_elements[i] == 0 or player.item_elements[i] == 1:
                    print(colored(player.items[i], "grey"), end="")
                if player.item_elements[i] == 2:
                    print(colored(player.items[i], "red"), end="")
                if player.item_elements[i] == 3:
                    print(colored(player.items[i], "light_blue"), end="")
                if player.item_elements[i] == 4:
                    print(colored(player.items[i], "green"), end="")
                if player.item_elements[i] == 5:
                    print(colored(player.items[i], "yellow"), end="")
                if player.item_elements[i] == 6:
                    print(colored(player.items[i], "magenta"), end="")
                if player.item_elements[i] == 7:
                    print(colored(player.items[i], "white"), end="")
                print(" <<<")
            else:
                if player.item_elements[i] == 0 or player.item_elements[i] == 1:
                    print(colored(player.items[i], "grey"))
                if player.item_elements[i] == 2:
                    print(colored(player.items[i], "red"))
                if player.item_elements[i] == 3:
                    print(colored(player.items[i], "light_blue"))
                if player.item_elements[i] == 4:
                    print(colored(player.items[i], "green"))
                if player.item_elements[i] == 5:
                    print(colored(player.items[i], "yellow"))
                if player.item_elements[i] == 6:
                    print(colored(player.items[i], "magenta"))
                if player.item_elements[i] == 7:
                    print(colored(player.items[i], "white"))
            j += 1
    
        
def inv(player):
    for i in player.inventory:
        if player.item_elements[i] == 0 or player.item_elements[i] == 1:
            print(colored(player.items[i], "grey"))
        if player.item_elements[i] == 2:
            print(colored(player.items[i], "red"))
        if player.item_elements[i] == 3:
            print(colored(player.items[i], "light_blue"))
        if player.item_elements[i] == 4:
            print(colored(player.items[i], "green"))
        if player.item_elements[i] == 5:
            print(colored(player.items[i], "yellow"))
        if player.item_elements[i] == 6:
            print(colored(player.items[i], "magenta"))
        if player.item_elements[i] == 7:
            print(colored(player.items[i], "white"))
         

def invfgt(player, cursor):
    for i in [0, 1, 2]:
        if i == 0:
            eq = player.eq1
        elif i == 1:
            eq = player.eq2
        elif i == 2:
            eq = player.eq3
        if eq != -1:
            if player.item_elements[eq] == 0 or player.item_elements[eq] == 1:
                print(colored(player.items[eq], "grey"), end = " ")
            elif player.item_elements[eq] == 2:
                print(colored(player.items[eq], "red"), end = " ")
            elif player.item_elements[eq] == 3:
                print(colored(player.items[eq], "light_blue"), end = " ")
            elif player.item_elements[eq] == 4:
                print(colored(player.items[eq], "green"), end = " ")
            elif player.item_elements[eq] == 5:
                print(colored(player.items[eq], "yellow"), end = " ")
            elif player.item_elements[eq] == 6:
                print(colored(player.items[eq], "magenta"), end = " ")
            elif player.item_elements[eq] == 7:
                print(colored(player.items[eq], "white"), end = " ")
            if cursor == i:
                print("<<<")
            else:
                print("")

    