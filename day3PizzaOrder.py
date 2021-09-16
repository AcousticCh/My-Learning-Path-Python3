#!usr/bin/env python

print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25\n")

print("Pepperoni for Small Pizza: + $2")
print("Pepperoni for Medium or Large Pizza: + $3\n")

print("Extra cheese for any size pizza: + $1\n")
price = 0
size = input("Size [S/M/L]: ").upper()
pepper = input("Pepperoni [Y/N]: ").upper()
extra_cheese = input("Extra Cheese [Y/N]: ").upper()

if size == "S":
	price += 15
	if pepper == "Y":
		price += 2
if size == "M":
	price += 20
	if pepper == "Y":
		price += 3
if size == "L":
	price += 25
	if pepper == "Y":
		price += 3	

if extra_cheese == "Y":
	price += 1
	
print(price)


