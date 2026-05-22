# Creating function
def calculate_bill(units):

    # Checking bill conditions
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = units * 7
    else:
        bill = units * 10

    # Returning bill amount
    return bill

# Taking input
units = int(input("Enter electricity units: "))

# Calling function
amount = calculate_bill(units)

# Displaying result
print("Electricity Bill =", amount)
