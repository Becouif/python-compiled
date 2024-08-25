class User():
  """User class for inheritance"""
  def __init__(self,email):
    # to be able to access this attribute or variable in child class
    # when an attribute is defined in init function
    # it cant be directly accessed in child class 
    self.email = email
  def sign_in(self):
    """Log in the user"""
    print("logged in")

  def attack(self):
    print("do nothing")


# we pass User class as an input to other class to inherit all the methods
class Wizard(User):
  def __init__(self,name,power,email):
    User.__init__(self,email)
    self.name = name
    self.power = power

# since i am passing User class as an input i can inherit all the methods
  def attack(self):
    User.attack(self)
    print(f"attacking with power of {self.power}")

# we can pass user also to other class and the method available in Wizard others 

class Archer(User):
  def __init__(self,name,num_arrows):
    self.name = name
    self.num_arrows = num_arrows


  def attack(self):
    print(f"attacking with arrows: arrows left - {self.num_arrows}")

# GOOD THING TO REMEMBER IS 
# isinstance can be use to check of an obj is an instance of a class
# issubclass can be used to check if a class is a subclass of another class

wizard1 = Wizard("Merlin",50)
# isinstance

print(isinstance(wizard1,Wizard))
# is instance of wizard1 an instance of Wizard class





archer1 = Archer("Robin", 30)

print(wizard1.attack())
print(archer1.attack())
print(archer1.sign_in())


# polymorphism

# by just putting it in a list everything will work and inherit all the methods too 
# by calling one object we can get multiple different response based on previously defined class
for char in [wizard1,archer1]:
  char.attack()