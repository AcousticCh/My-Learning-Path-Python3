#!usr/bin/env python3
from turtle import Turtle, Screen
import time
from snake import Snake


screen = Screen()

screen.title("Snake Clone")
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
snake = Snake()
	
game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()
	screen.onkey(snake.move_left, "a")
	screen.onkey(snake.move_right, "d")
	screen.onkey(snake.move_up, "w")
	screen.onkey(snake.move_down, "s")
	
	
		


screen.exitonclick()
