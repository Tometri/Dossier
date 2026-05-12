cars = ['Honda','Subaru','Porsche','Toyota','Audi']
print("Original list:" + str(cars))
#lists can be permanently sorted using the sort() method
cars.sort()
print("Sorted list:" + str(cars))
#sort() method can be used with the reverse argument to sort in reverse order
cars.sort(reverse=True)
print("Reverse sorted list:" + str(cars))
#the sorted() function lets you display in a particular order without changing the original list
print("Original list:" + str(cars))
print("Temporarily sorted list:" + str(sorted(cars)))
print("Original list:" + str(cars))
#reverse() method reverses the order of a list permanently
cars.reverse()
print("Reversed list:" + str(cars))
#you can find the length of a list using the len() function
print("Number of cars in the list:" + str(len(cars)))