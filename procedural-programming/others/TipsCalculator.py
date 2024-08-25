print('Welcome to the tips calculator\n')

bill = float(input('What was the total bill?\n'))

tip = int(input('What percentage tip would you like to give? 10, 12, or 15?\n'))


people = int(input('How many people to split the bill?\n'))

tip_percentage = tip / 100

tip_amount = bill * tip_percentage

total_bill = bill + tip_amount 

bill_per_person = total_bill/ people

final_amount = round(bill_per_person, 2)

final_amount = "{:.2f}".format(bill_per_person)

print(f'Each person should pay: ${final_amount} and the total biil is ${total_bill}')