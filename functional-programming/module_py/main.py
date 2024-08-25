import utility

import shopping.shopping_cart

from shopping.more_shopping import basket

# this code will make sure that the code is being run from main.py

# i will make sure that this file is the one getting run do something 
if __name__ == '__main__':

  print(utility.multiply(10,20))
  print(shopping.shopping_cart.addCart("apple\n"))
  print(basket.addLetter("enrich"))
  print(__name__)

  print('\n')

  # when we do this we can get d name of the module
  print(type(utility.std1))