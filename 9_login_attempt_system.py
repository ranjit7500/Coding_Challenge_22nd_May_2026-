# Predefined password
correct_password = "python123"


attempt = 1

# Loop for maximum 3 attempts
while attempt <= 3:

    # Taking password input
    password = input("Enter password: ")

    # Checking password
    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")

    # Increasing attempt count
    attempt += 1

# If all attempts finished
if attempt > 3:
    print("Maximum attempts reached")