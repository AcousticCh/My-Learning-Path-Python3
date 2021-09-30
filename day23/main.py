#!usr/bin/env python3
from turtle import Screen
from time import sleep
from player import Player
from car_manager import Cars
from levels import Levels
sleep_time = 0.1
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)

P_STARTING_POS = (0, -280)
PLAYER_COLOR = "#000000"
PLAYER_SHAPE = "turtle"
PLAYER_MOVEMENT_GAP = 20
player1 = Player(starting_pos = P_STARTING_POS, player_color = PLAYER_COLOR, player_shape = PLAYER_SHAPE, player_jump = PLAYER_MOVEMENT_GAP)
car = Cars()
level = Levels()

spawn_timer = 0
screen.listen()
game_running = True
while game_running:
	screen.update()
	sleep(sleep_time)
	screen.onkey(player1.move, "w")
	
	spawn_timer += 1
	if spawn_timer >= 6:
		car.generate_car()
		spawn_timer = 0

	car.move()
	if player1.ycor() >= 300:
		car.empty()
		car.car_speed += 2
		level.next_level()
		player1.go_back()
	for i in range(0, len(car.cars)):
		if player1.distance(car.cars[i]) <= 20:
			game_running = False
			level.game_over()
			
			
screen.exitonclick()
