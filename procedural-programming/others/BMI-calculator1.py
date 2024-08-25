print('welcome to BMI calculator\n')

height = input('enter height in meters\n')

weight = input('enter weight in kilogram\n')

# here i want to use is digit to monitor if the input is a number or not



height = float(height)
weight = int(weight)


bmi = weight / (height * height)

bmi = round(bmi, 2)
# bmi = "{:.2f}".format(bmi)
if bmi < 18.5:
  print(f"your BMI is {bmi}, you are underweight")

elif bmi <= 25:
  print(f"your BMI is {bmi}, you have a normal weight")

elif bmi <= 30:
  print(f"your BMI is {bmi}, you are slightly overweight")

elif bmi <= 35:
  print(f"your BMI is {bmi}, you are obese")

else:
  print(f"your BMI is {bmi}, you are clinically obese") 