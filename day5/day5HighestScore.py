#!usr/bin/env python
#replicate max function

student_scores = input("scores:\n")

student_scores = student_scores.replace(",", "")
score_list = student_scores.split(" ")
scores = []
for i in score_list:
	scores.append(int(i))
high_score = 0
for i in scores:
	if i > high_score:
		high_score = i

print(f"Highest score is {high_score}")
