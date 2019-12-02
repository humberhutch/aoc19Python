f = open("day1.txt")
fuel = f.readline()
total_fuel = 0
while (fuel != ""):
    total_fuel += int(fuel)//3-2
    fuel = f.readline()
print (total_fuel)
