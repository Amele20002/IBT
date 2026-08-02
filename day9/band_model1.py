from collections import deque

# -------------------------
# Branch Tree
# -------------------------

class Branch:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.children = []

    def add_branch(self, branch):
        self.children.append(branch)

    def total_balance(self):

        total = self.balance

        for child in self.children:
            total += child.total_balance()

        return total


# -------------------------
# Build Tree
# -------------------------

head = Branch("Head Office", 10000)

addis = Branch("Addis Region", 5000)
oromia = Branch("Oromia Region", 4000)

cbe1 = Branch("CBE-1", 3000)
cbe2 = Branch("CBE-2", 2500)
cbe3 = Branch("CBE-3", 3500)

head.add_branch(addis)
head.add_branch(oromia)

addis.add_branch(cbe1)
addis.add_branch(cbe2)

oromia.add_branch(cbe3)

# -------------------------
# Graph
# -------------------------

transfers = {
    "CBE-1": ["CBE-2", "CBE-3"],
    "CBE-2": ["CBE-4"],
    "CBE-3": ["CBE-4"],
    "CBE-4": []
}

# -------------------------
# BFS
# -------------------------

def bfs(graph, start):

    visited = []

    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:

            visited.append(node)

            for neighbour in graph[node]:
                queue.append(neighbour)

    return visited


# -------------------------
# Main
# -------------------------

print("Total Bank Balance:", head.total_balance(), "ETB")

print("\nBranches reachable from CBE-1:")

for branch in bfs(transfers, "CBE-1"):
    print(branch)
    #2
    from collections import deque

# -------------------------
# Account Class
# -------------------------

class Account:

    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance


# -------------------------
# Branch Class
# -------------------------

class Branch:

    def __init__(self, name):
        self.name = name
        self.children = []      # Sub-branches
        self.accounts = []      # Accounts in this branch

    def add_branch(self, branch):
        self.children.append(branch)

    def add_account(self, account):
        self.accounts.append(account)

    def total_balance(self):

        # Total balance of accounts in this branch
        total = sum(account.balance for account in self.accounts)

        # Add balances of all child branches
        for child in self.children:
            total += child.total_balance()

        return total


# -------------------------
# Build Branch Tree
# -------------------------

head = Branch("Head Office")

addis = Branch("Addis Region")
oromia = Branch("Oromia Region")

cbe1 = Branch("CBE-1")
cbe2 = Branch("CBE-2")
cbe3 = Branch("CBE-3")

head.add_branch(addis)
head.add_branch(oromia)

addis.add_branch(cbe1)
addis.add_branch(cbe2)

oromia.add_branch(cbe3)


# -------------------------
# Add Accounts
# -------------------------

cbe1.add_account(Account("Almaz", "1001", 2000))
cbe1.add_account(Account("Samuel", "1002", 1500))

cbe2.add_account(Account("Dawit", "1003", 3000))

cbe3.add_account(Account("Hanna", "1004", 2500))
cbe3.add_account(Account("Abel", "1005", 1800))


# -------------------------
# Transfers Graph
# -------------------------

transfers = {
    "1001": ["1002", "1003"],
    "1002": ["1004"],
    "1003": ["1005"],
    "1004": ["1005"],
    "1005": []
}


# -------------------------
# Breadth First Search
# -------------------------

def bfs(graph, start):

    visited = []
    queue = deque([start])

    while queue:

        current = queue.popleft()

        if current not in visited:

            visited.append(current)

            for neighbour in graph.get(current, []):
                queue.append(neighbour)

    return visited


# -------------------------
# Main Program
# -------------------------

print("Total Bank Balance")
print(head.total_balance(), "ETB")

print()

print("Accounts Reachable from 1001")

reachable = bfs(transfers, "1001")

for account in reachable:
    print(account)