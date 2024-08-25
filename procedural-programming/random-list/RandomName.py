print('welcome to the random who will pay among friends\n')



names_string = input("Give me everybody's names, separated by a comma.\n: ")
import random


names = names_string.split(", ")

name_length = len(names)

random_number = random.randint(0, int(name_length))
print(f"{names[random_number]} is going to buy the meal today!")
# print(random_number)
