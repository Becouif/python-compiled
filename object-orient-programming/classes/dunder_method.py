# dont be EDITING dunger methods 
# but there are cases you want to modify it 
# HERE WE WILL modify str method 
class Toy():
  def __init__(self,color,age):
    self.color = color
    self.age = age
    self.my_dict = {
      'name' : 'harry',
      'has_pets' : False
    }

# here we modifty d str but will be only callable with Toy instances 
  def ___str__(self):
    return f'{self.color}'
  def __len__(self):
    return 5
  
  # this call allow us to directly call instance of d object like  function call
  # e.g action_figure()
  def __call__(self):
    return('yes!')
  
  def __getitem__(self,i):
    return self.my_dict[i]

action_figure = Toy('red', 0)

print(action_figure.___str__())
print(action_figure.__len__())
# this wont work anymore because we have modify __str__ in toy 
# but i still go a result tho 
# it working in latest python i think
print(str(action_figure))

# here we are calling on call function in toy class
print(action_figure())

# here we are calling on getitem function in toy class
print(action_figure['name'])

