# day 5
# kaitlyn wiseman
# 12/09/2020

import csv

filename = "Input\Day5.txt"

PART = 2
# part 1
intcode = csv.reader(open(filename), delimiter=',')

int_list = []
for val in intcode:
    for comm in val:
        int_list.append(int(comm))

index = 0
opcode = int_list[index]
add = 0
inst_input = 1
if PART == 2:
    inst_input = 5
inst_output = []
while opcode != 99:
    length = len(str(opcode))
    # opcode 1: adds together numbers read from two positions
    # and stores the result in the third position.
    if str(opcode).endswith('1'):
        if length == 2 or length == 1:  # all are in mode 0
            int_list[int_list[index + 3]] = int_list[int_list[index + 1]] + int_list[int_list[index + 2]]
        elif length == 3:  # p2 is in mode 0, p1 is in mode 1
            int_list[int_list[index + 3]] = int_list[index + 1] + int_list[int_list[index + 2]]
        elif length == 4:  # p2 is in mode 1, p1 is unknown
            if str(opcode)[1] == '1':
                int_list[int_list[index + 3]] = int_list[index + 1] + int_list[index + 2]
            else:
                int_list[int_list[index + 3]] = int_list[int_list[index + 1]] + int_list[index + 2]
        add = 4
    # opcode 2: multiplies together numbers read from two positions
    # and stores the result in the third position.
    elif str(opcode).endswith('2'):
        if length == 2 or length == 1:  # all are in mode 0
            int_list[int_list[index + 3]] = int_list[int_list[index + 1]] * int_list[int_list[index + 2]]
        elif length == 3:  # p2 is in mode 0, p1 is in mode 1
            int_list[int_list[index + 3]] = int_list[index + 1] * int_list[int_list[index + 2]]
        elif length == 4:  # p2 is in mode 1, p1 is unknown
            if str(opcode)[1] == '1':
                int_list[int_list[index + 3]] = int_list[index + 1] * int_list[index + 2]
            else:
                int_list[int_list[index + 3]] = int_list[int_list[index + 1]] * int_list[index + 2]
        add = 4
    # opcode 3: gets input and puts it at the position specified
    # in its parameter.
    elif str(opcode).endswith('3'):
        int_list[int_list[index + 1]] = inst_input
        add = 2
    # opcode 4: outputs whatever is at the position specified by
    # its parameter.
    elif str(opcode).endswith('4'):
        if length == 3:
            inst_output.append(int_list[index + 1])
        else:
            inst_output.append(int_list[int_list[index + 1]])
        add = 2
    # opcode 5: jump if true. if p1 != 0, then, index = value of p2
    # otherwise, it does nothing and just adds 3.
    elif str(opcode).endswith('5'):
        if length <= 2: # p1 and p2 in parameter mode
            if int_list[int_list[index + 1]] != 0:
                index = int_list[int_list[index + 2]]
                add = 0
            else:
                add = 3
        elif length == 3: # p1 in value mode, p2 in parameter mode
            if int_list[index + 1] != 0:
                index = int_list[int_list[index + 2]]
                add = 0
            else:
                add = 3
        elif length == 4: # p1 is uk, p2 in value mode
            if str(opcode)[1] == '1': # p1 in val mode
                if int_list[index + 1] != 0:
                    index = int_list[index + 2]
                    add = 0
                else:
                    add = 3
            else: # p1 in param mode
                if int_list[int_list[index + 1]] != 0:
                    index = int_list[index + 2]
                    add = 0
                else:
                    add = 3
    # opcode 6: jump if false. if p1 == 0, index = value indicated
    # by p2. otherwise, does nothing and add = 3.
    elif str(opcode).endswith('6'):
        if length <= 2:  # p1 and p2 in parameter mode
            if int_list[int_list[index + 1]] == 0:
                index = int_list[int_list[index + 2]]
                add = 0
            else:
                add = 3
        elif length == 3:  # p1 in value mode, p2 in parameter mode
            if int_list[index + 1] == 0:
                index = int_list[int_list[index + 2]]
                add = 0
            else:
                add = 3
        elif length == 4:  # p1 is uk, p2 in value mode
            if str(opcode)[1] == '1':  # p1 in val mode
                if int_list[index + 1] == 0:
                    index = int_list[index + 2]
                    add = 0
                else:
                    add = 3
            else:  # p1 in param mode
                if int_list[int_list[index + 1]] == 0:
                    index = int_list[index + 2]
                    add = 0
                else:
                    add = 3
    # opcode 7: less than. if p1 < p2, p3 = 1. else, p3 = 0.
    elif str(opcode).endswith('7'):
        if length <= 2:  # all p in param mode
            if int_list[int_list[index + 1]] < int_list[int_list[index + 2]]:
                int_list[int_list[index + 3]] = 1
            else:
                int_list[int_list[index + 3]] = 0
        elif length == 3:  # p1 in val mode, p2 in param mode
            if int_list[index + 1] < int_list[int_list[index + 2]]:
                int_list[int_list[index + 3]] = 1
            else:
                int_list[int_list[index + 3]] = 0
        elif length == 4:  # p1 uk, p2 in val mode
            if str(opcode)[1] == '1':  # p1 in val mode
                if int_list[index + 1] < int_list[index + 2]:
                    int_list[int_list[index + 3]] = 1
                else:
                    int_list[int_list[index + 3]] = 0
            else:  # p1 in param mode
                if int_list[int_list[index + 1]] < int_list[index + 2]:
                    int_list[int_list[index + 3]] = 1
                else:
                    int_list[int_list[index + 3]] = 0
        add = 4
    # opcode 8: equals. if p1 == p2, p3 = 1. else p3 = 0.
    elif str(opcode).endswith('8'):
        if length <= 2:  # all p in param mode
            if int_list[int_list[index + 1]] == int_list[int_list[index + 2]]:
                int_list[int_list[index + 3]] = 1
            else:
                int_list[int_list[index + 3]] = 0
        elif length == 3:  # p1 in val mode, p2 in param mode
            if int_list[index + 1] == int_list[int_list[index + 2]]:
                int_list[int_list[index + 3]] = 1
            else:
                int_list[int_list[index + 3]] = 0
        elif length == 4:  # p1 uk, p2 in val mode
            if str(opcode)[1] == '1':  # p1 in val mode
                if int_list[index + 1] == int_list[index + 2]:
                    int_list[int_list[index + 3]] = 1
                else:
                    int_list[int_list[index + 3]] = 0
            else:  # p1 in param mode
                if int_list[int_list[index + 1]] == int_list[index + 2]:
                    int_list[int_list[index + 3]] = 1
                else:
                    int_list[int_list[index + 3]] = 0
        add = 4
    index += add
    opcode = int_list[index]

for i in inst_output:
    print(i)
