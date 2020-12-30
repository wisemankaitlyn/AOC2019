# day 07
# kaitlyn wiseman
# 12/30/2020


import csv
filename = "Input/Day07.txt"
intcode = csv.reader(open(filename), delimiter=',')

original_data = []
for val in intcode:
    for comm in val:
        original_data.append(int(comm))


def opcode_compute (int_list, inst_input, start_index):
    inst_output = []
    index = start_index
    opcode = int_list[index]
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
            int_list[int_list[index + 1]] = inst_input[0]
            inst_input.remove(int_list[int_list[index + 1]])
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
        if len(inst_output) > 0:
            inst_output.append(index)
            return inst_output
    return inst_output


thruster_output = 0

for i in range(5):
    for j in range(5):
        if j == i:
            continue
        for k in range(5):
            if k == i or k == j:
                continue
            for l in range(5):
                if l == i or l == j or l == k:
                    continue
                for m in range(5):
                    if m == i or m == j or m == k or m == l:
                        continue
                    this_data = original_data.copy()

                    A = opcode_compute(this_data, [i, 0], 0)
                    B = opcode_compute(this_data, [j, A[0]], 0)
                    C = opcode_compute(this_data, [k, B[0]], 0)
                    D = opcode_compute(this_data, [l, C[0]], 0)
                    E = opcode_compute(this_data, [m, D[0]], 0)

                    if E[0] > thruster_output:
                        thruster_output = E[0]

print("part 1: max thruster output is: " + str(thruster_output))

# part 2

thruster_output = 0

for i in [5, 6, 7, 8, 9]:
    for j in [5, 6, 7, 8, 9]:
        if j == i:
            continue
        for k in [5, 6, 7, 8, 9]:
            if k == i or k == j:
                continue
            for r in [5, 6, 7, 8, 9]:
                if r == i or r == j or r == k:
                    continue
                for m in [5, 6, 7, 8, 9]:
                    if m == i or m == j or m == k or m == r:
                        continue
                    this_data = original_data.copy()
                    A_data = original_data.copy()
                    B_data = original_data.copy()
                    C_data = original_data.copy()
                    D_data = original_data.copy()
                    E_data = original_data.copy()

                    A = opcode_compute(A_data, [i, 0], 0)
                    B = opcode_compute(B_data, [j, A[0]], 0)
                    C = opcode_compute(C_data, [k, B[0]], 0)
                    D = opcode_compute(D_data, [r, C[0]], 0)
                    E = opcode_compute(E_data, [m, D[0]], 0)
                    last_E = E
                    while True:
                        A = opcode_compute(A_data, [E[0]], A[1])
                        B = opcode_compute(B_data, [A[0]], B[1])
                        C = opcode_compute(C_data, [B[0]], C[1])
                        D = opcode_compute(D_data, [C[0]], D[1])
                        E = opcode_compute(E_data, [D[0]], E[1])
                        if E_data[E[1]] == 99:
                            break

                    if E[0] > thruster_output:
                        thruster_output = E[0]

print("part 2: the max thruster output is " + str(thruster_output))
