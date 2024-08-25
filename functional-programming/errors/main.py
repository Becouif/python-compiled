while True:
  try:
    age = int(input("Age: "))
    print(10/age)
    
  except ValueError:
    print('Please enter a number for age.')
  except ZeroDivisionError:
    print('Please enter age greater than 0.')
  else:
    # else run when no exception is raised
    print('Thank you.')
    break
  finally:
    # run regardless at the end of everything 
    print('End of program')

