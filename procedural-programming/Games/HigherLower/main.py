from game_data import data

from art import logo,vs

import random

# print(data)
clear = lambda: print("\033c", end="", flush=True)

still_playing = True

# function for compare
def compare(user_choice, a, b,):
  """ this function take 5 arg, user_choice, a, b, score, still_playing. and compare a and b, increase and show score"""
  if user_choice == "A":
    if a["follower_count"] > b["follower_count"]:
      return True
    elif a["follower_count"] < b["follower_count"]:
      return False
    else:
      return "Tie"

  elif user_choice == "B":
    if b["follower_count"] > a["follower_count"]:
      return True
    elif b["follower_count"] < a["follower_count"]:
      return False
    else:
      return "Tie"


print(logo)




compareA = random.choice(data)
compareB = random.choice(data)

score = 0



while still_playing:
  if compareA == compareB:
    compareB = random.choice(data)

  print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}")

  print(vs)

  print(f"Compare B: {compareB['name']}, a {compareB['description']}, from {compareA['country']}\n")

  user_choice = input("Who has more followers? Type 'A' or 'B': \n").upper()

  answer = compare(user_choice, compareA, compareB)


  clear()
  print(logo)
  if answer == True:
    score +=1
    print(f"You're right! Current score: {score}\n")

    compareA = compareB

    compareB = random.choice(data)
  else:
    still_playing = False
    print(f"You lose. Final score: {score}")










