from functools import reduce
# lambda param: action(param)

# we use it for things we wanna do once and forget about it 
my_list = [1,2,3]
print(list(map(lambda item: item *2, my_list)))


print(reduce(lambda acc, item: acc+item, my_list))