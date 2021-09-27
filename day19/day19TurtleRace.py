#!usr/bin/env python3
from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(height = 400, width = 500)
orange_turtle = Turtle()
purple_turtle = Turtle()
yellow_turtle = Turtle()
green_turtle = Turtle()
red_turtle = Turtle()
blue_turtle = Turtle()

orange_turtle.penup()
blue_turtle.penup()
green_turtle.penup()
red_turtle.penup()
purple_turtle.penup()
yellow_turtle.penup()

orange_turtle.setpos(-240, -125)
blue_turtle.setpos(-240, -75)
green_turtle.setpos(-240, -25)
red_turtle.setpos(-240, 25)
yellow_turtle.setpos(-240, 75)
purple_turtle.setpos(-240, 125)

purple_turtle.color("purple")
orange_turtle.color("orange")
blue_turtle.color("blue")
green_turtle.color("green")
red_turtle.color("red")
yellow_turtle.color("yellow")

purple_turtle.shape("turtle")
orange_turtle.shape("turtle")
blue_turtle.shape("turtle")
green_turtle.shape("turtle")
red_turtle.shape("turtle")
yellow_turtle.shape("turtle")

bet = screen.textinput("Turtle Race", "Choose your color, who will win!")


def purple_race():
	n = randint(1, 10)
	purple_turtle.forward(n)
	
	
def orange_race():
	n = randint(1, 10)
	orange_turtle.forward(n)
	
	
def blue_race():
	n = randint(1, 10)
	blue_turtle.forward(n)
	
	
def green_race():
	n = randint(1, 10)
	green_turtle.forward(n)
	
	
def red_race():
	n = randint(1, 10)
	red_turtle.forward(n)
	
	
def yellow_race():
	n = randint(1, 10)
	yellow_turtle.forward(n)
	
	
winner = ""
line_crossed = "False"
while line_crossed == "False":
	if purple_turtle.xcor() >= 230:
		winner = "purple"
		line_crossed = "True"
	elif orange_turtle.xcor() >= 230:
		winner = "orange"
		line_crossed = "True"
	elif blue_turtle.xcor() >= 230:
		winner = "blue"
		line_crossed = "True"
	elif green_turtle.xcor() >= 230:
		winner = "green"
		line_crossed = "True"
	elif red_turtle.xcor() >= 230:
		winner = "red"
		line_crossed = "True"
	elif yellow_turtle.xcor() >= 230:
		winner = "yellow"
		line_crossed = "True"
	
	purple_race()
	orange_race()
	blue_race()
	green_race()
	red_race()
	yellow_race()
	
if bet == winner:
	print(f"You win! Winner is {winner}")
else:
	print(f"you lose, winner is {winner}")
screen.exitonclick()
