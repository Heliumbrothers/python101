pin = int(input('Enter PIN'))

class CreditCard:
 #”””A consumer credit card.”””

    def __init__ (self, customer, bank, account, limit, balance):
        self.customer = customer
        self.bank = bank
        if balance is not None and balance > 0:
           self.balance = balance
        else:
            raise ValueError
        if isinstance(account, int) and isinstance(limit, int or float) == True:
            self.account = account
            self.limit = limit



    def get_customer(self):
 #”””Return name of the customer.”””
        return self.customer

    def get_bank(self):
 #”””Return the bank's name.”””
        return self.bank

    def get_account(self):
 #”””Return the card identifying number (typically stored as a string).”””
        return self.account

    def get_limit(self):
#”””Return current credit limit.”””
        return self.limit

    def get_balance(self):
#”””Return current balance.”””
        return self.balance
    

    def charge(self, amount_in_GBP):
        if not(self.balance + amount_in_GBP > self.limit):
            if isinstance(amount_in_GBP, float) and amount_in_GBP >= 0.00:
                self.balance += amount_in_GBP
                return self.balance
            else:
                raise ValueError('Enter a number')
        else:
            raise ValueError('You have gone over your credit card limit')
        

    def pay(self, amount_in_GBP):
        if not(self.balance - amount_in_GBP <0.00):
            if isinstance(amount_in_GBP, float) and amount_in_GBP >= 0.00:
                self.balance -= amount_in_GBP
                return self.balance
            else:
                raise ValueError('Enter a number')
        else:
            raise ValueError('You do not have enough cash to fullfil the transaction')
            

        
#################################################################################################
#################################################################################################


print('Enter PIN')
card = CreditCard('Bob', 'Nationwide', 560911118767, 50, 1.00)
print('Charging account number ' + str(card.get_account()) + ' a certain amount')
card.pay(2.00)
print(card.get_balance())
print(card.get_account())
print(card.get_bank())
print(card.get_customer())
print(card.get_limit())