n = int(input("Enter a number: "))

def prime(n):
  if n == 1:
    print("1 is not a prime number")
    return False
  
  elif n == 2:
    print("2 is a prime number")
    return True
  else:
    for x in range(2, n):
      if n % x == 0:
        print(f"{n} is not a prime number")
        return False
    print(f"{n} is a prime number")
    return True
  


prime(n)
  