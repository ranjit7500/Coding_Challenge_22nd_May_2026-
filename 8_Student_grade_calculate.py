
# Taking marks input
m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

# Calculating total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Checking grades
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# Displaying result
print("Percentage =", percentage)
print("Grade =", grade)