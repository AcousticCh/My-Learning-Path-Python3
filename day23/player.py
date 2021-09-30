#!usr/bin/env python3
from turtle import Turtle



class Player(Turtle):
	def __init__(self, starting_pos, player_color, player_shape, player_jump):
		super().__init__()
		self.penup()
		self.color(player_color)
		self.goto(starting_pos)
		self.fix = self.pos()
		self.shape(player_shape)
		self.seth(90)
		self.jump = player_jump
	def move(self):
		self.forward(self.jump)
	def go_back(self):
		self.ht()
		self.goto(self.fix)
		self.showturtle()
