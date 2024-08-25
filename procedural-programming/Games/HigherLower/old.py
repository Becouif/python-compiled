from game_data import data

from art import logo,vs

import random

# print(data)

still_playing = True

# function for compare
def higher_lower(user_choice, a, b, score, still_playing):
  """ this function take 5 arg, user_choice, a, b, score, still_playing. and compare a and b, increase and show score"""
  if user_choice == "A":
    if a["follower_count"] > b["follower_count"]:
      score + 1
      print(f"You're right! Current score: {score}" )
    elif a["follower_count"] < b["follower_count"]:
      print(f"Sorry, that's wrong. Final score: {score}")
    else:
      still_playing = False
      print(f"That's a tie. Final score: {score}")

      


  elif user_choice == "B":
    if b["follower_count"] > a["follower_count"]:
      score + 1
      print(f"You're right! Current score: {score}" )
    elif b["follower_count"] < a["follower_count"]:
      print(f"Sorry, that's wrong. Final score: {score}")
    else:
      print(f"That's a tie. Final score: {score}")
      still_playing = False



print(logo)




compareA = random.choice(data)
compareB = random.choice(data)

score = 0



while still_playing:
  if compareA == compareB:
    compareB = random.choice(data)

  print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}")

  print(vs)

  print(f"Compare B: {compareB['name']}, a {compareB['description']}, from {compareA['country']}")


  user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

  higher_lower(user_choice, compareA, compareB, score, still_playing)

  compareA = compareB
  compareB = random.choice(data)






