#!usr/bin/env python
from subprocess import call
bidders = {}

should_continue = True
while should_continue == True:
	call("clear")
	print("Welcome to the Secret Auction!")
	name = input("What is your name?\n")
	bid = input("What is your bid?\n")
	bidders.update({name: bid})
	
	
	def do_again():
		again = input("Is there more bidders?\n")
		if again == "no":
			return False
		elif again == "yes":
			return True
		else:
			print(" [+] Invalid input")
			return do_again()
	
	should_continue = do_again()	
	 
bid_val = max(bidders.values())
	

def get_highest_bidder(val):
	for key, value in bidders.items():
		if val == value:
			return key
	return print("Key doesn't exist")
	
print(f"The highest bid goes to {get_highest_bidder(bid_val)}")

		
