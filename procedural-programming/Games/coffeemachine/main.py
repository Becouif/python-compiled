from menu import MENU, resources


is_on = True

money = 0

def is_resource_sufficient(order_ingredients):
  """Returns True when order can be made, False if ingredients are insufficient."""
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True

def process_coins():
  """Returns the total calculated from coins inserted."""
  print("Please insert coins.")
  total = int(input("how many quarters?: ")) * 0.25
  total += int(input("how many dimes?: ")) * 0.1
  total += int(input("how many nickles?: ")) * 0.05
  total += int(input("how many pennies?: ")) * 0.01
  return total

def calculate_resources(order_ingredients):
  """Returns the quantity of resources left after making the order."""
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  return resources


def is_transaction_sucessful(money_received, drink_cost):
  """Return True when payment is accepted, or False if money is insufficient."""
  if money_received >= drink_cost:
    change = round(money_received - drink_cost, 2)
    print(f"Here is ${change} in change.")
    global money
    money += drink_cost
    return True
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False

# cost = MENU["espresso"]["cost"]
# print(cost)

while is_on:
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")
  else:
    pickedMenu = MENU[choice]

    if is_resource_sufficient(pickedMenu["ingredients"]):
      payment = process_coins()
      if is_transaction_sucessful(payment, pickedMenu["cost"]):
        calculate_resources(pickedMenu['ingredients'])
        print(f"Here is your {choice} ☕. Enjoy!")

      # print(f"Here is your {choice} ☕. Enjoy!")
   















