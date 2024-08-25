import random



def run_guess(answer,guess):
    if 0 < guess < 11:
        if guess == answer:
            print("Correct!")
            return True
    else:
        print("Wrong!")
        return False


if __name__ == '__main__':
    answer_generated = random.randint(1,10)

    while True:
        try:
            guess = int(input('guess a number between 1~10: '))
            if (run_guess(answer_generated,guess)):
                break
        except ValueError:
            print("That's not a number!")
            continue
        except TypeError:
            print("That's not a number!")
            continue




