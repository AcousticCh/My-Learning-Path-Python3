#!usr/bin/env python3
from turtle import Turtle
from random import randint



class Cars(Turtle):
	def __init__(self):
		super().__init__()
		self.ht()
		self.cars = []
		self.color_list = ["yellow", "blue", "orange", "green", "red", "purple",]
		self.generate_car()
		self.car_speed = 10
		
	def generate_car(self):
		n = randint(0, len(self.color_list) - 1)
		placement = randint(-250, 250)
		car = Turtle()
		car.ht()
		car.penup()
		car.goto(650, placement)
		car.seth(180)
		car.shape("square")
		car.turtlesize(stretch_wid = 1, stretch_len = 2,)
		car.color(self.color_list[n])
		car.showturtle()
		self.cars.append(car)
		
	def move(self):
		for i in range(0, len(self.cars)):
			self.cars[i].forward(self.car_speed)
			
	def empty(self):
		for i in range(0, len(self.cars)):
			self.cars[i].clear()
			self.cars[i].goto(600, 0)
		self.cars = []
