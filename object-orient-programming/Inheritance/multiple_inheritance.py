class User():
  """User class for inheritance"""
  def sign_in(self):
    """Log in the user"""
    print("logged in")

  def attack(self):
    print("do nothing")


# we pass User class as an input to other class to inherit all the methods
class Wizard(User):
  def __init__(self,name,power):
    self.name = name
    self.power = power

# since i am passing User class as an input i can inherit all the methods
  def attack(self):
    User.attack(self)
    print(f"attacking with power of {self.power}")

# we can pass user also to other class and the method available in Wizard others 

class Archer(User):
  def __init__(self,name,arrows):
    self.name = name
    self.arrows = arrows


  def attack(self):
    print(f"attacking with arrows: arrows left - {self.arrows}")

  def run(self):
    return 'ran really fast'


  
class HybridBorg(Wizard,Archer):
  def __init__(self, name,power,arrows):
    Wizard.__init__(self,name,power)
    Archer.__init__(self,name,arrows)



hb1 = HybridBorg('borgie',50,100)

print(hb1.run())

