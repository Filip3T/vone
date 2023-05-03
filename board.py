from termcolor import colored

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
