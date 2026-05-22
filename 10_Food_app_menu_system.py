
while True:

 
    print("\n1. Pizza")
    print("2. Burger")
    print("3. Pasta")
    print("4. Exit")

   
    choice = input("Enter your choice: ")

  
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
