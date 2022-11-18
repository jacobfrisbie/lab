import pytest
from account import account

def test_init():
    account1 = account("Jacob")
    assert account1.getname() == "Jacob"
    assert account1.getbalance() == 0

def test_deposit():
    