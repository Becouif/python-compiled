# map, filter, reduce and zip 
def multiple_by2(li):
  new_list = []
  for item in li:
    new_list.append(item*2)
  return new_list
  

print(multiple_by2([1,2,3]))
# first functions are pure function without side effects
# this first function has no effect on outside world 
# because it requires no outside function or data


def multiple_bytwo(li):
  new_list = []
  for item in li:
    new_list.append(item*2)
  return print(new_list)

multiple_bytwo([1,2,3])

# this second function has side effects
# we give access to print function from outside world 

# ANOTHER EXAMPLE OF FUNCTION WITH SIDE EFFECTS
new_list = []

def multiple_by3(li):
  for item in li:
    new_list.append(item*3)
  return new_list


print(multiple_by3([1,2,3]))