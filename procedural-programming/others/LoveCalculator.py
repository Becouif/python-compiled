print('Welcome!!!, its love season')

name1 = input('enter your name\n')
name2 = input('enter your crush name\n')

combined_string = name1 + name2
combined_string = combined_string.lower()

t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

true = t + r + u + e

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

# print(f"your love score is {love_score}")

if (score < 10) or (score > 90):
  print(f'your score is {love_score}, you go together like coke and mentos')

elif (score >= 40) and (score <= 50):
  print(f'your score is {love_score}, you are alright together')

else:
  print(f'your score is {love_score}')