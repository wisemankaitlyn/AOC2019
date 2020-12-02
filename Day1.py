# day 1
# kaitlyn wiseman
# 12/02/2020


# part 1
mass_list = open("Input\Day1.txt", "r")

fuel_required = 0

mass = mass_list.readline()
while mass != "":
    fuel_required += int(int(mass) / 3) - 2
    mass = mass_list.readline()

print("part 1: the total fuel required for liftoff is: ")
print(fuel_required)

mass_list.close()

# part 2
mass_list = open("Input\Day1.txt", "r")

fuel_required = 0
init_fuel = 0
add_fuel = 0

mass = mass_list.readline()
while mass != "":
    init_fuel = int(int(mass) / 3) - 2
    fuel_required += init_fuel

    add_fuel = int(init_fuel / 3) - 2

    while add_fuel > 0:
        fuel_required += add_fuel
        add_fuel = int(add_fuel / 3) - 2

    mass = mass_list.readline()

print("part 2: the total fuel required for liftoff is: ")
print(fuel_required)

mass_list.close()
