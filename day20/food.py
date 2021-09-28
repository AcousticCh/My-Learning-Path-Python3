#!usr/bin/env python3
from turtle import Turtle
from random import randint
class Food(Turtle):
	def __init__(self):
		super().__init__()
		
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
		self.color("#0000ff")
		self.speed(0)
		random_x = randint(-280, 280)
		random_y = randint(-280, 280)
		self.goto(random_x, random_y)
	
		
	def move(self):
		random_x = randint(-280, 280)
		random_y = randint(-280, 280)
		self.goto(random_x, random_y)
		
	
