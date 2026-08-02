# ----------------------------
# Observer
# ----------------------------

class SMSAlert:

    def update(self, message):
        print(f"SMS ALERT: {message}")


# ----------------------------
# Alert Service (SRP)
# ----------------------------

class AlertService:

    @staticmethod
    def notify(account, message):
        account._notify(message)


# ----------------------------
# Base Account
# ----------------------------

class Account:

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance
        self._observers = []

    @property
    def balance(self):
        return self._balance

    # Observer methods

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):
        for observer in self._observers:
            observer.update(message)

    # Banking methods

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount

        AlertService.notify(
            self,
            f"{amount} ETB deposited into {self.account_number}"
        )

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount

        AlertService.notify(
            self,
            f"{amount} ETB withdrawn from {self.account_number}"
        )

    def statement(self):

        print("\n------ Statement ------")
        print("Owner:", self.owner)
        print("Account:", self.account_number)
        print("Balance:", self.balance, "ETB")


# ----------------------------
# Savings Account
# ----------------------------

class SavingsAccount(Account):

    def __init__(self, owner, account_number, balance=0, interest_rate=0.05):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):

        interest = self.balance * self.interest_rate
        self._balance += interest

        AlertService.notify(
            self,
            f"Interest Added: {interest:.2f} ETB"
        )


# ----------------------------
# Current Account
# ----------------------------

class CurrentAccount(Account):

    def __init__(self, owner, account_number, balance=0, overdraft_limit=500):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")

        self._balance -= amount

        AlertService.notify(
            self,
            f"{amount} ETB withdrawn from {self.account_number}"
        )


# ----------------------------
# Factory Pattern
# ----------------------------

class AccountFactory:

    @staticmethod
    def create(kind, owner, account_number, balance):

        if kind.lower() == "saving":
            return SavingsAccount(owner, account_number, balance)

        elif kind.lower() == "current":
            return CurrentAccount(owner, account_number, balance)

        else:
            raise ValueError("Unknown account type")


# ----------------------------
# Main Program
# ----------------------------

sms = SMSAlert()

saving = AccountFactory.create(
    "saving",
    "Almaz",
    "1001",
    2000
)

saving.subscribe(sms)

saving.deposit(500)
saving.withdraw(300)
saving.add_interest()
saving.statement()

print()

current = AccountFactory.create(
    "current",
    "Dawit",
    "1002",
    1000
)

current.subscribe(sms)

current.withdraw(1200)
current.deposit(400)
current.statement()