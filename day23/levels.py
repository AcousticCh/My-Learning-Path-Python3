#!usr/bin/env python3
from turtle import Turtle

class Levels(Turtle):
	def __init__(self):
		super().__init__()
		self.ht()
		self.penup()
		self.goto(-290, 280)
		self.clear()
		self.current_level = 0
		self.write(arg = f"Level: {self.current_level}", move = False, align = "left", font = ("Arial", 10, "normal"))
	
	def next_level(self):
		self.clear()
		self.current_level += 1
		self.write(arg = f"Level: {self.current_level}", move = False, align = "left", font = ("Arial", 10, "normal"))

	def game_over(self):
		self.goto(0, 0)
		self.write(arg = "        Game Over!\nYou've been run over", move = False, align = "center", font = ("Arial", 20, "normal"))
