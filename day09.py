# day 09
# kaitlyn wiseman
# 01/01/2021

import csv
filename = "Input/Day09.txt"
intcode = csv.reader(open(filename), delimiter=',')


# parameter mode 0: position mode
#   the parameter is interpreted as a position. if the parameter is 50, its value is the value stored at address 50 in
#   memory.
# parameter mode 1: immediate mode
#   the parameter is interpreted as a value. if the parameter is 50, its value is simply 50.
# parameter mode 2: relative mode
#   behaves like 0: position mode, but the parameters count from the relative base, not 0. if the parameter is 50 and
#   the relative base is -7, then its value is the value stored at address (50 + -7 = ) 43.

def opcode_compute(int_list, inst_input, start_index):
    for n in range(10000000):
        int_list.append(0)
    inst_output = []
    rel_base = 0
    index = start_index
    opcode = int_list[index]
    while opcode != 99:
        length = len(str(opcode))
        # opcode 1: adds together numbers read from two positions
        # and stores the result in the third position.
        if str(opcode).endswith('1'):
            if length == 2 or length == 1:  # all are in mode 0
                int_list[int_list[index + 3]] = int_list[int_list[index + 1]] + int_list[int_list[index + 2]]
            elif length == 3:  # p2 is in mode 0, p1 is uk
                if str(opcode)[0] == '1':  # p1 in mode 1
                    int_list[int_list[index + 3]] = int_list[index + 1] + int_list[int_list[index + 2]]
                elif str(opcode)[0] == '2':  # p1 in mode 2
                    int_list[int_list[index + 3]] = int_list[int_list[index + 1] + rel_base] \
                                                    + int_list[int_list[index + 2]]
            elif length == 4:  # p1 is unknown; p2 is unknown but NOT mode 0
                if str(opcode)[0] == '1':  # p2 in mode 1
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        int_list[int_list[index + 3]] = int_list[int_list[index + 1]] + int_list[index + 2]
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        int_list[int_list[index + 3]] = int_list[index + 1] + int_list[index + 2]
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        int_list[int_list[index + 3]] = int_list[int_list[index + 1] + rel_base] + int_list[index + 2]
                elif str(opcode)[0] == '2':  # p2 in mode 2
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        int_list[int_list[index + 3]] = int_list[int_list[index + 1]] \
                                                        + int_list[int_list[index + 2] + rel_base]
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        int_list[int_list[index + 3]] = int_list[index + 1] + int_list[int_list[index + 2] + rel_base]
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        int_list[int_list[index + 3]] = int_list[int_list[index + 1] + rel_base] \
                                                        + int_list[int_list[index + 2] + rel_base]
            elif length == 5:
                if str(opcode)[0] == '2':  # p3 in mode 2
                    if str(opcode)[1] == '0':  # p2 in mode 0
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1]] \
                                                                       + int_list[int_list[index + 2]]
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            int_list[int_list[index + 3] + rel_base] = int_list[index + 1] \
                                                                       + int_list[int_list[index + 2]]
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1] + rel_base] \
                                                                       + int_list[int_list[index + 2]]
                    elif str(opcode)[1] == '1':  # p2 in mode 1
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1]] \
                                                                       + int_list[index + 2]
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            int_list[int_list[index + 3] + rel_base] = int_list[index + 1] + int_list[index + 2]
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1] + rel_base] \
                                                                       + int_list[index + 2]
                    elif str(opcode)[1] == '2':  # p2 in mode 2
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1]] \
                                                                       + int_list[int_list[index + 2] + rel_base]
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            int_list[int_list[index + 3] + rel_base] = int_list[index + 1] \
                                                                       + int_list[int_list[index + 2] + rel_base]
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1] + rel_base] \
                                                                       + int_list[int_list[index + 2] + rel_base]
            add = 4
        # opcode 2: multiplies together numbers read from two positions
        # and stores the result in the third position.
        elif str(opcode).endswith('2'):
            if length == 2 or length == 1:  # all are in mode 0
                int_list[int_list[index + 3]] = int_list[int_list[index + 1]] * int_list[int_list[index + 2]]
            elif length == 3:  # p2 is in mode 0, p1 is uk
                if str(opcode)[0] == '1':  # p1 in mode 1
                    int_list[int_list[index + 3]] = int_list[index + 1] * int_list[int_list[index + 2]]
                elif str(opcode)[0] == '2':  # p1 in mode 2
                    int_list[int_list[index + 3]] = int_list[int_list[index + 1] + rel_base] \
                                                    * int_list[int_list[index + 2]]
            elif length == 4:  # p1 is unknown; p2 is unknown but NOT mode 0
                if str(opcode)[0] == '1':  # p2 in mode 1
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        int_list[int_list[index + 3]] = int_list[int_list[index + 1]] * int_list[index + 2]
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        int_list[int_list[index + 3]] = int_list[index + 1] * int_list[index + 2]
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        int_list[int_list[index + 3]] = int_list[int_list[index + 1] + rel_base] * int_list[index + 2]
                elif str(opcode)[0] == '2':  # p2 in mode 2
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        int_list[int_list[index + 3]] = int_list[int_list[index + 1]] \
                                                        * int_list[int_list[index + 2] + rel_base]
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        int_list[int_list[index + 3]] = int_list[index + 1] * int_list[int_list[index + 2] + rel_base]
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        int_list[int_list[index + 3]] = int_list[int_list[index + 1] + rel_base] \
                                                        * int_list[int_list[index + 2] + rel_base]
            elif length == 5:
                if str(opcode)[0] == '2':  # p3 in mode 2
                    if str(opcode)[1] == '0':  # p2 in mode 0
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1]] \
                                                                       * int_list[int_list[index + 2]]
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            int_list[int_list[index + 3] + rel_base] = int_list[index + 1] \
                                                                       * int_list[int_list[index + 2]]
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1] + rel_base] \
                                                                       * int_list[int_list[index + 2]]
                    elif str(opcode)[1] == '1':  # p2 in mode 1
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1]] \
                                                                       * int_list[index + 2]
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            int_list[int_list[index + 3] + rel_base] = int_list[index + 1] * int_list[index + 2]
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1] + rel_base] \
                                                                       * int_list[index + 2]
                    elif str(opcode)[1] == '2':  # p2 in mode 2
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1]] \
                                                                       * int_list[int_list[index + 2] + rel_base]
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            int_list[int_list[index + 3] + rel_base] = int_list[index + 1] \
                                                                       * int_list[int_list[index + 2] + rel_base]
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            int_list[int_list[index + 3] + rel_base] = int_list[int_list[index + 1] + rel_base] \
                                                                       * int_list[int_list[index + 2] + rel_base]
            add = 4
        # opcode 3: gets input and puts it at the position specified
        # in its parameter.
        elif str(opcode).endswith('3'):
            if length <= 2:  # p1 in mode 0
                int_list[int_list[index + 1]] = inst_input[0]
                inst_input.remove(int_list[int_list[index + 1]])
            elif length == 3:
                if str(opcode)[0] == '2':  # p1 in mode 2
                    int_list[int_list[index + 1] + rel_base] = inst_input[0]
                    inst_input.remove(int_list[int_list[index + 1] + rel_base])
            add = 2
        # opcode 4: outputs whatever is at the position specified by
        # its parameter.
        elif str(opcode).endswith('4'):
            if length == 3:
                if str(opcode)[0] == '1':  # p1 in mode 1
                    inst_output.append(int_list[index + 1])
                elif str(opcode)[0] == '2':  # p1 in mode 2
                    inst_output.append(int_list[int_list[index + 1] + rel_base])
            else:  # p1 in mode 0
                inst_output.append(int_list[int_list[index + 1]])
            add = 2
        # opcode 5: jump if true. if p1 != 0, then, index = value of p2
        # otherwise, it does nothing and just adds 3.
        elif str(opcode).endswith('5'):
            if length <= 2:  # p1 and p2 in parameter mode 0
                if int_list[int_list[index + 1]] != 0:
                    index = int_list[int_list[index + 2]]
                    add = 0
                else:
                    add = 3
            elif length == 3:  # p1 uk but not 0, p2 in parameter mode 0
                if str(opcode)[0] == '1':  # p1 in mode 1
                    if int_list[index + 1] != 0:
                        index = int_list[int_list[index + 2]]
                        add = 0
                    else:
                        add = 3
                elif str(opcode)[0] == '2':  # p1 in mode 2
                    if int_list[int_list[index + 1] + rel_base] != 0:
                        index = int_list[int_list[index + 2]]
                        add = 0
                    else:
                        add = 3
            elif length == 4:  # p1 is uk, p2 uk but not 0
                if str(opcode)[0] == '1':  # p2 in mode 1
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        if int_list[int_list[index + 1]] != 0:
                            index = int_list[index + 2]
                            add = 0
                        else:
                            add = 3
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        if int_list[index + 1] != 0:
                            index = int_list[index + 2]
                            add = 0
                        else:
                            add = 3
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        if int_list[int_list[index + 1] + rel_base] != 0:
                            index = int_list[index + 2]
                            add = 0
                        else:
                            add = 3
                elif str(opcode)[0] == '2':  # p2 in mode 2
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        if int_list[int_list[index + 1]] != 0:
                            index = int_list[int_list[index + 2] + rel_base]
                            add = 0
                        else:
                            add = 3
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        if int_list[index + 1] != 0:
                            index = int_list[int_list[index + 2] + rel_base]
                            add = 0
                        else:
                            add = 3
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        if int_list[int_list[index + 1] + rel_base] != 0:
                            index = int_list[int_list[index + 2] + rel_base]
                            add = 0
                        else:
                            add = 3
        # opcode 6: jump if false. if p1 == 0, index = value indicated
        # by p2. otherwise, does nothing and add = 3.
        elif str(opcode).endswith('6'):
            if length <= 2:  # p1 and p2 in parameter mode 0
                if int_list[int_list[index + 1]] == 0:
                    index = int_list[int_list[index + 2]]
                    add = 0
                else:
                    add = 3
            elif length == 3:  # p1 uk but not 0, p2 in parameter mode 0
                if str(opcode)[0] == '1':  # p1 in mode 1
                    if int_list[index + 1] == 0:
                        index = int_list[int_list[index + 2]]
                        add = 0
                    else:
                        add = 3
                elif str(opcode)[0] == '2':  # p1 in mode 2
                    if int_list[int_list[index + 1] + rel_base] == 0:
                        index = int_list[int_list[index + 2]]
                        add = 0
                    else:
                        add = 3
            elif length == 4:  # p1 is uk, p2 uk but not 0
                if str(opcode)[0] == '1':  # p2 in mode 1
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        if int_list[int_list[index + 1]] == 0:
                            index = int_list[index + 2]
                            add = 0
                        else:
                            add = 3
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        if int_list[index + 1] == 0:
                            index = int_list[index + 2]
                            add = 0
                        else:
                            add = 3
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        if int_list[int_list[index + 1] + rel_base] == 0:
                            index = int_list[index + 2]
                            add = 0
                        else:
                            add = 3
                elif str(opcode)[0] == '2':  # p2 in mode 2
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        if int_list[int_list[index + 1]] == 0:
                            index = int_list[int_list[index + 2] + rel_base]
                            add = 0
                        else:
                            add = 3
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        if int_list[index + 1] == 0:
                            index = int_list[int_list[index + 2] + rel_base]
                            add = 0
                        else:
                            add = 3
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        if int_list[int_list[index + 1] + rel_base] == 0:
                            index = int_list[int_list[index + 2] + rel_base]
                            add = 0
                        else:
                            add = 3
        # opcode 7: less than. if p1 < p2, p3 = 1. else, p3 = 0.
        elif str(opcode).endswith('7'):
            if length <= 2:  # all p in param mode 0
                if int_list[int_list[index + 1]] < int_list[int_list[index + 2]]:
                    int_list[int_list[index + 3]] = 1
                else:
                    int_list[int_list[index + 3]] = 0
            elif length == 3:  # p1 uk but not mode 0, p2 in mode 0
                if str(opcode)[0] == '1':  # p1 in mode 1
                    if int_list[index + 1] < int_list[int_list[index + 2]]:
                        int_list[int_list[index + 3]] = 1
                    else:
                        int_list[int_list[index + 3]] = 0
                elif str(opcode)[0] == '2':  # p1 in mode 2
                    if int_list[int_list[index + 1] + rel_base] < int_list[int_list[index + 2]]:
                        int_list[int_list[index + 3]] = 1
                    else:
                        int_list[int_list[index + 3]] = 0
            elif length == 4:  # p1 uk, p2 uk but not mode 0
                if str(opcode)[0] == '1':  # p2 in mode 1
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        if int_list[int_list[index + 1]] < int_list[index + 2]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        if int_list[index + 1] < int_list[index + 2]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        if int_list[int_list[index + 1] + rel_base] < int_list[index + 2]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
                elif str(opcode)[0] == '2':  # p2 in mode 2
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        if int_list[int_list[index + 1]] < int_list[int_list[index + 2] + rel_base]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        if int_list[index + 1] < int_list[int_list[index + 2] + rel_base]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        if int_list[int_list[index + 1] + rel_base] < int_list[int_list[index + 2] + rel_base]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
            elif length == 5:
                if str(opcode)[0] == '2':  # p3 in mode 2
                    if str(opcode)[1] == '0':  # p2 in mode 0
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            if int_list[int_list[index + 1]] < int_list[int_list[index + 2]]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            if int_list[index + 1] < int_list[int_list[index + 2]]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            if int_list[int_list[index + 1] + rel_base] < int_list[int_list[index + 2]]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                    elif str(opcode)[1] == '1':  # p2 in mode 1
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            if int_list[int_list[index + 1]] < int_list[index + 2]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            if int_list[index + 1] < int_list[index + 2]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            if int_list[int_list[index + 1] + rel_base] < int_list[index + 2]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                    elif str(opcode)[1] == '2':  # p2 in mode 2
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            if int_list[int_list[index + 1]] < int_list[int_list[index + 2] + rel_base]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            if int_list[index + 1] < int_list[int_list[index + 2] + rel_base]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            if int_list[int_list[index + 1] + rel_base] < int_list[int_list[index + 2] + rel_base]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
            add = 4
        # opcode 8: equals. if p1 == p2, p3 = 1. else p3 = 0.
        elif str(opcode).endswith('8'):
            if length <= 2:  # all p in param mode 0
                if int_list[int_list[index + 1]] == int_list[int_list[index + 2]]:
                    int_list[int_list[index + 3]] = 1
                else:
                    int_list[int_list[index + 3]] = 0
            elif length == 3:  # p1 uk but not mode 0, p2 in mode 0
                if str(opcode)[0] == '1':  # p1 in mode 1
                    if int_list[index + 1] == int_list[int_list[index + 2]]:
                        int_list[int_list[index + 3]] = 1
                    else:
                        int_list[int_list[index + 3]] = 0
                elif str(opcode)[0] == '2':  # p1 in mode 2
                    if int_list[int_list[index + 1] + rel_base] == int_list[int_list[index + 2]]:
                        int_list[int_list[index + 3]] = 1
                    else:
                        int_list[int_list[index + 3]] = 0
            elif length == 4:  # p1 uk, p2 uk but not mode 0
                if str(opcode)[0] == '1':  # p2 in mode 1
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        if int_list[int_list[index + 1]] == int_list[index + 2]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        if int_list[index + 1] == int_list[index + 2]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        if int_list[int_list[index + 1] + rel_base] == int_list[index + 2]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
                elif str(opcode)[0] == '2':  # p2 in mode 2
                    if str(opcode)[1] == '0':  # p1 in mode 0
                        if int_list[int_list[index + 1]] == int_list[int_list[index + 2] + rel_base]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
                    elif str(opcode)[1] == '1':  # p1 in mode 1
                        if int_list[index + 1] == int_list[int_list[index + 2] + rel_base]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
                    elif str(opcode)[1] == '2':  # p1 in mode 2
                        if int_list[int_list[index + 1] + rel_base] == int_list[int_list[index + 2] + rel_base]:
                            int_list[int_list[index + 3]] = 1
                        else:
                            int_list[int_list[index + 3]] = 0
            elif length == 5:
                if str(opcode)[0] == '2':  # p3 in mode 2
                    if str(opcode)[1] == '0':  # p2 in mode 0
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            if int_list[int_list[index + 1]] == int_list[int_list[index + 2]]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            if int_list[index + 1] == int_list[int_list[index + 2]]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            if int_list[int_list[index + 1] + rel_base] == int_list[int_list[index + 2]]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                    elif str(opcode)[1] == '1':  # p2 in mode 1
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            if int_list[int_list[index + 1]] == int_list[index + 2]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            if int_list[index + 1] == int_list[index + 2]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            if int_list[int_list[index + 1] + rel_base] == int_list[index + 2]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                    elif str(opcode)[1] == '2':  # p2 in mode 2
                        if str(opcode)[2] == '0':  # p1 in mode 0
                            if int_list[int_list[index + 1]] == int_list[int_list[index + 2] + rel_base]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '1':  # p1 in mode 1
                            if int_list[index + 1] == int_list[int_list[index + 2] + rel_base]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
                        elif str(opcode)[2] == '2':  # p1 in mode 2
                            if int_list[int_list[index + 1] + rel_base] == int_list[int_list[index + 2] + rel_base]:
                                int_list[int_list[index + 3] + rel_base] = 1
                            else:
                                int_list[int_list[index + 3] + rel_base] = 0
            add = 4
        # opcode 9: adjust the relative base by the value of its only parameter.
        elif str(opcode).endswith('9'):
            if length <= 2:  # p1 in mode 0
                rel_base += int_list[int_list[index + 1]]
            elif str(opcode)[0] == '1':  # p1 in mode 1
                rel_base += int_list[index + 1]
            elif str(opcode)[0] == '2':  # p1 in mode 2
                rel_base += int_list[int_list[index + 1] + rel_base]
            add = 2
        index += add
        opcode = int_list[index]
    return inst_output


original_data = []
for val in intcode:
    for comm in val:
        original_data.append(int(comm))

# part 1
print(opcode_compute(original_data.copy(), [1], 0))

# part 2
print(opcode_compute(original_data.copy(), [2], 0))
