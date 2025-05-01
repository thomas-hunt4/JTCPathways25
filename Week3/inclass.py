

# class Students:



#     def __init__(self, name, student_id, gpa=0.0):

#         self.name = name
#         self.sid = student_id
#         self.gpa = gpa


                 
    


#     def is_honor_roll(self, student_id, gpa=0.0):
#         if self.gpa >= 3.5:
#             return True
#         else:
#             return False
          

        



#     def update_gpa(self, new_gpa):
#         self.gpa = new_gpa

# student1 = Students("Alice", "B3437", 3.7)
# student2 = Students("Bob", "B9763")

# print(student1.gpa)

# student2.update_gpa(3.8)


        
                 
#         pass



class BankAccount:
    bank_name = "Python National Bank"


    def __init__(self, account_number, owner_name, balance = 0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.tranactions = []

        self.tranactions.append(balance)








alice_account = BankAccount("12345", "Bo Jackon", 1000)
blob_account = BankAccount("12457", "Blob Blobberston", 500)



    
        pass



class BankAccount:
    """A class to represent a bank account."""
    
    # Class attribute - shared by all instances
    bank_name = "Python National Bank"
    
    def __init__(self, account_number, owner_name, balance=0):
        """Initialize a new bank account with account details."""
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.transactions = []  # List to track transaction history
        
        # Record opening transaction
        self.transactions.append(f"Account opened with ${balance}")
    
    def deposit(self, amount):
        """Add money to the account balance."""
        if amount <= 0:
            print("Error: Deposit amount must be positive")
            return False
        
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        return True
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds exist."""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
            return False
        
        if amount > self.balance:
            print("Error: Insufficient funds")
            return False
        
        self.balance -= amount
        self.transactions.append(f"Withdrawal: ${amount}")
        return True
    
    def get_balance(self):
        """Return the current account balance."""
        return self.balance
    
    def print_transactions(self):
        """Print the transaction history."""
        print(f"Transaction history for account {self.account_number}:")
        for transaction in self.transactions:
            print(f"- {transaction}")
        print(f"Current balance: ${self.balance}")

# Create some accounts
alice_account = BankAccount("12345", "Alice Johnson", 1000)
bob_account = BankAccount("67890", "Bob Smith", 500)

# Perform some transactions
alice_account.deposit(500)
bob_account.withdraw(200)
alice_account.withdraw(1200)  # Should fail - insufficient funds
alice_account.withdraw(800)   # Should succeed

# Print information
print(f"{alice_account.owner_name}'s balance: ${alice_account.get_balance()}")
print(f"{bob_account.owner_name}'s balance: ${bob_account.get_balance()}")

# Print transaction history
alice_account.print_transactions()

# Demonstrate class attribute
print(f"Both accounts are with {BankAccount.bank_name}")
print(f"Alice's bank: {alice_account.bank_name}")
print(f"Bob's bank: {bob_account.bank_name}")