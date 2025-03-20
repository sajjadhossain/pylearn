# tests/test_bank_account.py
"""
Test Bank Account class methods:
- Balance
- Deposit
- Withdraw
- Check Balance
"""
import pytest
from classes.bank_account import BankAccount

account = BankAccount(1000)

def test_deposit():
    """
    Test that depositing into an account works as expected
    """
    account.deposit(500)
    assert account.check_balance() == "Your balance is: 1500"

def test_withdraw():
    """
    Test that withdrawing from an account works as expected
    """
    account.withdraw(1000)
    assert account.check_balance() == "Your balance is: 500"

def test_check_balance():
    """
    Test that check balance for an account works as expected
    """
    assert account.check_balance() == "Your balance is: 500"

def test_withdraw_over_limit():
    """
    Test that withdrawing more than available from an account returns an error as expected
    """
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(1000)
        