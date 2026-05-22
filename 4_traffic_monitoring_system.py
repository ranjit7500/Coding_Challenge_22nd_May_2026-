# Taking speed input
speed = int(input("Enter vehicle speed: "))

# Defining speed limit
speed_limit = 60

# Checking speed
if speed > speed_limit:
    print("Vehicle exceeded the speed limit")
else:
    print("Vehicle is within speed limit")
