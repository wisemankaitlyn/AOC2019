# day 6
# kaitlyn wiseman
# 12/12/2020

import csv

read = csv.reader(open("Input\Day6.txt", "r"), delimiter=')')
orbits = [[val1, val2] for val1, val2 in read]
numOrbits = 0


def check_orbit(planet):
    for ln in orbits:
        if planet == ln[1]:
            global numOrbits
            numOrbits = numOrbits + 1
            check_orbit(ln[0])
            break
    return


def transfers(index, orbiting, prevind):
    for x in range(len(orbits)):
        if x == index or x == prevind:
            continue
        if orbits[x][0] == orbits[index][orbiting]:
            if orbits[x][1] == 'SAN':
                return 0
            try:
                return transfers(x, 1, index) + 1
            except TypeError:
                continue
        if orbits[x][1] == orbits[index][orbiting]:
            if orbits[x][0] == 'SAN':
                return 0
            try:
                return transfers(x, 0, index) + 1
            except TypeError:
                continue
    return None


for line in orbits:
    check_orbit(line[0])
    numOrbits = numOrbits + 1

print("part 1: number of orbits is: " + str(numOrbits))

# part 2

for i in range(len(orbits)):
    if orbits[i][1] == "YOU":
        print("part 2: the minimum number of transfers from you to santa is " + str(transfers(i, 0, i)))
        break

