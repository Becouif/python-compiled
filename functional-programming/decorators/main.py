def hello(func):
  return func()


def greet():
  return "greetings to you my people"

a = hello(greet)

# print(a)


#Decorator

def my_decorator(func):
  def wrap_func():
    print('**********')
    func()
    print('***********')
  return wrap_func

@my_decorator
def hello():
  print('Helloooo')


@my_decorator
def bye():
  print('See ya later')

# my_decorator(bye)()

hello()