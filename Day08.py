# day 08
# kaitlyn wiseman
# 01/01/2021  (happy new year!!)

import pandas as pd

image_data = open("Input/Day08.txt")

# 25 * 6 = 150
width = 25
height = 6

# find the layer that contains the fewest '0' digits.
# on that layer, count the number of '1' digits and
# the number of '2' digits.  what is the product of
# those two numbers?

layers = []

while True:
    temp = image_data.readline(150)
    if temp == '':
        break
    layers.append(temp)

z_cnt = 150
z_ind = 0

for n in range(len(layers)):
    if layers[n].count('0') < z_cnt:
        z_cnt = layers[n].count('0')
        z_ind = n

o_cnt = layers[z_ind].count('1')
t_cnt = layers[z_ind].count('2')

print(str(o_cnt * t_cnt))


# part 2

image_data.close()
image_data = open("Input/Day08.txt")
layers.clear()

while True:
    t_l = []
    temp = image_data.readline(width)
    if temp == '':
        break
    t_l.append(temp)
    for n in range(height - 1):
        temp = image_data.readline(width)
        t_l.append(temp)
    layers.append(t_l)

full_image = ['0' * width] * height

for h in range(height):
    for w in range(width):
        for layer in layers:
            # layer[h][w]
            if layer[h][w] == '1':
                temp = full_image[h][0:w]
                temp += '#'
                temp += full_image[h][w+1:]
                full_image[h] = temp
                break
            elif layer[h][w] == '0':
                temp = full_image[h][0:w]
                temp += ' '
                temp += full_image[h][w + 1:]
                full_image[h] = temp
                break

for layer in full_image:
    print(layer)
