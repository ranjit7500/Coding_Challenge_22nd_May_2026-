# Taking age input
age = int(input("Enter age: "))

# Checking age category
if age < 12:
    print("Ticket Price = 100")
elif age < 60:
    print("Ticket Price = 200")
else:
    print("Ticket Price = 150")