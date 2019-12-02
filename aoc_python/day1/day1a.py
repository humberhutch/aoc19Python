def calculate_fuel(data):
    return int(data)//3-2

def main():
    f = open("day1.txt")
    fuel = f.readline()
    total_fuel = 0
    while (fuel != ""):
        total_fuel += calculate_fuel(fuel)
        fuel = f.readline()
    print (total_fuel)

main()