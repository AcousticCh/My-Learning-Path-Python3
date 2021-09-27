#!usr/bin/env python

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
	
for q in question_data["results"]:
	question_text = q["question"]
	question_answer = q["correct_answer"]
	new_question = Question(question_text, question_answer)
	question_bank.append(new_question)
	

quiz = QuizBrain(question_bank)
testing = "True"
while testing == "True"	:
	quiz.is_correct(quiz.next_question())
	testing = quiz.still_has_questions()
	
