# LIST, SET, Dictionary 
my_list = [char for char in 'hello']

my_list2 = [num for num in range(0,100)]

my_list3 = [num *2 for num in range(0,100)]

my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]

# print(my_list4)

#Dictionary 

# my_dict = {key: value**2}

simple_dict = {
  'a':1,
  'b':2
}


my_dict = {k:v**2 for k,v in simple_dict.items() if v%2 == 0}

my_dict2 = {num:num*2 for num in [1,2,3]}


print(my_dict)