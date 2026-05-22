# Taking purchase amount as input
amount = float(input("Enter purchase amount: "))

# Checking discount conditions
if amount >= 5000:
    discount = amount * 0.20   # 20% discount
elif amount >= 3000:
    discount = amount * 0.10   # 10% discount
else:
    discount = amount * 0.05   # 5% discount

# Calculating final amount
final_amount = amount - discount

# Displaying final bill
print("Final Bill Amount =", final_amount)
