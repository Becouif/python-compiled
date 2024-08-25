
def generator_function(num):
  for i in range(num):
    yield i*2


gen = generator_function(100)

next(gen)

next(gen)

print(next(gen))

for i in gen:
  print(i)


# making a list instead of generator 

# def make_list(num):
#   result= []
#   for i in range(num):
#     result.append(i*2)
#   return result

# my_list = make_list(100)
# print(list(range(100)))