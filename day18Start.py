#!usr/bin/env python
from turtle import Turtle, Screen

pen = Turtle()
def draw_square(height, width):
	for i in range(0, 2):
		pen.forward(width)
		pen.right(90)
		pen.forward(height)
		pen.right(90)


def draw_dotted_line(distance):
	length = round(distance / 10)
	for i in range(0, length):
		pen.forward(5)
		pen.penup()
		pen.forward(5)
		pen.pendown()
	
	
draw_dotted_line(200)
screen = Screen()
screen.exitonclick()
