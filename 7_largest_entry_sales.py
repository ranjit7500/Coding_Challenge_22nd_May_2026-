# Taking inputs
sale1 = int(input("Enter first sales figure: "))
sale2 = int(input("Enter second sales figure: "))
sale3 = int(input("Enter third sales figure: "))

# Finding largest number
if sale1 > sale2 and sale1 > sale3:
    print("Largest Sales Figure =", sale1)
elif sale2 > sale1 and sale2 > sale3:
    print("Largest Sales Figure =", sale2)
else:
    print("Largest Sales Figure =", sale3)
