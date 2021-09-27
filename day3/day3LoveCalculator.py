#!usr/bin/env python
print("Welcome to the love calculator")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

score = 0
score2 = 0

score += name1.count("t")
score += name1.count("r")
score += name1.count("u")
score += name1.count("e")

score += name2.count("t")
score += name2.count("r")
score += name2.count("u")
score += name2.count("e")

score2 += name1.count("l")
score2 += name1.count("o")
score2 += name1.count("v")
score2 += name1.count("e")

score2 += name2.count("l")
score2 += name2.count("o")
score2 += name2.count("v")
score2 += name2.count("e")

score = str(score)
score2 = str(score2)

score = score + score2

print(score)
