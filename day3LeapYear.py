#!usr/bin/env python

print("check if your year is leap year")
year = input("year: ")
year = int(year)

if year % 4 == 0:
	if year % 100 != 0:
		print("leap year")
	else:
		if year % 400 == 0:
			print("leap year")
		
		
else:
	print("Not a leap year")
	
