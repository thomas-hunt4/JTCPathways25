"""
Banking System

This module contains classes for implementing a simple banking system.
"""

class Account:
    """
    Base class for bank accounts.
    
    Attributes:
        account_number (str): Unique identifier for the account
        holder_name (str): Name of the account holder
        balance (float): Current account balance
    """
    
    def __init__(self, account_number, holder_name, initial_balance=0.00):

        Account.num = account_number
        Account.name = holder_name
        Account.init_bal = float(initial_balance)
        if initial_balance < 0:
            raise ValueError("Opening balance can not be negative value.")
        """
        Initialize a new bank account.
        
        Args:
            account_number (str): Unique identifier for the account
            holder_name (str): Name of the account holder
            initial_balance (float, optional): Starting balance. Defaults to 0.
        
        Raises:
            ValueError: If initial_balance is negative
        """
        # TODO: Implement this method
        pass
    
    def deposit(self, amount):
        self.addfunds = float(amount)
        new_bal = self.addfunds + Account.init_bal 
        if new_bal > self.init_bal:
            return True
            Account.init_bal = new_bal
        else: 
            False 
        
       
        
        """
        Add money to the account.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            bool: True if deposit was successful, False otherwise
            
        Raises:
            ValueError: If amount is not positive
        """
        # TODO: Implement this method
        pass
    
    def withdraw(self, amount):
        self.withdraw = float(amount)
        new_bal = self.init_bal - self.withdraw
        if new_bal < 0:
            raise ValueError("Insufficient funds for this withdraw; Please select a lesser amount.")
        elif new_bal > self.init_bal:
            return new_bal; True
        else:
            False
    

        

        """
        Remove money from the account if sufficient funds are available.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal was successful, False otherwise
            
        Raises:
            ValueError: If amount is not positive
        """
        # TODO: Implement this method
        pass
    
    def get_balance(self):
        self.bal = Account.init_bal
        return self.bal
        

        """
        Get the current balance of the account.
        
        Returns:
            float: Current balance
        """
        # TODO: Implement this method
        pass
    
    def __str__(self):
        """
        Return a string representation of the account.
        
        Returns:
            str: Account information
        """
        # TODO: Implement this method
        pass


class Bank:
    """
    Class representing a bank that manages multiple accounts.
    
    Attributes:
        name (str): Name of the bank
        accounts (dict): Dictionary mapping account numbers to Account objects
    """
    
    def __init__(self, name):
        """
        Initialize a new bank with a name.
        
        Args:
            name (str): Name of the bank
        """
        # TODO: Implement this method
        pass
    
    def create_account(self, account_number, holder_name, initial_balance=0):
        """
        Create a new account at this bank.
        
        Args:
            account_number (str): Unique identifier for the account
            holder_name (str): Name of the account holder
            initial_balance (float, optional): Starting balance. Defaults to 0.
            
        Returns:
            Account: The newly created account
            
        Raises:
            ValueError: If an account with the given account_number already exists
        """
        # TODO: Implement this method
        pass
    
    def find_account(self, account_number):
        """
        Find an account by its account number.
        
        Args:
            account_number (str): Account number to search for
            
        Returns:
            Account or None: The account if found, None otherwise
        """
        # TODO: Implement this method
        pass
    
    def transfer(self, from_account_number, to_account_number, amount):
        """
        Transfer money from one account to another.
        
        Args:
            from_account_number (str): Account number to transfer from
            to_account_number (str): Account number to transfer to
            amount (float): Amount to transfer
            
        Returns:
            bool: True if transfer was successful, False otherwise
            
        Raises:
            ValueError: If either account does not exist or amount is invalid
        """
        # TODO: Implement this method
        pass
    
    def get_total_assets(self):
        """
        Calculate the total assets (sum of all account balances) in the bank.
        
        Returns:
            float: Total assets
        """
        # TODO: Implement this method
        pass


class SavingsAccount(Account):
    """
    Savings account that earns interest.
    
    Attributes:
        interest_rate (float): Annual interest rate (decimal)
    """
    
    def __init__(self, account_number, holder_name, initial_balance=0, interest_rate=0.01):
        """
        Initialize a new savings account.
        
        Args:
            account_number (str): Unique identifier for the account
            holder_name (str): Name of the account holder
            initial_balance (float, optional): Starting balance. Defaults to 0.
            interest_rate (float, optional): Annual interest rate. Defaults to 0.01 (1%).
        """
        # TODO: Implement this method - hint: use super().__init__() to call the parent constructor
        pass
    
    def apply_interest(self):
        """
        Apply interest to the account balance.
        
        Returns:
            float: Amount of interest added
        """
        # TODO: Implement this method
        pass


def main():
    """
    Main function to demonstrate the banking system.
    """
    # Create a bank
    bank = Bank("Python National Bank")
    
    # Create accounts
    bank.create_account("1001", "Alice Smith", 1000)
    bank.create_account("1002", "Bob Johnson", 500)
    
    # Create a savings account
    savings = SavingsAccount("1003", "Charlie Brown", 1500, 0.025)
    bank.accounts[savings.account_number] = savings
    
    # Perform some transactions
    print("Initial state:")
    for account_number, account in bank.accounts.items():
        print(account)
    
    # Deposit and withdraw
    bank.find_account("1001").deposit(500)
    bank.find_account("1002").withdraw(100)
    
    # Transfer
    bank.transfer("1001", "1002", 200)
    
    # Apply interest to savings account
    interest_earned = bank.find_account("1003").apply_interest()
    print(f"\nInterest earned on savings account: ${interest_earned:.2f}")
    
    # Show final state
    print("\nFinal state:")
    for account_number, account in bank.accounts.items():
        print(account)
    
    # Show total assets
    print(f"\nTotal bank assets: ${bank.get_total_assets():.2f}")


if __name__ == "__main__":
    main()