import random

answer = random.randint(1,10)

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if 0 < guess < 11:
            if guess == answer:
                print("Correct!")
                break
        else:
            print("Wrong!")
    except ValueError:
        print("That's not a number!")
        continue