print("welcome to number guessing game \n")

from art import logo

import random

number = random.randint(1, 100)

print(logo)
print("I'm thinking of a number between 1 and 100\n")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# print(difficulty)
# print(number)
if difficulty == "easy":
  Attempts = 10
elif difficulty == "hard":
  Attempts = 5
else:
  print("Invalid input")
  exit()


while Attempts > 0:
  print(f"You have {Attempts} attempts remaining to guess the number")

  guess = int(input("Make a guess: "))

  if guess == number:
    print(f"Correct\nYou win\n")
    break
  elif guess == 0:
    print("Invalid input")
    exit()
  elif guess > number:
    print("Too high\nTry again\n")
    Attempts -= 1
  elif guess < number:
    print("Too low\nTry again\n")
    Attempts -= 1
  elif guess > 100:
    print(f"{guess} number higher than 100\n")
  else:
    print(f"Invalid guess number {guess}\n")

if Attempts == 0:
  print("sorry you out of attempt\n")
  print(f"the number is {number}")
