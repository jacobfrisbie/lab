class Account:
    def __init__(self, name):  # Create objects inside Account class
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):  # Deposit method adds to the account balance
        if amount > 0:
            self.__account_balance = self.__account_balance + amount  # Add amount deposited to account balance
            return True
        else:
            return False

    def withdraw(self, amount):  # Withdraw method withdraws from the account balance
        if amount > 0:  # Check the account for a positive balance
            if amount <= self.__account_balance:  # Limiting withdraws to less or equal to account balance
                self.__account_balance = self.__account_balance - amount  # Subtracting amount deposited from balance
                return True
            else:
                return False
        else:
            return False

    def get_balance(self):  # Get balance method to retrieve account balance private variable
        return self.__account_balance

    def get_name(self):  # Get name method to retrieve account name private variable
        return self.__account_name
