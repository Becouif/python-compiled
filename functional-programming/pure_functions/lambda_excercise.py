my_list = [5,2,3]
# square 
print(list(map(lambda num: num**2 , my_list)))

# list sorting using the second element in each tuple
a = [(0,2),(4,3),(9,9), (10, -1)]
a.sort(key = lambda x:x[1])

print(a)