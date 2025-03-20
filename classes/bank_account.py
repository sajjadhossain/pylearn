class BankAccount:

    def __init__(self, balance):

        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if amount > self.balance:

            raise ValueError("Insufficient funds")

        self.balance -= amount

    def check_balance(self):

        print("Your balance is: ", self.balance)