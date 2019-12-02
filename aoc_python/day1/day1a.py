def calculate_fuel(data):
    return int(data)//3-2

def main():
    data = open("day1.txt").readlines()
    total_fuel = 0
    for fuel in data:
        total_fuel += calculate_fuel(fuel)
    print (total_fuel)

main()