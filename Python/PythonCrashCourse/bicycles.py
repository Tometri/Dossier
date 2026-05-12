#Square brackets indicate a list, which is a collection of items in a particular order.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#You can access any individual item in a list by using its index, which is the position of the item in the list.
print(bicycles[0])
print(bicycles[0].title())

#by using a negative index, you can start counting from the end of the list instead of the beginning.
print(bicycles[-1])

#an item from a list can be used in a messsage
message = "My first bicycle was a " + bicycles[0].title() + "."

#elements of a list can be changed by accessing the index and assigning a new value
bicycles[0] = 'trike'
print(bicycles)

#the simplest way to add a new item to the end of a list is to use the append() method
bicycles.append('huffy')
print(bicycles)

#you can start with an empty list and then add items to it
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#you can insert a new item at any position in your list by using the insert() method
motorcycles.insert(0, 'ducati') 
print(motorcycles)

#if you know the position of the item you want to remove from a list, you can use the del statement
del motorcycles[0]
print(motorcycles)

#the pop() method removes the last item in a list, but it lets you work with that item after removing it
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#you can also pop an item from any position in a list by including the index of the item you want to remove in parentheses
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#if you only know the value of the item you want to remove from a list, you can use the remove() method
motorcycles.remove('yamaha')
print(motorcycles)

#remove() can also be used to remove a value that is stored in a variable
cars = ['honda', 'toyota', 'subaru', 'tesla']
print(cars)
no_electric = 'tesla'
cars.remove(no_electric)
print(cars)

#the remove() method only removes the first occurrence of the value you specify. If there are multiple values, you’ll need to call remove() once for each value you want to remove or a loop can be used to remove all occurrences of a value in a list.
