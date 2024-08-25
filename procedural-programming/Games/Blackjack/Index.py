import random
import os

from Art import logo


clear = lambda: os.system('cls')



print("Welcome to Blackjack")

# deal_card how to do it
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card= random.choice(cards)
  return card


def calculate_score(cards):
  score = sum(cards)

  # if 11 in cards and 10 in cards and len(cards) == 2:
  if score == 21 and len(cards) == 2:
    return 0
  
  if score > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)

  return score


def compare(user_score,computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "You Lose, computer has Backjack"
  elif user_score == 0:
    return "You win with a Blackjack"
  elif user_score > 21:
    return "You went over. You Lose"
  elif computer_score > user_score:
    return "You lose"
  else:
    return "You win"
  


def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False


  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())




  # hint 6 

  # start of calculate score function logic 


  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}\n")
    print(f"Computer's first card: {computer_cards[0]}\n")


    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  # compare(user_score,computer_score)
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score,computer_score))


restart = input("Do you want to play again? Type 'y' or 'n': ")
while restart == "y":
  clear()
  play_game()
  # restart = input("Do you want to play again? Type 'y' or 'n': ")




