#!usr/bin/env python
from math import ceil
print("What is the surface area of wall")

width = int(input("Width: "))
height = int(input("Height: "))


def cans(width, height):
    paint_cans = ceil((width * height) / 5)

    print(f"Your will need {paint_cans}")
    
cans(width = width, height = height)
