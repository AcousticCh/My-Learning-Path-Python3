totalOfBill = ""
amountOfPeople = ""
tipPercentage = ""

print("Welcome to the Tip Calculator")
totalOfBill = input("What is the total bill's cost?\n")
totalOfBill = float(totalOfBill)

amountOfPeople = input("how many people are splitting the bill?\n")
amountOfPeople = int(amountOfPeople)

tipPercentage = input("What percentage of the bill would you like the tip to be?\n")
tipPercentage = int(tipPercentage)

tip = tipPercentage / 100
tip *= totalOfBill
billPerPerson = (totalOfBill + tip) / amountOfPeople

print(f"Each person should pay: ${billPerPerson}")