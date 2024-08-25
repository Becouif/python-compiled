student_scores = input('input the list of scores: ').split(',')

highest_score = 0
for score in student_scores:
  if int(score) > highest_score:
    highest_score = int(score)
  else:
    highest_score = highest_score

print(f"the highest score in the class is {highest_score}\n")


lowest_score = highest_score

for score in student_scores:
  if int(score) < lowest_score:
    lowest_score = int(score)
  else:
    lowest_score = lowest_score

print(f"the lowest score in the class is {lowest_score}\n")