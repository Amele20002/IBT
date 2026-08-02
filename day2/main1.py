# Loop over a range of numbers
#for i in range(1, 4):
# print(f"Receipt #{i}")
# Receipt #1 / #2 / #3
# Loop over a list of names
#names = ["Almaz", "Dawit", "Tigist"]
#for name in names:
#print(f"Selam, {name}")
#day2 exercise
# total_bill=3000
# number_of_people=4
# def split_bill(total, people, tip_rate=0.10):
#     tip_amount=total*tip_rate
#     total_tip_with_tip= total+ tip_amount
#     per_person = total_tip_with_tip / people
#     return per_person
# # Step 3: Use the function to calculate each person's share
# share = split_bill(total_bill, number_of_people)

# # Step 4: List of names
# names = ["Almaz", "Dawit", "Tigist"]

# # Step 5: Loop through names and print each person's share
# for name in names:
#     print(f"{name} should pay {share:.2f} ETB")
#day 2 exercise
# List of customers (name, balance)
customers = [
    ("Almaz", 1500),
    ("Dawit", 700),
    ("Tigist", 200),
    ("Hanna", 1200),
    ("Samuel", 450),
]

# Function to determine customer tier
def tier(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"

# Counters for each tier
premium = 0
standard = 0
basic = 0

print("Customer Report")
print("-" * 40)

# Loop through customers
for name, balance in customers:
    customer_tier = tier(balance)

    print(f"{name}: {customer_tier} ({balance} ETB)")

    # Count the tiers
    if customer_tier == "Premium":
        premium += 1
    elif customer_tier == "Standard":
        standard += 1
    else:
        basic += 1

# Print summary
print("\nSummary")
print(f"Premium Customers: {premium}")
print(f"Standard Customers: {standard}")
print(f"Basic Customers: {basic}")