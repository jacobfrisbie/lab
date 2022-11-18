import pytest
from account import Account  # Import the Account class from account.py


def test_init():  # Test init method
    testAccount = Account("Jacob")  # Create Account with name "Jacob"
    assert testAccount.get_name() == "Jacob"  # Check the name is Jacob
    assert testAccount.get_balance() == 0  # Check the balance is zero


def test_deposit():  # Test deposit method
    testAccount = Account("Jacob")  # Create the Account
    testAccount.deposit(35)  # Deposit 35 using the deposit method
    assert testAccount.get_balance() == 35  # Check the balance


def test_withdraw():  # Test withdraw method
    testAccount = Account("Jacob")  # Create the Account
    testAccount.deposit(35)
    testAccount.withdraw(15)
    assert testAccount.get_balance() == 20  # Check the balance
