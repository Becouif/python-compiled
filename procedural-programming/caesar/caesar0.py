
# simple function 
def greet():
  for n in range(3):
    print(f"Welcome to Blessing space\n")
    print(f"say hi\n")

greet()


# function with input parameter 
def greet_with_name(name):
  print(f"{name} Welcome to Blessing space \n")
  print(f"say hi to {name}\n")


username = input("Enter your name: ")
greet_with_name(username)



def greet_with(name, location):
  print(f"Hello {name}")
  print(f"the location is {location}")


greet_with(username, "Nigeria")

greet_with(location="nigeria", name=username)