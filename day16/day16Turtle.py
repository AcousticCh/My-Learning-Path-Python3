#!usr/bin/env python
from turtle import Turtle, Screen

pen = Turtle()
game = Screen()


pen.shape("turtle")
pen.color("red")

pen.forward(100)

print(pen.pos())

game.exitonclick()
