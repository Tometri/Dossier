height = int(input("Enter your height in cm: "))
credits = int(input("Enter your credits: "))
if height >= 136 and credits >= 10:
    print("Enjoy the ride!")
elif height < 136 and credits >= 10:
    print("You are not tall enough to ride.")
elif height >= 136 and credits < 10:
    print("You do not have enough credits to ride.")
else:
    print("You do not meet the requirements to ride.")