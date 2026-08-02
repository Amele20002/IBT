# --------------------------
# Observer
# --------------------------

class SMSAlert:

    def update(self, message):
        print("SMS:", message)


# --------------------------
# Alert Service
# --------------------------

class AlertService:

    @staticmethod
    def notify(account, message):
        account._notify(message)


# --------------------------
# Base Account
# --------------------------

class Account:

    def __init__(self, owner, account_number, balance=0):

        self.owner = owner
        self.account_number = account_number
        self._balance = balance

        self._observers = []

        # Transaction history (STACK)
        self.history = []

    @property
    def balance(self):
        return self._balance

    # ------------------
    # Observer
    # ------------------

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):
        for observer in self._observers:
            observer.update(message)

    # ------------------
    # Deposit
    # ------------------

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

        # Save transaction
        self.history.append(("deposit", amount))

        AlertService.notify(
            self,
            f"Deposited {amount} ETB"
        )

    # ------------------
    # Withdraw
    # ------------------

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount

        self.history.append(("withdraw", amount))

        AlertService.notify(
            self,
            f"Withdrew {amount} ETB"
        )

    # ------------------
    # Undo Last
    # ------------------

    def undo_last(self):

        if not self.history:
            print("No transactions to undo.")
            return

        action, amount = self.history.pop()

        if action == "deposit":
            self._balance -= amount

        elif action == "withdraw":
            self._balance += amount

        print(f"Undo successful: {action} {amount} ETB")

    # ------------------
    # Statement
    # ------------------

    def statement(self):

        print("\n------ Statement ------")
        print("Owner:", self.owner)
        print("Account:", self.account_number)
        print("Balance:", self.balance, "ETB")


# --------------------------
# Savings Account
# --------------------------

class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)


# --------------------------
# Current Account
# --------------------------

class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0, overdraft=500):

        super().__init__(owner, number, balance)

        self.overdraft = overdraft

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance + self.overdraft:
            raise ValueError("Overdraft exceeded")

        self._balance -= amount

        self.history.append(("withdraw", amount))

        AlertService.notify(
            self,
            f"Withdrew {amount} ETB"
        )


# --------------------------
# Factory
# --------------------------

class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance):

        if kind.lower() == "saving":
            return SavingsAccount(owner, number, balance)

        elif kind.lower() == "current":
            return CurrentAccount(owner, number, balance)

        else:
            raise ValueError("Unknown account type")


# --------------------------
# Registry
# --------------------------

class AccountRegistry:

    def __init__(self):

        self.accounts = {}

    def add(self, account):

        self.accounts[account.account_number] = account

    def find(self, number):

        return self.accounts.get(number)

    def list_all(self):

        for number in sorted(self.accounts):

            account = self.accounts[number]

            print(
                account.account_number,
                account.owner,
                account.balance
            )


# --------------------------
# Main Program
# --------------------------

sms = SMSAlert()

registry = AccountRegistry()

acc1 = AccountFactory.create(
    "saving",
    "Almaz",
    "1001",
    2000
)

acc2 = AccountFactory.create(
    "current",
    "Dawit",
    "1002",
    1000
)

acc1.subscribe(sms)
acc2.subscribe(sms)

registry.add(acc1)
registry.add(acc2)

acc1.deposit(500)
acc1.withdraw(200)

acc2.deposit(300)

print("\nAccounts")
registry.list_all()

print("\nFinding account 1001")

account = registry.find("1001")

account.statement()

print("\nUndo last transaction")

account.undo_last()

account.statement()