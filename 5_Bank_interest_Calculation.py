# Taking inputs
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

# Calculating simple interest
si = (principal * rate * time) / 100

# Displaying result
print("Simple Interest =", si)