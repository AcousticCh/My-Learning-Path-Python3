#!usr/bin/env python

from random import randint

print("Choose your weapon")
player_selection = input("0 for rock, 1 for paper, 2 for scissors: ")
player_selection = int(player_selection)
ai_selection = randint(0, 2)

if player_selection == ai_selection:
	print("Tie! Try again")
elif player_selection == 0:
	if ai_selection == 1:
		print("You Lose :( ")
	else:
		print("You Win!")
elif player_selection == 1:
	if ai_selection == 2:
		print("You Lose :( ")
	else:
		print("You Win!")
elif player_selection == 2:
	if ai_selection == 0:
		print("You Lose :( ")
	else:
		print("You Win!")
else:
	print("Error: Invalid input")
	
