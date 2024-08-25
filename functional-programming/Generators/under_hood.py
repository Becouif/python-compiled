def special_for(iterable):
  iterator = iter(iterable)
  # when we use iter it allow us to get next(iterator)
  while True:
    try:
      print(iterator)
      print(next(iterator) *2)
    except StopIteration:
      break


special_for([1,2,3])

# range function creation in under_hood

class MyGen():
  current = 0
  def __init__(self,first,last):
    self.first = first
    self.last = last

# makes iterables 
  def __iter__(self):
    return self
  
  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

for i in MyGen(0,100):
  print(i)