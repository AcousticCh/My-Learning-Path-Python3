#!usr/bin/env python3
from turtle import Turtle, Screen
pen = Turtle()
screen = Screen()


def move_forward():
	pen.forward(10)
	

def move_backward():
	pen.backward(10)


def turn_right():
	pen.right(10)


def turn_left():
	pen.left(10)
	

def turn_move():
	pen.forward(10)
	pen.right(10)
	

def clear():
	pen.penup()
	pen.clear()
	pen.seth(0)
	pen.setpos(0, 0)
	pen.pendown()


screen.listen()

	
screen.onkey(fun = move_forward, key = "w")
screen.onkey(fun = move_backward, key = "s")
screen.onkey(fun = turn_right, key = "d")
screen.onkey(fun = turn_left, key = "a")
screen.onkey(fun = clear, key = "c")




screen.exitonclick()
