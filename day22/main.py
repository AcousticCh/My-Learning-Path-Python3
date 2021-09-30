#!usr/bin/env python3
from turtle import Screen, Turtle
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from random import randint

first_score_pos = -50
second_score_pos = 40
BACKGROUND_COLOR = "#000000"
LINE_COLOR = "#FFFFFF"

def setup_background(bgcolor, lcolor):
	screen = Screen()
	screen.setup(width = 800, height = 600)
	screen.bgcolor(bgcolor)
	screen.tracer(0)
	background_pen = Turtle()
	background_pen.speed(0)
	background_pen.ht()
	background_pen.pencolor(lcolor)
	background_pen.width(5)
	background_pen.penup()
	background_pen.setheading(90)
	background_pen.goto(0, -288)
	
	
	
	
	while background_pen.ycor() <= 300:
		background_pen.pendown()
		background_pen.forward(20)
		background_pen.penup()
		background_pen.forward(20)
		
	return screen
	
	
screen = setup_background(bgcolor = BACKGROUND_COLOR, lcolor = LINE_COLOR)
player1 = Paddle()
player2 = Paddle()
ball = Ball()
player1_score = ScoreBoard(first_score_pos)
player2_score = ScoreBoard(second_score_pos)
player1.player_1()
player2.player_2()
ball.start_ball()
screen.listen()
game_running = True
while game_running:
	screen.update()
	sleep(0.1)
	screen.onkey(player1.move_up, "w")
	screen.onkey(player1.move_down, "s")
	screen.onkey(player2.move_up, "Up")
	screen.onkey(player2.move_down, "Down")
	ball.bounce()
	ball.hit(player1.pen)
	ball.hit(player2.pen)
	if ball.miss() == "right":
		player1_score.add_point()
		if player1_score.points == 10:
			game_running = False
	if ball.miss2() == "left":
		player2_score.add_point()
		if player2_score.points == 10:
			game_running = False
	
	ball.ball_move()
	
	
if player1_score.points > player2_score.points:
	player1_score.goto(12, 0)
	player1_score.write("Game over!  Left side wins", align = "center", font = ("Arial", 20, "normal"))
elif player2_score.points > player1_score.points:
	player2_score.goto(20, 0)
	player2_score.write("Game over!  Right side wins", align = "center", font = ("Arial", 20, "normal"))

screen.exitonclick()
