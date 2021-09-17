#!usr/bin/env python
student_heights = input("List of student heights:\n")
student_heights = student_heights.replace(",", "")
student_height_list = student_heights.split(" ")
student_list = []
added_heights = 0
number_of_heights = 0

for item in student_height_list:
	student_list.append(int(item))
for item in student_list:
	number_of_heights += 1
	added_heights += item
average_heights = added_heights / number_of_heights

print(average_heights)
