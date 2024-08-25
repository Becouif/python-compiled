student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score > 100:
    student_grades[student] = "Invalid Score"
  elif score in range(91,101):
    student_grades[student] = "Outstanding"
  elif score in range(81,91):
    student_grades[student] = "Exceeds Expectations"
  elif score in range(71,81):
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"


print(student_grades)