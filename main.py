from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
drink_menu = Menu()
profit = MoneyMachine()
on = "True"
while on == "True":
	drink = input(f"What would you like {drink_menu.get_items()}: ").lower()
	if drink == "report":
		machine.report()
		profit.report()
		continue
	if drink == "off":
		on = "False"
		print("Goodbye!")
		continue
	drink = drink_menu.find_drink(drink) # drink is now a MenuItem()
	if machine.is_resource_sufficient(drink): # if have resources return True
		print(f"Your drink cost ${drink.cost}")
		profit.make_payment(drink.cost)
		machine.make_coffee(drink)
		
	else:
		print(" [+] Insufficient Ingredients")
	
