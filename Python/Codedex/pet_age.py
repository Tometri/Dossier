pet_type = input("Enter the type of pet (dog/cat): ")
pet_age = int(input("Enter the age of your pet in animal years: "))
if pet_type == "dog":
    dog_age = pet_age * 7
    print("Your dog's age in human years is: " + str(dog_age))
elif pet_type == "cat":
    cat_age = pet_age * 6
    print("Your cat's age in human years is: " + str(cat_age))
else:
    print("Invalid pet type. Please enter 'dog' or 'cat'.")