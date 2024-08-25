def sum(num1, num2):
  try:
    return num1 + num2
  except TypeError as err:
    print(f"Both must be type Integer {err}")
  except (ValueError, ZeroDivisionError) as err:
    print(f"ValueError or ZeroDivisionError {err}")



print(sum(1,"2"))