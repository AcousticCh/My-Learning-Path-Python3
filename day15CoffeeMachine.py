#!usr/bin/env python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_in_machine = 0

off = "False"
while off == "False":
	
	selected_drink = input("What would you like (espresso/latte/cappuccino): ").lower()
	
	if selected_drink == "report":
		print(f"Water: {resources['water']}ml")
		print(f"Milk: {resources['milk']}ml")
		print(f"Coffee: {resources['coffee']}g")
		print(f"Money: ${'{:.2f}'.format(money_in_machine)}")
		continue
	if selected_drink == "off":
		print("Goodbye!")
		off = "True"
		break
	
	
	price = MENU[selected_drink]["cost"]
	price_print = "{:.2f}".format(price)
	
	print(f"Your drink cost ${price_print}")
	get_quarters = float(input("How many quarters: "))
	get_quarters *= 0.25
	get_dimes = float(input("How many dimes: "))
	get_dimes *= 0.10
	get_nickels = float(input("How many nickels: "))
	get_nickels *= 0.05
	get_pennies = float(input("How many pennies: "))
	get_pennies *= 0.01
	
	paid = get_quarters + get_dimes + get_nickels + get_pennies
	
	if paid >= price:
		change = paid - price# change return varibale
		needed_res = MENU[selected_drink]["ingredients"]# subtract resources used
		needed_water = needed_res["water"]
		needed_milk = needed_res["milk"]
		needed_coffee = needed_res["coffee"]
		resources["water"] -= needed_water
		resources["milk"] -= needed_milk
		resources["coffee"] -= needed_coffee
		if resources["water"] <= 0:
			print(f"Insufficient water")
			off = "True"
			print(f"Returning: ${paid}\n have a nice day!")
			break
		if resources["milk"] <= 0:
			print(f"Insufficient milk")
			off = "True"
			print(f"Returning: ${paid}\n have a nice day!")
			break
		if resources["coffee"] <= 0:
			print(f"Insufficient coffee")
			off = "True"
			print(f"Returning: ${paid}\n have a nice day!")
			break
	else:
		print(f"Insufficient funds, Refunding ${paid}")
		off = "True"	
	money_in_machine += price
	change_print = "{:.2f}".format(change)
	print(f"Here is your change: ${change_print}")
	print(f"Here is your {selected_drink} have a nice day!")




#make report and off options
