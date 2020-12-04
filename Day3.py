# day 3
# kaitlyn wiseman
# 12/03/2020

import csv

wire_in = csv.reader(open("Input\Day3.txt"), delimiter=',')

wire1 = []
wire2 = []
index = 0
for line in wire_in:
    for val in line:
        wire1.append([val[0], val[1:len(val)]])
    break
for line in wire_in:
    for val in line:
        wire2.append([val[0], val[1:len(val)]])

wire1_path = []
current_spot = [0, 0]


for pair in wire1:
    if pair[0] == "R":
        temp = int(pair[1])
        while temp > 0:
            wire1_path.append(current_spot.copy())
            current_spot[0] += 1
            temp -= 1
    elif pair[0] == "L":
        temp = int(pair[1])
        while temp > 0:
            wire1_path.append(current_spot.copy())
            current_spot[0] -= 1
            temp -= 1
    elif pair[0] == "U":
        temp = int(pair[1])
        while temp > 0:
            wire1_path.append(current_spot.copy())
            current_spot[1] += 1
            temp -= 1
    elif pair[0] == "D":
        temp = int(pair[1])
        while temp > 0:
            wire1_path.append(current_spot.copy())
            current_spot[1] -= 1
            temp -= 1


wire2_path = []
current_spot = [0, 0]

for pair in wire2:
    if pair[0] == "R":
        temp = int(pair[1])
        while temp > 0:
            wire2_path.append(current_spot.copy())
            current_spot[0] += 1
            temp -= 1
    elif pair[0] == "L":
        temp = int(pair[1])
        while temp > 0:
            wire2_path.append(current_spot.copy())
            current_spot[0] -= 1
            temp -= 1
    elif pair[0] == "U":
        temp = int(pair[1])
        while temp > 0:
            wire2_path.append(current_spot.copy())
            current_spot[1] += 1
            temp -= 1
    elif pair[0] == "D":
        temp = int(pair[1])
        while temp > 0:
            wire2_path.append(current_spot.copy())
            current_spot[1] -= 1
            temp -= 1


current_spot = [0, 0]
intersections = []

for pair in wire2_path:
    try:
        wire1_path.index(pair)
        intersections.append(pair.copy())
    except ValueError:
        continue


intersections.remove([0, 0])
small_dist = abs(intersections[0][0]) + abs(intersections[0][1])

for pair in intersections:
    if small_dist > abs(pair[0]) + abs(pair[1]):
        small_dist = abs(pair[0]) + abs(pair[1])

print("part 1: the smallest distance is: " + str(small_dist))

# part 2
short_dist = wire1_path.index(intersections[0]) + wire2_path.index(intersections[0])

for pair in intersections:
    if short_dist > wire1_path.index(pair) + wire2_path.index(pair):
        short_dist = wire1_path.index(pair) + wire2_path.index(pair)

print("part 2: the shortest distance is: " + str(short_dist))
