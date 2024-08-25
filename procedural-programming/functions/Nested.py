def outer_functino(a,b):
  def inner_function(c,d):
    return c+d
  return inner_function(a,b)

result = outer_functino(1,2)
print(result)