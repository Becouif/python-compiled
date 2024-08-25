# using map take a function that handle what you want to do to each item in a list

my_list = [1,2,3]

def muliply_by2(item):
  return item*2


print(list(map(muliply_by2,my_list)))

# it can be use multiple ways on a list 

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def capitalize(item):

  return item.capitalize()

print(list(map(capitalize,alphabet)))