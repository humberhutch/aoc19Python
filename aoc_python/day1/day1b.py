def calculate_fuel(data):
    return int(data)//3-2

def main():
	f = open("day1.txt")
	fuel = f.readline()
	total_fuel = 0
	while (fuel != ""):
		sub_total=0
		next_fuel = calculate_fuel(fuel)
		while (next_fuel>0):
			sub_total += next_fuel
			next_fuel = calculate_fuel(next_fuel)
		total_fuel +=sub_total
		fuel = f.readline()
	print (total_fuel)

main()