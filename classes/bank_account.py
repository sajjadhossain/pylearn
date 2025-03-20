# classes/bank_account.py
"""
Bank Account class with access to:
- Balance
- Deposit
- Withdraw
- Check Balance
"""
from typing import Union
class BankAccount:
    """
    This class will allow users to access the main methods for the bank account
    """
    def __init__(self, balance: int) -> int:
        self.balance = balance

    def deposit(self, amount: int) -> int:
        """
        Make a deposit, add the amount deposited to the balance
        """
        self.balance += amount

    def withdraw(self, amount: int) -> Union[int, str]:
        """
        Make a withdrawl, subract the amount deposited to the balance
        If the amount requested is more than the balance, return error
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    def check_balance(self) -> str:
        """
        Check the balance
        """
        return "Your balance is: " + str(self.balance)
    