# 3 flavours: espresso (50ml water, 18g coffe, £1.50), latte (200ml water, 24g coffe, 150ml milk, £2.50) and cappuccino (250ml water, 24g coffee, 100ml milk, £3.00).
# start with 300ml water, 200ml milk and 100g coffee.
# special functions: 'off' to turn off machine and 'report' to get status.
import coffee_machine_data as coffee

coffee_machine = coffee.CoffeeMachine(300, 100, 200, 0)

coffee_machine.create_file('coffee_machine_user')


#while True:
coffee_machine.ask_for_option()
