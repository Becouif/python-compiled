from random import randint
# generate anumber 1-10
answer = randint(1,10)
#input from user 



#check that input is a number 1-10
while True:
  try:
  # if guess < 1 or guess > 10:
    guess = int(input("Guess a number between 1 and 10: "))
    if 0 < guess <11:
      if guess == answer:
        print("You got it!")
        break
    else:
      print("Invalid input, i said 1~10")
  except ValueError:
    print(f"I said enter number")  

# check if number is the right guess, otherwise ask again


