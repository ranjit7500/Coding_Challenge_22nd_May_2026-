
amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20   # 20% discount
elif amount >= 3000:
    discount = amount * 0.10   # 10% discount
else:
    discount = amount * 0.05   # 5% discount

final_amount = amount - discount


print("Final Bill Amount =", final_amount)
