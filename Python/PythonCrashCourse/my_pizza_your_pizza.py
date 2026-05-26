my_pizzas = ['salami', 'pepperonit', 'spinach and alfredo']
friends_pizzas = my_pizzas.copy()
friends_pizzas.append('pineapple')
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
    