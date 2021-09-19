#!usr/bin/env python

calculation = input("Would you like to add, subtract, divide or multiply?\n")

numa = int(input("First Number: "))
numb = int(input("Second Number: "))

def add(num1, num2):
	add = num1 + num2
	return add
	
def subtract(num1, num2):
	subtract = num1 - num2
	return subtract
	
def divide(num1, num2):
	divide = num1 / num2
	return divide
	
def multiply(num1, num2):
	multiply = num1 * num2
	return multiply
	
def calculate(operation):
	switcher = {
		"add": add(num1 = numa, num2 = numb),
		"subtract": subtract(num1 = numa, num2 = numb),
		"divide": divide(num1 = numa, num2 = numb),
		"multiply": multiply(num1 = numa, num2 = numb),
		}
	return switcher[operation]
numa = calculate(operation = calculation)
print(numa)

again = input("Continue or end?\n").title()
while again == "Continue":
	calculation = input("Would you like to add, subtract, divide or multiply?\n")
	numb = int(input("next number: "))
	numa = calculate(operation = calculation)
	print(numa)
	again = input("Continue or end?\n").title()
		
	

