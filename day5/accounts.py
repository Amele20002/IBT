class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        print(f"{amount} ETB deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount
        print(f"{amount} ETB withdrawn successfully.")

    def statement(self):
        print("\n----- Account Statement -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self._balance} ETB")


class SavingsAccount(Account):

    def __init__(self, owner, account_number, balance=0, interest_rate=0.05):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self._balance += interest
        print(f"Interest Added: {interest:.2f} ETB")


class CurrentAccount(Account):

    def __init__(self, owner, account_number, balance=0, overdraft_limit=500):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")

        self._balance -= amount
        print(f"{amount} ETB withdrawn successfully.")


# Testing

saving = SavingsAccount("Almaz", "1001", 1500)
saving.deposit(500)
saving.add_interest()
saving.statement()

current = CurrentAccount("Dawit", "1002", 800)
current.withdraw(1000)
current.statement()