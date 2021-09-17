#!usr/bin/env python
import random
word_list = ["king", "queen", "bishop"]
word_selected = random.choice(word_list)
word = []
blanks = []
#once i get one right game breaks
for i in word_selected:
	blanks.append("_")
	word.append(i)
	
tries_left = 10

while "_" in blanks:
	test = []
	print(blanks)
	print(f"Attempts Left: {tries_left}")
	letter = input("choose your letter: ")
	for i in range(0, len(word)):
		if letter == word[i]:
			blanks.pop(i)
			blanks.insert(i, word[i])
			test.append("True")
		else:
			test.append("False")
			
	if "True" not in test:
		tries_left = tries_left - 1
		
	if tries_left == 0:
		print("You Lose")
		exit()
			
print(f"{blanks} You Win!")
