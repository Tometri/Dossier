bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]
total = 0
for amount in bill:
    total += amount
print("Total bill amount: $", total)
num_people = 4
split_amount = total / num_people
print("Each person should pay: $", split_amount)