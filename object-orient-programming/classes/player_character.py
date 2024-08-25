class PlayerCharacter:
  """take in name and age as defualt values"""
  # class object attribute 
  membership = True

  # constructor
  # will be run with the instanciated object
  def __init__(self,name="anonymous",age =0):
    if(age > 18):
      self.name = name #attributes
      self._age = age

  def run(self): #methods
    print(f"{self.name} is running")
    return "done"

  # class methods can be called without instanciating the object 
  # can also be called decorators 
  # cls is like self
  # in static method we dont have access to d object (cls)
  @classmethod
  def adding_things(cls,num1,num2):
    return cls("Teddy",num1+num2)
    # return num1 + num2
  











player1 = PlayerCharacter("Tom", 20)
player2 = PlayerCharacter("Jerry", 19)
# using the class method we can add different attributes
player3 = PlayerCharacter.adding_things(2,3)

print(player3)
player1.attack = 50

print(player1.attack)
print(player1.name)
print(player1.run())

print(player2.name)