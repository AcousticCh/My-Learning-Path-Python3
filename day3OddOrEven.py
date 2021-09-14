#!usr/bin/env python

print("Is your number odd or even?")
number = input("input integer here: \n")
number = int(number)
num_for_Equation = number %2
if num_for_Equation == 0:
	print(f"{number} is even!")
elif num_for_Equation == 1:
	print(f"{number} is odd!")
else:
	print("error")
