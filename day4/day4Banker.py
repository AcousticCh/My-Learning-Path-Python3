#!usr/bin/env python
import random
names = input("Names?\n")

for i in names:
	if i == ",":
		names = names.replace(i, "")

name_list = names.split(" ")

print(random.choice(name_list))

