my_list = [1,2,3,4,5,6,7,8,9,10]

# we use a function that will evaluate into a boolean expression 
def odd(item):
  return item %2 != 0


print(list(filter(odd,my_list)))

# filter through things in a list

# d function take a parameter of each element in filter 