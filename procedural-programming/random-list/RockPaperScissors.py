print("Welcome to rock paper scissors game\n")
print('what do you choose? type 0 for rock, 1 for paper or 2 for scissors\n')

import random

computer_number = random.randint(0, 2)
user_input = int(input(": "))



game = ['rock', 'paper', 'scissors']


rock = '''    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\. '''


paper = '''  '''




if user_input >= 3 or user_input < 0:
  print('you typed an invalid number, you lose')
else:
  computer_choice = game[computer_number]
  user_choice = game[user_input]
  print(f'you chose {game[user_input]}')
  print(f'computer chose {computer_choice}')

  if user_input == computer_number:
    print('it is a tie')

  elif user_input == 0 and computer_number == 3:
    print("you win")
    print(f'{user_choice} wins')

  elif user_input > computer_number:
    print("You win\n")


  elif computer_number > user_input:
    print("you lose\n")

  elif user_input == 1 and computer_choice == 0:
    print("you win\n")
    print(f'{user_choice} wins')

  elif user_input == 2 and computer_choice == 1:
    print("you win\n")
    print(f'{user_choice} wins')
  else:
    print("you lose\n")


