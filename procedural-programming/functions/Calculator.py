
# to clear the console after each bid 
# clear = lambda: print("\033c", end="", flush=True)
from CalculatorLogo import logo

# add 
def add(n1, n2):
  return n1 + n2

# subtract
def subtract(n1, n2):
  return n1 - n2

# multiply

def multiply(n1, n2):
  return n1 * n2

# divide
def divide(n1, n2):
  return n1 / n2

# here we assign each symbol to a function
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide

}





# we make everything a function 
# then we can recall the function when needed

def calculator():
  continue_calculation = True
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  while continue_calculation:
    choice_symbol = input("Pick an operation: ")

    num2 = float(input("What's the second number?: "))
    calculation_function = operations[choice_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {choice_symbol} {num2} = {answer}")

    print(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation\n")
    user_response = input(": ").lower()

    if user_response == 'y':
      num1 == answer

    elif user_response == 'n':
      continue_calculation = False
      print(f"\nThanks for using the calculator, {answer}\n")
      calculator()

    else:
      continue_calculation = False
      print(f"\nThanks for using the calculator, {answer}\n")
      


calculator()