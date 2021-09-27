#!usr/bin/env python
import random

input("Call your side and hit enter to flip coin")
coin = random.randint(0, 1)

if coin == 0:
	print("tails!")
else:
	print("heads!")
