# day 2
# kaitlyn wiseman
# 12/02/2020

import csv
from copy import deepcopy

# part 1
intcode = csv.reader(open("Input\Day2.txt"), delimiter=',')

int_list = []
for val in intcode:
    for c in val:
        int_list.append(int(c))
list_copy = int_list.copy()  # set aside for part 2

int_list[1] = 12
int_list[2] = 2

index = 0
opcode = int_list[index]
while opcode != 99:
    if opcode == 1:
        int_list[int_list[index + 3]] = int_list[int_list[index + 1]] + int_list[int_list[index + 2]]
    else:
        int_list[int_list[index + 3]] = int_list[int_list[index + 1]] * int_list[int_list[index + 2]]
    index = index + 4
    opcode = int_list[index]

print("part 1: the value at index zero is: " + str(int_list[0]))
print()


# part 2
temp_list = list_copy.copy()

noun = 0
verb = -1

while temp_list[0] != 19690720:
    if verb == 99:
        noun += 1
        verb = 0
    else:
        verb += 1
    temp_list = list_copy.copy()
    temp_list[1] = noun
    temp_list[2] = verb

    index = 0
    opcode = temp_list[index]
    while opcode != 99:
        if opcode == 1:
            temp_list[temp_list[index + 3]] = temp_list[temp_list[index + 1]] + temp_list[temp_list[index + 2]]
        else:
            temp_list[temp_list[index + 3]] = temp_list[temp_list[index + 1]] * temp_list[temp_list[index + 2]]
        index = index + 4
        opcode = temp_list[index]


print("part 2: noun is " + str(noun) + ". verb is " + str(verb) + ".")
print(str(100 * noun + verb) + " is the answer.")
