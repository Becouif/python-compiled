some_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

duplicates = []

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)

duplicates2 = [x for x in some_list if some_list.count(x) >1]

print(duplicates2)