#!usr/bin/env python3
from turtle import Turtle
PLAYERS = 1

class Paddle(Turtle):
	def __init__(self):
		super().__init__()
		
		self.pen = Turtle()
		self.pen.penup()
		self.pen.speed(0)
		self.pen.shape("square")
		self.pen.color("#FFFFFF")
		self.pen.seth(90)
		self.pen.shapesize(stretch_wid = 1, stretch_len = 5)
		
	def player_1(self):
		self.pen.goto(-380, 0)

	
	def player_2(self):
		self.pen.goto(375, 0)
		
	def move_up(self):
		self.pen.forward(20)
	
	def move_down(self):
		self.pen.backward(20)
