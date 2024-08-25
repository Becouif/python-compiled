print('welcome to pizza ordering system\n')
print('please select your pizza size\n')
print('small (S)\nmedium (M)\nlarge(L)\n')

size = input('enter your choice\n')

size = size.upper()

bill = 0

if size == 'S':
  bill = 15
  # print(f'your bill is ${bill}')
  # add topping or not to the bill
  pepperoni = input('do you want pepperoni? Y or N\n')
  pepperoni = pepperoni.upper()
  if pepperoni == "Y":
    bill += 2
    print(f'your current bill is ${bill}')
  # end of if statement for pepperoni
  extra_cheese = input('do you want extra cheese? Y or N\n')
  extra_cheese = extra_cheese.upper()
  if extra_cheese == "Y":
    bill += 1
    print(f'your current bill is ${bill}')

  print(f"your final bill is ${bill}")
# start of else if for the medium size 
elif size == 'M':
  bill = 20
  # print(f'your bill is ${bill}')
  # add topping for midium size
  pepperoni = input('do you want pepperoni? Y or N\n')
  pepperoni = pepperoni.upper()
  if pepperoni == "Y":
    bill += 3
    print(f'your current bill is ${bill}')
  # end of if statement for pepperoni
  extra_cheese = input('do you want extra cheese? Y or N\n')
  extra_cheese = extra_cheese.upper()
  if extra_cheese == "Y":
    bill += 1
    print(f'your current bill is ${bill}')

  print(f"your final bill is ${bill}")

# start of large size 
elif size == 'L':
  bill = 25
  # print(f'your bill is ${bill}')
  # add topping for large size
  pepperoni = input('do you want pepperoni? Y or N\n')
  pepperoni = pepperoni.upper()
  if pepperoni == "Y":
    bill += 3
    print(f'your current bill is ${bill}')
  # end of if statement for pepperoni
  extra_cheese = input('do you want extra cheese? Y or N\n')
  extra_cheese = extra_cheese.upper()
  if extra_cheese == "Y":
    bill += 1
    print(f'your current bill is ${bill}')

  print(f"your final bill is ${bill}")
else:
  print('invalid input')

  print('thanks for ordering')
