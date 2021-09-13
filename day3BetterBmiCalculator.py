#!usr/bin/env python
weight = ""
height = ""
bmi = 0

weight = input("What is your weight in pounds?\n")
weight = float(weight)
weight = weight * 0.45359237
height = input("What is your height in feet? (inches will be next)\n")
height = float(height)
inches = input(f"How many inches between {height} feet and {height + 1} feet?\n")
inches = float(inches)
inches = inches / 12
print(height, inches)
height = (height + inches) * 0.3048
print(height)
bmi = weight / (height ** 2)
bmi = round(bmi, 1)
if bmi < 18.5:
	bmi_rating = "underweight"
elif bmi >= 18.5 and bmi < 25.0:
	bmi_rating = "a normal weight"
elif bmi >= 25.0 and bmi < 30.0:
	bmi_rating = "overweight"
elif bmi >= 30.0 and bmi < 40:
	bmi_rating = "obese"
elif bmi >= 40: 
	bmi_rating = "extremely obese"
else:
	print("Conditional error line 30")
	
print(f"Your Bmi is {bmi}, you are considered {bmi_rating}.")
