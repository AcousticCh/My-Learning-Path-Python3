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
print(bmi)

