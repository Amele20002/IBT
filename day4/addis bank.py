class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount

    def statement(self):
        print("Owner:", self.owner)
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance, "ETB")


# Create an account
account1 = Account("Almaz", 1001, 1500)

# Show statement
account1.statement()

# Deposit money
account1.deposit(500)

# Withdraw money
account1.withdraw(300)

print("\nAfter Transactions:")
account1.statement()

# Read balance using @property
print("\nCurrent Balance:", account1.balance, "ETB")