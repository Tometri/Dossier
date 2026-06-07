current_users = ['herobrine', 'John 117', 'Batman', 'Arthur Morgan', 'Solid Snake']
new_users = ['SumBum', 'herobrine', 'that guy, from fortnite', 'Bill_from_accounting', 'Jimmy Neutron']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")