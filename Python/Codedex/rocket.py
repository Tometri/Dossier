def distance_to_miles():
    distance = float(input("Enter the distance in kilometers: "))
    miles = distance / 1.609
    print(f"The distance in miles is: {miles:.2f}")

distance_to_miles()