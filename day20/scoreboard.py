#!usr/bin/env python3
from turtle import Turtle
class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.points = 0
		self.color("#ffffff")
		self.hideturtle()
		self.penup()
		self.sety(270)
		self.clear()
		self.write(arg = f"Score: {self.points}", move = False, align = "center", font = ("Arial", 20, "normal"))
		
	def add_point(self):
		self.clear()
		self.points += 1
		self.write(arg = f"Score: {self.points}", move = False, align = "center", font = ("Arial", 20, "normal"))

	def game_over(self):
		self.goto(0, 0)
		self.write("Game over!", align = "center", font = ("Arial", 20, "normal"))
