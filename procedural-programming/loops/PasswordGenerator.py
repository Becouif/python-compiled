import random
letterslist = [
  'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numberslist = ['0','1','2','3','4','5','6','7','8','9']


symbolslist = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to password generator\n")


nr_letters = int(input("How many letters would you like in your password?\n"))

nr_numbers = int(input("How many numbers would you like in your password?\n"))

nr_symbols = int(input("How many symbols would you like in your password?\n"))



password = ""


for letters in range(0, nr_letters):
  password += random.choice(letterslist)
for numbers in range(0, nr_numbers):
  password += random.choice(numberslist)
for symbols in range(0, nr_symbols):
  password += random.choice(symbolslist)

print("Your password is:\n  ")
password = str(password)
print(password)



# Hard level 
password_list = []


for letters in range(0, nr_letters):
  password_list.append(random.choice(letterslist))


for numbers in range(0, nr_numbers):
  password_list.append(random.choice(numberslist))


for symbols in range(0, nr_symbols):
  password_list.append(random.choice(symbolslist))



random.shuffle(password_list)
# print(password_list)

password_second =""

for char in password_list:
  password_second += char

print(f"Your password is: {password_second}")