# building performance decorator 

from time import time

def performance(fn):
  def wrapper(*args, **kawrgs):
    # this monitor d time that d function want to start running 
    t1 = time()
    result = fn(*args, **kawrgs)
    t2 = time()
    # and this monitor the time the function stop running 
    print(f'took {t2-t1} ms')
    return result
  return wrapper


@performance
def long_time():
  for i in range(100000000):
    i * 5


long_time()