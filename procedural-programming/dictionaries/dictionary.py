programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again",
  "Loop": "The action of doing something over and over again",
  "List": "A collection of items in a particular order",
  "Dictionary": "A collection of key-value pairs in a particular order",
  "Tuple": "A collection of items in a particular order, but they can't be changed",
  123: "The number 123",
}

# dictionary is key and value 

# retrieving an item 
print(programming_dictionary["Bug"])
print(programming_dictionary[123])


# adding new items
programming_dictionary["Time"] = "The amount of time that has passed"
print(programming_dictionary)


# creating an empty dictionary
empty_dictionary = {}


# wipe and existing dict 
programming_dictionary = {}

print(programming_dictionary)

# edit a value in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)


# looping through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

