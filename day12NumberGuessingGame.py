#!usr/bin/env python
from random import randint
from subprocess import call

def start():
	call("clear")
	print("Welcome to the Number Guessing Game")
	print("I am thinking of a number between 1 and 100")
	print("Can you guess it?")
	difficulty = input("Select Difficulty:\n'Easy'\n'Hard'\n")
	if difficulty != "easy":
		if difficulty != "hard":
			print(" [+] Invalid input")
			start()
	if difficulty == "easy":
		rounds = 10
	elif difficulty == "hard":
		rounds = 5
	
	play(turns = rounds)
		
def play(turns):
	ai_number = randint(1, 100)
	player_guess = 0
	while turns > 0:
		print(f"You have {turns} guesses left")
		player_guess = int(input("Choose your number: "))
		if player_guess == ai_number:
			again = input("You Win, play again? [y/n]: ").lower()
			if again == "y":
				start()
			elif again == "n":
				break
			else:
				print(" [+] Invalid input")
		if player_guess < ai_number:
			print("Guess too low")
			turns = turns - 1
		elif player_guess > ai_number:
			print("Guess too high")
			turns = turns - 1
start()
