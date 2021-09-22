#!usr/bin/env python
# TODO: ask the questions
# TODO: check if anser was correct
# TODO: check if questions left = 0

class QuizBrain:
	def __init__(self, q_list):
		self.question_number = 0
		self.question_list = q_list
		self.correct = 0
		
		
	def still_has_questions(self):
		if self.question_number == len(self.question_list):
			print("Quiz Complete!")
			print(f"Your final score is {self.correct} out of {len(self.question_list)}")
			return "False"
		else:
			return "True"
		
		
	def next_question(self):
		current_question = self.question_list[self.question_number]
		self.question_number += 1
		answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
		answer_list = [current_question.answer, answer]
		return answer_list
		
	def is_correct(self, response):
		if response[0].lower() == response[1].lower():
			print("You're right")
			self.correct += 1
		else:
			print(f"You're wrong")
		print(f"correct answer is {response[0]}")
		print(f"Correct: {self.correct}/{len(self.question_list)}\n")
			
		
		
