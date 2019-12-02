def calculate_fuel(data):
	return int(data)//3-2

def main():
	data = open("day1.txt").readlines()
	total_fuel = 0
	for fuel in data:
		sub_total=0
		next_fuel = calculate_fuel(fuel)
		while (next_fuel>0):
			sub_total += next_fuel
			next_fuel = calculate_fuel(next_fuel)
		total_fuel +=sub_total
	print (total_fuel)

main()