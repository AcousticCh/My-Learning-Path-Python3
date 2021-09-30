#!usr/bin/env python3
from turtle import Turtle
from random import randint

bounce_down_to_right = randint(270, 360)
bounce_down_to_left = randint(180, 270)
bounce_up_to_right = randint(0, 90)
bounce_up_to_left = randint(90, 180)

class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len = 1, stretch_wid = 1)
		self.color("#00FF00")
		self.speed(0)
		self.MOVEMENT_GAP = 10

	def start_ball(self):
		self.goto(0, 0)
		self.seth(randint(0, 359))
		
		
	def ball_move(self):
		self.forward(self.MOVEMENT_GAP)
		
		
	def bounce(self):
		if self.ycor() >= 288:
			if self.heading() >= 0 and self.heading() <= 90:
				self.seth(bounce_down_to_right)
			elif self.heading() >= 90 and self.heading() <= 180:
				self.seth(bounce_down_to_left)
		elif self.ycor() <= -288:
			if self.heading() >= 270 and self.heading() <= 360:
				self.seth(bounce_up_to_right)
			elif self.heading() >= 180 and self.heading() <= 270:
				self.seth(bounce_up_to_left)
		
	def hit(self, paddle):
		b1 = randint(90, 180)
		b2 = randint(180, 270)
		b3 = randint(0, 90)
		b4 = randint(270, 360)
		
		if self.xcor() > 365 and self.distance(paddle) < 51:
			if self.heading() > 0 and self.heading() < 90:
				self.seth(b1)
				self.MOVEMENT_GAP += 1
			elif self.heading() > 270 and self.heading() < 360:
				self.seth(b2)
				self.MOVEMENT_GAP += 1
		elif self.xcor() < -370 and self.distance(paddle) < 51:
			if self.heading() > 90 and self.heading() < 180:
				self.seth(b3)
				self.MOVEMENT_GAP += 1
			elif self.heading() > 180 and self.heading() < 270:
				self.seth(b4)
				self.MOVEMENT_GAP += 1
		
	def miss(self):
		if self.xcor() >= 400:
			self.start_ball()
			return "right"
			
	def miss2(self):
		if self.xcor() <= -400:
			self.start_ball()
			return"left"
