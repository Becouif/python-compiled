# basic function 
def my_function():
  print("welcome to my function")


my_function()


# function with input parameter
def another_function(something):
  print(something)


# function with output 
def yet_another_function():
  return "something"


# function with input and output
def function_with_input_and_output(something):
  return something

the_output = function_with_input_and_output("something")



def format_name(first_name, last_name):
  return f"{last_name.title()}, {first_name.title()}"

