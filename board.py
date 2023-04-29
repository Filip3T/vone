from termcolor import colored

def plansza(x, y, cords, moves):
    i = 0
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
        print("│")
        i += 1
        if i == y:
            print("└────", (x - 1) * "┴────", "┘", sep="")
        else:
            print("├────", (x - 1) * "┼────", "┤", sep="")
