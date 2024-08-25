# Local Scope 

def drink_potion():
  # this is a local scope 
  # it will not be access outside of the function
  potion_strength = 2
  print(potion_strength)


drink_potion()
# print(potion_strength)

# global scope 
health = 10

def increase_health():
  print(health)


increase_health()


# There is no Block Scope in py 

# if you create a variable within loops, if statement it is still global variables 
game_level = 3
enemies = ["skeleton", "zombie", "alien"]
if game_level > 3:
  new_enemy = enemies[0]

# you can access new_enemy anywhere in the program
# print(new_enemy)


# MODIFYING A GLOBAL VARIABLE SCOPE WITHOUT USING GLOBAL 

friends = 1

def increase_friends():
  return friends + 1

friends = increase_friends()

print(friends)

# GLOBAL CONSTANTS 

# we make them uppercase to avoid mistakes

PI= 3.14159
