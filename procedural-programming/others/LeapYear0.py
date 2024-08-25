print('welcome to leap year calculator\n')

year = int(input('enter a year\n: '))


if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f'{year} is leap year')

    else:
      print('year is not leap year')
  else:
    print(f'{year} is leap year')

else:
  print('year is not leap year')










# if year % 4 == 0:
#   print(f'{year} is leap year')

# elif year % 100 == 0:
#   if year % 400 == 0:
#     print(f'{year} is leap year') 
# else:
#   print('year is not leap year')