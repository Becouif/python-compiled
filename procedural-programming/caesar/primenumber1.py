def prime_number(n):
  is_prime = True;

  for i in range(2, n):
    if n % i == 0:
      is_prime = False;
      break;
  if is_prime:
    print(f"{n} is a prime number.")
  else:
    print(f"{n} is not a prime number.")


user_number = int(input("Enter a number: "))
prime_number(user_number)