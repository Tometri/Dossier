menu = [
    '🍔 Cheeseburger',
    '🍟 Fries',
    '🥤 Soda',
    '🍦 Ice Cream',
    '🍪 Cookie'
]
def get_item():
    order = input("Please enter the item you'd like to order: ")
    if order in menu:
        print(f"Great choice! Your {order} will be ready shortly.")
    else:        print("Sorry, we don't have that item. Please choose from the menu.")

def welcome():
    print("Welcome to the Drive-Thru! Here's our menu:")
    for item in menu:
        print(item)

def main():
    welcome()
    get_item()

main()