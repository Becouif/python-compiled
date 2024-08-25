print("Welcome to rollercoster ticket!!!\n")
print("the following prompt will help to calculate your ticket price\n")

height = int(input("enter your height in cm: "))

bill = 0

if height >= 120:
  print('you can ride the rollercoster')
  age = int(input("enter your age: "))
  if age < 12:
    bill = 5
    print(f'children tickts are ${bill}')
  elif age <= 18:
    bill = 7
    print(f'youths tickets are ${bill}')
  else:
    bill = 12
    print(f'adult tickets are ${bill}')

    want_photo = input("do you want a photo taken? y or n: ")
    want_photo = want_photo.upper()
    if want_photo == 'Y':
      bill += 3
      print('$3 added to your bill')
      print(f'total bill is ${bill}')

    else:
      print(f'total bill is ${bill}')
      print('no photo taken')

else:
  print('you have to grow taller before you can ride the rollercoster')