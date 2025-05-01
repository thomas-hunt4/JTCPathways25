

# class Book:



#     def __init__(self, title, author, pages, year_pub, checked_out = False ):

#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.yrpub = year_pub
#         self.chkout = checked_out



#     def book_checkout(self):
#         if self.chkout == True:
#             print(f'{self.title} is available to checkout ')
#         else:
#             self.chkout == False
#             print(f'{self.title}')





        
            
        
        

    




#         pass

# # Activity: In pairs, create a Book class with the following requirements:
# # Attributes for title, author, pages, and year published
# # A boolean attribute checked_out that defaults to False
# # Methods to:
# # Check out the book (if not already checked out)
# # Return the book (if currently checked out)
# # Add a review (store in a list of reviews)
# # Get the average review rating (if reviews exist)
# # Create a small library of at least 3 books and demonstrate all functionality



# # class Student:
# #     school_name = "Yo JTC raps"
# #     total_students = 0

# #     def __init__(self, name, grade):
# #         self.name = name 
# #         self.grade = grade


# #         Student.total_students =+ 1


# #     def display_info(self):
# #         print(f"Name: {self.name}, Grade: {self.grade}, School: {self.school_name}")


# # alice = Student("Alice", 95)
# # bOb = Student('Bob", 87)
              

# # print(f'School name: {Student.school_name}')


# #         pass


# class Counter:
#     count = 0

#     def __init__(self):
#         self.count =+ 1



# c1 = Counter()
# # c2 = Counter()
        

# print(Counter.count)




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



