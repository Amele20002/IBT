# -------------------------
# Observer
# -------------------------

class SMSAlert:

    def update(self, message):
        print("SMS:", message)


# -------------------------
# Alert Service
# -------------------------

class AlertService:

    @staticmethod
    def notify(account, message):
        account._notify(message)


# -------------------------
# Account
# -------------------------

class Account:

    def __init__(self, owner, account_number, balance=0):

        self.owner = owner
        self.account_number = account_number
        self._balance = balance

        self.history = []

        self._observers = []

    @property
    def balance(self):
        return self._balance

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):

        for observer in self._observers:
            observer.update(message)

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

        self.history.append(("deposit", amount))

        AlertService.notify(
            self,
            f"Deposited {amount} ETB"
        )

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

    def statement(self):

        print(
            self.owner,
            self.account_number,
            self.balance
        )


# -------------------------
# Registry
# -------------------------

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

    # -------------------------
    # Day 8
    # -------------------------

    def top_by_balance(self, n):

        accounts = sorted(

            self.accounts.values(),

            key=lambda account: account.balance,

            reverse=True

        )

        return accounts[:n]

    # -------------------------

    def binary_search(self, numbers, target):

        left = 0
        right = len(numbers) - 1

        while left <= right:

            mid = (left + right) // 2

            if numbers[mid] == target:
                return self.accounts[target]

            elif numbers[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return None

    # -------------------------

    def find_by_number(self, number):

        numbers = sorted(self.accounts.keys())

        return self.binary_search(numbers, number)

    # -------------------------

    def total_transactions(self, account):

        def recursive(history):

            if len(history) == 0:
                return 0

            return history[0][1] + recursive(history[1:])

        return recursive(account.history)


# -------------------------
# Main
# -------------------------

registry = AccountRegistry()

a1 = Account("Almaz", "1001", 2000)
a2 = Account("Dawit", "1002", 1500)
a3 = Account("Hanna", "1003", 4000)
a4 = Account("Samuel", "1004", 700)

registry.add(a1)
registry.add(a2)
registry.add(a3)
registry.add(a4)

a1.deposit(500)
a1.withdraw(100)

a2.deposit(300)

a3.deposit(1000)
a3.withdraw(200)

print("\nTop Accounts")

for account in registry.top_by_balance(3):

    print(
        account.owner,
        account.balance
    )

print("\nBinary Search")

found = registry.find_by_number("1002")

if found:

    found.statement()

print("\nTotal Transactions")

print(
    registry.total_transactions(a1)
)