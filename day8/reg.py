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
            print(account.account_number, account.owner, account.balance)

    # -------------------------
    # Leaderboard
    # -------------------------

    def top_by_balance(self, n=5):

        accounts = sorted(
            self.accounts.values(),
            key=lambda account: account.balance,
            reverse=True
        )

        return accounts[:n]

    # -------------------------
    # Binary Search
    # -------------------------

    def binary_search(self, numbers, target):

        left = 0
        right = len(numbers) - 1

        while left <= right:

            mid = (left + right) // 2

            if numbers[mid] == target:
                return mid

            elif numbers[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1

    # -------------------------
    # Find by Number
    # -------------------------

    def find_by_number(self, number):

        nums = sorted(self.accounts.keys())

        i = self.binary_search(nums, number)

        if i >= 0:
            return self.accounts[nums[i]]

        return None

    # -------------------------
    # Recursive Total
    # -------------------------

    def total_transactions(self, account):

        def recursive(history):

            if len(history) == 0:
                return 0

            return history[0][1] + recursive(history[1:])

        return recursive(account.history)