

print('Welcome to the BMI calculator\n')


print('enter weight in kilogram\n')

weight = float(input())

height = float(input('enter height in meters\n'));

bmi = weight / (height * height)

print('your BMI is' + ' '+ str(bmi))