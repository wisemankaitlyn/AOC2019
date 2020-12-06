# day 4
# kaitlyn wiseman
# 12/06/2020

low = 172851
high = 675869

i = range(low, high + 1)
numValid = 0

for password in i:
    adj_same = False
    nev_dec = True
    temp = str(password)
    index = 0
    for digit in temp:
        if digit + digit in temp:
            adj_same = True
        if index != 5:
            if int(digit) > int(temp[index + 1]):
                nev_dec = False
        index += 1
    if adj_same and nev_dec:
        numValid += 1

print("part 1: the number of valid passwords is " + str(numValid))

low = 172851
high = 675869

i = range(low, high + 1)
numValid = 0

for password in i:
    adj_same = False
    nev_dec = True
    temp = str(password)
    index = 0
    for digit in temp:
        if digit + digit in temp and digit + digit + digit not in temp:
            adj_same = True
        if index != 5:
            if int(digit) > int(temp[index + 1]):
                nev_dec = False
        index += 1
    if adj_same and nev_dec:
        numValid += 1

print("part 2: the number of valid passwords is " + str(numValid))
