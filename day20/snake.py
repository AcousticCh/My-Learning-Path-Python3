#!usr/bin/env python3
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
class Snake:
	def __init__(self):
		self.segment = []
		self.create_snake()

	def create_snake(self):
		for position in STARTING_POSITIONS:
			pen = Turtle()
			pen.shape("square")
			pen.color("white")
			pen.penup()
			pen.goto(position)
			self.segment.append(pen)
		
	def move(self):
		for seg_num in range(len(self.segment) - 1, 0, -1):
			new_x = self.segment[seg_num -1].xcor()
			new_y = self.segment[seg_num -1].ycor()
			self.segment[seg_num].goto(new_x, new_y)
		self.segment[0].forward(DISTANCE)
		
	def move_left(self):
		self.segment[0].seth(180)
		
	def move_right(self):
		self.segment[0].seth(0)
	
	def move_up(self):
		self.segment[0].seth(90)
		
	def move_down(self):
		self.segment[0].seth(270)
		
	
