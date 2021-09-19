#!usr/bin/env python

print("check how many days in a month")
year_selected = input("year: ")
year_selected = int(year_selected)
month_selected = input("Month by number: ")
month_selected = int(month_selected)
months_dict = {
	1: 31,
	2: 28,
	3: 31,
	4: 30,
	5: 31,
	6: 30,
	7: 31,
	8: 31,
	9: 30,
	10: 31,
	11: 30,
	12: 31,
	}
def days_in_month(year, month):

	if year % 4 == 0:
		if year % 100 != 0:
			leap = True
		else:
			if year % 400 == 0:
				leap = True
	else:
		leap = False
	if leap == True:
		months_dict.update({2: 29})
	return months_dict[2]
	

days = days_in_month(year = year_selected, month = month_selected)
print(f"there is {days} days in that month")
