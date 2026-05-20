rating = float(input("Enter the rating of the food (0-5): "))
if rating > 4.5:
    print("Perfection")
elif rating > 4.0:
    print("Excellent")
elif rating > 3.0:
    print("Good")
elif rating > 2.0:
    print("Fair")
else:    
    print("Poor")
