import time
import math


ESC = "\x1b"
CSI = f"{ESC}["
res = f"{CSI}0m"
WHITE = "\u001b[47m"
BLACK = "\u001b[40m"
RED = '\u001b[41m'


def poland_flag(width = 20, height = 8):
    for y in range(1, height + 1):
        if y <= height // 2:
            print(f"{WHITE}{" " * width}")
        else:
            print(f"{RED}{" " * width}")
    print(f"{res}")


poland_flag()


def draw(width = 11, n = 4):
    line = " "
    center = width // 2
    center2 = width // 4
    height = 6
    for i in range(height + 1):
        if i == 1 or i == 3 or i == 5:
            print((f"{WHITE}{line*width}") * n)
        if i == 2:
            print((f"{res}{line * center}{WHITE}{line * 1}{res}{line * center}") * n)
        if i == 4:
            print((f"{res}{line * center2}{WHITE}"
                f'{line * 1}{res}{line * center2}{res}{line * 1}'
                f'{res}{line * center2}{WHITE}{line * 1}{res}{line * center2}') * n)
    print(f"{res}")


draw()


def graphic():
    WIDTH = 49
    HEIGHT = 9
    for i in range(HEIGHT, 0, -1):
        if i != 1:
            print(f'{i}{CSI}48;5;{0}m{"|"}{res}{" "*(i** 2)* 2}{CSI}48;5;{5}m{"*"}{res}')
            print(f'{" "}{CSI}48;5;{0}m{"|"}{res}')
        else:
            print(f'{i}{CSI}48;5;{0}m{"|"}{res}{" "*i**2}{CSI}48;5;{5}m{"*"}{res}')
            print(f'{" "}{CSI}48;5;{0}m{"|"}{"__"*WIDTH}{res}')
    print(f'{res}', end = '')
    for x in range(0, WIDTH+1):
        print(f'{" "}{x}', end = '')
    print(" ")


graphic()


def diagramma():   
    f = open("sequence.txt")
    numbers = []
    avg1 = 0
    avg2 = 0
    for line in f.readlines():
        numbers .append(abs(float(line)))
    for x in range(0,125):
        avg1 += numbers[x]
    for y in range(249,124,-1):
        avg2 += numbers[y]

    avg1 = avg1 / 125
    avg2 = avg2 / 125
    f.close()

    for i in range(100, 0, -1):
        if 100 > i > 51:
            print(f'{i}{CSI}48;5;{0}m{" |"}{BLACK}')
        if i == 100:
            print(f'{i}{CSI}48;5;{0}m{"|"}{BLACK}')
        if i == 51:
            for x in range(51,49,-1):  
                print(f'{x}{CSI}48;5;{0}m{" |"}{" "*16}{RED}{" "}{CSI}48;5;{0}m')
        if i == 49:
            for x in range(49,9,-1):   
                print(f'{x}{CSI}48;5;{0}m{" |"}{" "*4}{WHITE}{" "}'
                f'{CSI}48;5;{0}m{" "*11}{RED}{" "}{CSI}48;5;{0}m')
            for x in range(9,0,-1):
                print(f'{x}{CSI}48;5;{0}m{"  |"}{" "*4}{WHITE}{" "}'
                f'{CSI}48;5;{0}m{" "*11}{RED}{" "}{CSI}48;5;{0}m')
    print(f'{"0  |"}{"_"*20}')
    print(f'{BLACK}')
    print(f'{WHITE}{" "}{BLACK}{"- первые 125 чисел"}')
    print(f'{RED}{" "}{BLACK}{"- вторые 125 чисел"}')
    print(f'{res}')
    
    
diagramma()