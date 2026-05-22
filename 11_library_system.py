# List containing overdue status
books = ["yes", "no", "yes", "yes", "no"]

# Initializing counter
count = 0

# Loop through list
for book in books:

    # Checking overdue book
    if book == "yes":
        count += 1

# Displaying total overdue books
print("Total Overdue Books =", count)