'''
Bankroll. Keeping track of player money balance
'''

class Bankroll ():

    def __init__(self, starting_amount = 0):
        self.balance = starting_amount

    def __str__(self):
        return f'{self.balance}'

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount <= self.balance:
            self.balance = self.balance - withdrawal_amount
            print(self.balance)
            return withdrawal_amount
        else:
            return 0

    def add_to_amount(self, amount):
        self.balance = self.balance + amount