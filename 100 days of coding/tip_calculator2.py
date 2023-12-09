alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print('Welcome to the tip calculator')
total_fee = input('What was the total fee?')
for i in range(25):
    if alphabet_list[i] in total_fee != True:
        ValueError('Enter a floating-point number please')
    else:
        float(total_fee)
percentage_tip = float(input('What percentatge tip would you like to give?\n'))
people_to_split_bill = int(input('How many people to split the bill?\n'))
individual_fee = round((total_fee + ((total_fee / 100) * percentage_tip)) / people_to_split_bill, 2)
print(f'Each person should pay £{individual_fee}')
leftover_fee = (total_fee + ((total_fee / 100)) * percentage_tip) % people_to_split_bill
if (total_fee + ((total_fee / 100))) % people_to_split_bill != 0:
    print(f'However, {round(leftover_fee)} people will have to pay 1p extra')