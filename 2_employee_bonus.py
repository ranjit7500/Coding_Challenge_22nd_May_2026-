attendance = float(input("Enter attendance percentage: "))
performance = int(input("Enter performance rating (1-10): "))


if attendance >= 90 and performance >= 8:
    print("Employee is eligible for bonus")
else:
    print("Employee is not eligible for bonus")
