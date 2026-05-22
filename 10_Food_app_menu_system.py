# Infinite loop
while True:

    # Displaying menu
    print("\n1. Pizza")
    print("2. Burger")
    print("3. Pasta")
    print("4. Exit")

    # Taking user choice
    choice = input("Enter your choice: ")

    # Checking choice
    if choice == "1":
        print("Pizza Selected")
    elif choice == "2":
        print("Burger Selected")
    elif choice == "3":
        print("Pasta Selected")
    elif choice == "4":
        print("Exiting Menu")
        break
    else:
        print("Invalid Choice")
