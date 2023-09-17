import os
from time import sleep
from gospergun import gospergun

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def evolveField(field):
    nextField = []
    for rowIndex in range(len(field)):
        row = []
        for cellIndex in range(len(field[rowIndex])):
            newCellValue = evolveCell(field, rowIndex, cellIndex)
            row.append(newCellValue)
        nextField.append(row)
    return nextField

def evolveCell(field, x, y):
    neighborCount = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i>=0 and i<len(field) and j>=0 and j<len(field[x]) and (i != x or j != y):
                neighborCount+=field[i][j]
    if neighborCount == 3:
        return 1
    elif neighborCount == 2 and field[x][y] == 1:
        return 1
    else:
        return 0

def printField(field):
    for row in field:
        for cell in row:
            if cell == 0:
                print("░░", end='')
            if cell == 1:
                print("▓▓", end='')
        print()
    return

def runGame(field):
    while True:
        cls()
        field = evolveField(field)
        printField(field)
        sleep(0.2)

blinker = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
    ]

cls()
runGame(gospergun)