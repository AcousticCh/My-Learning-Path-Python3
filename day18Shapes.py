#!usr/bin/env python
from turtle import Turtle, Screen
from random import randint
from day18colors import color_list, angle_list
class Artist:
	def __init__(self, length_input, sides_input, angle_input, speed_input):
		self.pen = Turtle()
		self.screen = Screen()
		self.length = length_input
		self.color = "black"
		self.angle = angle_input
		self.sides = sides_input
		self.speed = speed_input
		
		
		
	def draw(self):
		
		for i in range(0, self.sides):
			self.pen.forward(self.length)
			self.pen.right(self.angle)
		self.update_draw()
		self.screen.exitonclick()
		
		
		
		
	def update_draw(self):
		
		self.sides += 1
		self.angle = 360 / self.sides
		self.new_color()
		
		
	def draw_circle(self):
		self.new_color()
		self.pen.speed(self.speed)
		self.pen.circle(100)
		self.turn()
		
	def turn(self):
		
		self.pen.left(5)
		
		if self.pen.heading() == 0:
			return print("end")
		self.draw_circle()
	
	
		
	def new_color(self):
		self.screen.colormode(255)
		r = randint(0, 255)
		g = randint(0, 255)
		b = randint(0, 255)
		self.pen.pencolor(r, g, b)
		
		
	
	def random_walk(self):
		self.pen.pensize(30)
		self.pen.speed(10)
		num = randint(0, len(angle_list) - 1)
		self.angle = angle_list[num]
		self.pen.right(self.angle)
		self.pen.forward(100)
		self.new_color()
	
		
artsy = Artist(length_input = 100, sides_input = 3, angle_input = 120, speed_input = 10)
artsy.draw_circle()
