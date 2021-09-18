#!usr/bin/env python

print("Prime or Not!")

n = int(input("Your number: "))
def prime_check(number):
	prime = True
	for i in range(2, number):
		if number % i == 0:
			prime = False
			print("Not Prime")
			break;
	if prime == True:
		print("Prime!")
prime_check(number = n)
