#!usr/bin/env python

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {
	
	}


for student in student_scores:
	if student_scores[student] <= 70:
		student_grades.update({student: "Failing"})
	elif student_scores[student] >= 71 and student_scores[student] <= 80:
		student_grades.update({student: "Acceptable"})
	elif student_scores[student] >= 81 and student_scores[student] <=90:
		student_grades.update({student: "Exceeds expectations"})
	elif student_scores[student] >= 91 and student_scores[student] <= 100:
		student_grades.update({student: "Outstanding"})
	
print(student_grades)
