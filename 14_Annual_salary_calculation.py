# Creating function
def annual_salary(monthly_salary):

    # Calculating annual salary
    yearly_salary = monthly_salary * 12

    # Returning annual salary
    return yearly_salary

# Taking input
monthly = float(input("Enter monthly salary: "))

# Calling function
salary = annual_salary(monthly)

# Displaying result
print("Annual Salary =", salary)
