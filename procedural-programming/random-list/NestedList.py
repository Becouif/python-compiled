fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
vegetables = ["Potato", "Onion", "Carrot", "Cucumber", "Tomato", "Broccoli", "Cabbage"]

# nested list 
dirty_dozen = [fruits, vegetables]

# using indexing dirty_dozen[1] will access vegetables only 
# while using indexing  dirty_dozen[1][1] will give d element in index 1 on vegetables
# i.e index 1 of index 1 
print(dirty_dozen[0][2])
print(dirty_dozen[1][1])