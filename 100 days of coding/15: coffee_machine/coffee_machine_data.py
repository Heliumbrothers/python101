import sys, os, json


menu = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18, "milk": 0},
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    },
    "water": {
        "ingredients": {
            "water": 150,
            "milk": 0,
            "coffee": 0
        },
        "cost": 5
    },
    "milk": {
        "ingredients": {
            "water": 0,
            "milk": 150,
            "coffee": 0
        },
        "price": 15
    }
    
}

USER_LOG_FILENAME = "/Users/stanley/Documents/python101/100 days of coding/coffee_machine_user.json"

attributes = ["water", "coffee", "milk"]


class CoffeeMachine:
    def __init__(
        self, water: int, coffee: int, milk: int, money_made: int, user_history=None
    ):
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.money_made = money_made
        self.user_history = user_history
        if self.user_history != None:
            self.user_history = user_history
        else:
            self.user_history = self.get_data(USER_LOG_FILENAME)

    auth = int("01120364")
    history = {}
    user = {}
    attributes = []
    attributes.append("water")
    attributes.append("coffee")
    attributes.append("milk")
    attributes.append("cost")
    drinks = ["latte", "espresso", "cappuccino"]

    def get_status(self, raw_data:bool):
        if raw_data == False:
            return [
                f"Water remaining = {self.water}",
                f"Coffee remaining = {self.coffee}",
                f"Milk remaining = {self.milk}",
                f"Money made = {self.money_made}",
            ]
        else:
            return [self.water, self.coffee, self.milk, self.money_made]

    def add_water(self, amount):
        self.water += amount

    def add_coffee(self, amount):
        self.coffee += amount

    def add_milk(self, amount):
        self.coffee = amount

    def add_money(self, amount):
        self.money_made += amount

    def remove_transaction(self):
        self.history.pop(len(self.history) - 1)

    def get_data(self, file):
        with open(file, "r") as f:
            data = f.read()
            return data

    def save_data(self, filename, data):
        try:
            with open(filename, "a") as filename:
                filename.write(str(data))
                dict(filename)
        except:
            return
        
    def create_file(self, filename):
        with open(f"{filename}.json", "w") as filename:
            json.dump("", filename)

    def refresh_file(self, filename):
        with open(filename, "w"):
            if isinstance(filename, dict):
                filename.clear()
            if isinstance(filename, str):
                filename = ""
            if isinstance(filename, int):
                filename = 0
            if isinstance(filename, list):
                filename = []

    def check_user(self, user_name):
        if user_name in self.user_history:
            return True
        else:
            return False

    def save_status(self):
        # TODO write a function to save status
        self.save_data(
            "Status", [self.get_status(True), self.user_history, self.history]
        )

    def turn_off(self):
        self.save_status()
        sys.exit("program terminated")

    def refresh(self):
        if input("Enter PW: ") == int(self.auth):
            os.system("cts" if os.name == "sts" else "clear")
            self.save_status()
            self.water = 300
            self.coffee = 100
            self.milk = 200
            self.money_made = 0
            self.history = []
            self.user_history = []
            print("Refreshed!")
        else:
            print("Incorrect PW")
            return

    def get_user_details(self, user):
        if self.check_user(user) == True:
            return self.user_history[self.user_history.index(user)]
        else:
            return KeyError("Item not found")

    def initialize(self):
        self.user_history = self.save_data(
            "Coffee_User_History.json", [self.user_history]
        )
        return self.user_history

    def add(self, data, filename: str):
        with open(filename, mode="w", encoding="utf-8") as filename:
            json.dump(data, filename)

    def ask_for_option(self):
        while True:
            prompt = input(
                "Which operation would you like? [buy/status/refresh/SHUTDOWN]"
            )
            if prompt == "status":
                print(self.get_status(False))
                break
            elif prompt == "refresh":
                self.refresh()
                break
            elif prompt == "SHUTDOWN":
                self.turn_off()
            elif prompt == "buy":
                self.buy_coffee()
                break
            else:
                print("the operation is not recognized, please try again")

    def buy_coffee(self):
        prompt = input(
            "How do you want your coffee? [espresso/latte/cappuccino/water/milk]"
        )

        if self.water - menu[prompt]["ingredients"]["water"] < 0:
            print(f"Sorry, we are out of water")
        elif self.coffee - menu[prompt]["ingredients"]["coffee"] < 0:
            print("Sorry, we are out of coffee")
        elif self.milk - menu[prompt]["ingredients"]["milk"] < 0:
            print("Sorry, we are out of milk")

        cost = menu[prompt]["cost"]
        print(f'The price is {menu[prompt]["cost"]} tokens')
        cont = input("Do you want to continue? y/n: ").lower()
        if cont == "y":
            print(self.user_history)
            print(self.history)

            name = input("What is your name: ")

            if name not in self.user_history:
                self.user["name"] = name
                self.user["tokens"] = int(
                    input("How many tokens are in your CoffeMachine™ account: ")
                )
                print("Your account has been saved!")
                self.save_data(
                   USER_LOG_FILENAME , [self.user["name"], self.user["tokens"]]
                )
                self.user["tokens"] -= int(cost)
                print(self.user)
                self.history[name] = self.user["tokens"]
                print(self.user)
                self.user_history["name"] = self.user

            else:
                print(self.user)
                list(self.user)
                user_details = self.user_history[self.user_history.index(self.user)]
                confirm = (
                    f"Check if these details are correct: {user_details} y/n: "
                ).lower()

                if confirm == "y":
                    self.user_history[name["tokens"]] - cost
                    print("Here is your coffee! Enjoy! ☕")
