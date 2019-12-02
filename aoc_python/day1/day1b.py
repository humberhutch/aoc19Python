f = open("day1.txt")
fuel = f.readline()
total_fuel = 0
while (fuel!=""):
	sub_total = 0
	next_fuel = int(fuel)//3-2
	sub_total = next_fuel
	
	while (next_fuel >0):
		next_fuel = int(next_fuel)//3-2
		sub_total += next_fuel
	total_fuel +=sub_total
	fuel = f.readline()
	    
print (total_fuel)