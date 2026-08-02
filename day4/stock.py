stock = {}

# Read stock from file
try:
    with open("stock.txt", "r") as f:
        for line in f:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)

except FileNotFoundError:
    print("No stock file yet — starting empty")

# Function to adjust stock
def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount

# Update stock
adjust("Paracetamol", 5)
adjust("Ibuprofen", -2)

# Show all stock
print("Current Stock:")
for item, qty in stock.items():
    print(f"{item}: {qty}")

# Show low stock
low = [item for item, qty in stock.items() if qty < 10]
print("Low stock:", low)

# Save updated stock
with open("stock.txt", "w") as f:
    for item, qty in stock.items():
        f.write(f"{item},{qty}\n")