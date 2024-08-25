while True:
  try:
    age = int(input("Age: "))
    print(10/age)
    # to throw my own error 
    raise ValueError('Invalid value')
  except ZeroDivisionError:
    print('Please enter age greater than 0.')
  else:
    # else run when no exception is raised
    print('Thank you.')
    break
  finally:
    # run regardless at the end of everything 
    print('End of program')

