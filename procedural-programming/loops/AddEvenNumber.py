
target = input("Enter the number : ") 

if int(target) >= 1000:
  print("Number should be less than 1000")
  exit()

total_even_number = 0
for i in range(1, int(target)+1):
  if i % 2 == 0:
    total_even_number += i

print(total_even_number);


# another way to implement it 


second_total_number = 0
for i in range(2, int(target)+1, 2):
  second_total_number += i
print(second_total_number)