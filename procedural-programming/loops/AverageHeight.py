print('welcome to average height calculator\n')
print('input students age seprated by comma\n')

student_heights = input("Input a list of student heights\n: ").split(',')




# print(student_heights)



# for n in range(0, len(student_heights)):
  # student_heights[n] = int(student_heights[n])
  # print(f"length of list is {len(student_heights)}")
  # print(f"height of list is {student_heights[n]}")

# to get total height 
total_height = 0

for height in student_heights:
  total_height += int(height)

print(f"total height is {total_height}")

# to get number of students
students_length = 0

for student in student_heights:
  students_length += 1

print(f"length of list is {students_length}")

average_height = round(total_height / students_length)

print(average_height)