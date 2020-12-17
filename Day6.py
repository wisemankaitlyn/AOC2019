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


for line in orbits:
    check_orbit(line[0])
    numOrbits = numOrbits + 1

print("part 1: number of orbits is: " + str(numOrbits))

# part 2
