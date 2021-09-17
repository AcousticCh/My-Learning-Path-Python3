#!usr/bin/env python
import random
print("Welcome to PyPassword Generator")

list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                   "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                   "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                   "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
list_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
list_of_symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


num_of_letters = input("Number of letters: ")
num_of_numbers = input("Number of numbers: ")
num_of_symbols = input("Number of symbols: ")

num_of_letters = int(num_of_letters)
num_of_numbers = int(num_of_numbers)
num_of_symbols = int(num_of_symbols)

total_characters = num_of_letters + num_of_numbers + num_of_symbols
password = []
while total_characters > len(password):
	if num_of_letters > 0:
		num = random.randint(0, len(password))
		num_of_letters = num_of_letters - 1
		letter = random.choice(list_of_letters)
		password.insert(num, letter)
	if num_of_numbers > 0:
		num = random.randint(0, len(password))
		num_of_numbers = num_of_numbers - 1
		number = random.choice(list_of_numbers)
		password.insert(num, number)	
	if num_of_symbols > 0:
		num = random.randint(0, len(password))
		num_of_symbols = num_of_symbols - 1
		symbol = random.choice(list_of_symbols)
		password.insert(num, symbol)
counter = 0
final_password = ""
for char in password:
	final_password += char
	counter = counter + 1
	
print(final_password)
