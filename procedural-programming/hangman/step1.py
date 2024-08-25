word_list = ["ardvark", "baboon", "camel"]

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


chosen_word = random.choice(word_list)

word_length = len(chosen_word)

lives = 6

display = []
for letter in chosen_word:
  display.append("_")

print(display)

end_of_game = False

while not end_of_game:
  user_guess = input("guess a letter: ").lower()
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == user_guess:
      display[position] = letter


  if user_guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("you lose")

  print(display)
  if "_" not in display:
    end_of_game = True
    print("you win")


  print(stages[lives])