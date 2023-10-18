# Bonus. Elementary Cellular Automaton:
import random
from colorama import Fore


def nextcell(a):
    if a == "111":
        return 0
    if a == "110":
        return 1
    if a == "101":
        return 1
    if a == "100":
        return 0
    if a == "011":
        return 1
    if a == "010":
        return 1
    if a == "001":
        return 1
    if a == "000":
        return 0


matrix = []
x = []
for i in range(8):
    x.append(random.randint(0, 1))
nextgen = []
prevgen = x
for i in range(0, len(prevgen)):
    prevgen[i] = int(prevgen[i])
print(prevgen)
for i in range(200):
    for j in range(8):
        if j == 0:
            nextgen.append(nextcell(str(0) + str(prevgen[0]) + str(prevgen[1])))
        elif j == 7:
            nextgen.append(nextcell(str(prevgen[6]) + str(prevgen[7]) + str(0)))
        else:
            nextgen.append(nextcell(str(prevgen[j-1]) + str(prevgen[j]) + str(prevgen[j+1])))
    matrix.append(nextgen)
    prevgen = nextgen
    nextgen = []

for i in range(len(matrix)):
    for j in range(8):
        if matrix[i][j] == 1:
            print(Fore.RED, matrix[i][j], end=' ')
        else:
            print(Fore.BLUE, matrix[i][j], end=' ')
    print()
