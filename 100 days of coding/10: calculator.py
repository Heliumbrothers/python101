import sys, os
os.system('cls' if os.name == 'sts' else 'clear')
class Calculate:#, operation, number, history)

    def __init__ (self, history):
        self.history = history

    def get_history(self, index):
        '''Get all the calculations that you have made. If index == None, return whole list'''
        if self.history == []:
            return
        else:
            if index == None:
                if self.history == []:
                    return 'No history can be found'
                return self.history

    def clear_history(self):
        self.history = []
    
    def add(self, number1, number2):
        '''Return sum of number1 and number2'''
        return (int(number1) + int(number2))
    
    def multiply(self, number1, number2):
        '''Return number1 * number2'''
        return int(number1) * int(number2)

    def divide(self, number1, number2):
        '''Return number1 / number2'''
        if (int(number1) / int(number2)) % 1 == 0:
            return int(number1) // int(number2)
        else:
            return int(number1) / int(number2)
    
    def subtract(self, number1, number2):
        '''Return number1 - number2'''
        return int(number1) - int(number2)
        
    def modulus(self, number1, number2):
        '''Returns number1 % number2'''
        return int(number1) % (number2)
    
    def power(self, number1, power):
        '''Returns number1 to the power of number2'''
        result = 0
        for i in range(1, int(power)):
            if i == 1:
                result = int(number1) * int(number1)
            else:
                result = result * int(number1)
        return result

    def factorial(self, number1):
        '''Returns number1 factorial'''
        result = 1
        for i in range(1, int(number1) - 1):
            result = result * i
        return i
    def add_history(self, calculation):
        '''Adds calculation to history'''
        self.history.append(calculation)
    



number = Calculate(history=[])
print('Welcome to the Calculator!')
stop = False
while stop != True:
    if stop == True:
        sys.exit()
    operation = input('Type \'+\' to add, \'-\' to subtract, \'*\' to multiply, \'/\' to divide, \'m\' for modulus, \'p\' for power, \'f\' for factorial \'h\' to get history and \'c\' to clear history: ').lower()
    if str(operation) == 'h' or 'c':

        if operation == 'h':
            print(number.get_history(None))
        if operation == 'c':
            number.clear_history()
            print('History cleared')
        continue
    
    if str(operation) == '+' or '-' or '*' or '/':
        number1 = input('Type your first number: ')
        if str(operation) == 'f':
            if operation == 'f':
                print(f'Your answer is {number.factorial(number1)}')
                number.add_history(f'{number1} factorial')

        number2 = input('Type your second number: ')
        if operation == '+':
            print(f'Your answer is {number.add(number1, number2)}')
            number.add_history(f'{number1} - {number2}')
        if operation == '-':
            print(f'Your answer is {number.subtract(number1, number2)}')
            number.add_history(f'{number1} - {number2}')
        if operation == '*':
            print(f'Your answer is {number.multiply(number1, number2)}')
            number.add_history(f'{number1} * {number2}')
        if operation == '/':
            print(f'Your answer is {number.divide(number1, number2)}')
            number.add_history(f'{number1} / {number2}')
        if operation == 'm':
            print(f'Your answer is {number.modulus(number1, number2)}')
            number.add_history(f'{number1} mod. {number2}')
        if operation == 'p':
            print(f'Your answer is {number.power(number1, number2)}')
            number.add_history(f'{number1} to the power of {number2}')


    if input('Type \'yes\' to continue calculating or \'no\' to stop: ').lower() == 'no':
        sys.exit()
        

