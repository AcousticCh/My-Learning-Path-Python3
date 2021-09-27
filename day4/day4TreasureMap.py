#!usr/bin/env python

import random

num1 = input("Choose your row [1-5]: ")
num2 = input("Choose your column [1-5]: ")
num1 = int(num1)
num2 = int(num2)
num1 -= 1
num2 -= 1

col_select_0 = ["x", "x", "x", "x", "x",]
col_select_1 = ["x", "x", "x", "x", "x",]
col_select_2 = ["x", "x", "x", "x", "x",]
col_select_3 = ["x", "x", "x", "x", "x",]
col_select_4 = ["x", "x", "x", "x", "x",]

rows = [col_select_0, col_select_1, col_select_2, col_select_3, col_select_4]

rows[num1][num2] = "a"

print(f"{col_select_0}\n{col_select_1}\n{col_select_2}\n{col_select_3}\n{col_select_4}")
