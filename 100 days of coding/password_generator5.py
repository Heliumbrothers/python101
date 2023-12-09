import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '£', '$', '%', '^', '&', '*', '(', ')']
alphabet_count = 0
num_count = 0
symbol_count = 0

print('Welcome to the password generator!')
number_of_letters = int(input('How many letters do you want in your password: '))
number_of_numbers = int(input('How many numbers do you want in your password: '))
number_of_symbols = int(input('How many symbols do you want in your password: '))
password = ''

for i in range(0, (number_of_letters + number_of_numbers + number_of_symbols)):
    if random.randint(0, 2) == 0 and alphabet_count != number_of_letters:
        password += (alphabet[random.randint(0, 25)])
    if random.randint(0, 2) == 1 and num_count != number_of_numbers:
        password += (numbers[random.randint(0, 9)])
    if random.randint(0, 2) == 2 and symbol_count != number_of_symbols:
        password += (symbols[random.randint(0, 9)])

print(str(password))
