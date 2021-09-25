#!usr/bin/env python
from turtle import Turtle, Screen
from random import randint

pen = Turtle()
screen = Screen()
screen.colormode(255)

color_list = [(36, 19, 15), (196, 145, 125), (28, 106, 158), (8, 22, 46), (140, 87, 54), (237, 215, 87), (212, 73, 98), (199, 133, 154)]

x = -70 * 5
y = -70 * 5
pen.penup()
pen.setposition(x, y)
pen.pendown()
go = 0
while go < 10:
	for i in range(0, 10):
		n = randint(0, 7)
		pen.seth(0) # east
		pen.color(color_list[n])
		pen.begin_fill()
		pen.circle(10)
		pen.end_fill()
		pen.penup()
		pen.forward(70)
	y += 70
	pen.setposition(x, y) 
	for i in range(0, 10):
		n = randint(0, 7)
		pen.seth(0) # east
		pen.color(color_list[n])
		pen.begin_fill()
		pen.circle(10)
		pen.end_fill()
		pen.penup()
		pen.forward(70)
	y += 70
	pen.setposition(x, y) 
	go += 1






screen.exitonclick
