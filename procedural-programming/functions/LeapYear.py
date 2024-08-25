

def is_leap(year):
  """ Take in year (int) and return true if leap year, false if not


  """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  


user_entered_year = int(input("Enter a year: "))

def days_in_months(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]



year = int(input("Enter a year: "))
month =int(input("Enter a month: "))
days = days_in_months(year, month)
print(days)




