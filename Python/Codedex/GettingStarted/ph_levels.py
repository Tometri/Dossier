ph = float(input("Enter the pH level: "))
if ph > 7:
    print("The solution is basic.")
elif ph < 7:
    print("The solution is acidic.")
else:
    print("The solution is neutral.")