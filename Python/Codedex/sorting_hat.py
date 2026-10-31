print("Welcome to the Sorting Hat Quiz! \nAnswer the following questions to find out which Hogwarts house you belong to!")

points_gryffindor = 0
points_hufflepuff = 0
points_ravenclaw = 0
points_slytherin = 0

question_one = int(input("Q1: Which do you prefer, Dusk or Dawn? \n1) Dusk \n2) Dawn \nAnswer: "))
if question_one == 1:
    points_gryffindor += 1
    points_ravenclaw += 1
elif question_one == 2:
    points_hufflepuff += 1
    points_slytherin += 1
else:
    print("Invalid input. Please enter 1 or 2.")

question_two = int(input("Q2: When you die, you want to be remembered as? \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold \nAnswer: "))
if question_two == 1:
    points_hufflepuff += 2
elif question_two == 2:
    points_slytherin += 2
elif question_two == 3:
    points_ravenclaw += 2
elif question_two == 4:
    points_gryffindor += 2
else:
    print("Invalid input. Please enter 1, 2, 3, or 4.")

question_three = int(input("Q3: Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum \nAnswer: "))
if question_three == 1:
    points_slytherin += 4
elif question_three == 2:
    points_hufflepuff += 4
elif question_three == 3:
    points_ravenclaw += 4
elif question_three == 4:
    points_gryffindor += 4
else:
    print("Invalid input. Please enter 1, 2, 3, or 4.")

# Determine the house with the most points
houses = {
    "Gryffindor": points_gryffindor,
    "Hufflepuff": points_hufflepuff,
    "Ravenclaw": points_ravenclaw,
    "Slytherin": points_slytherin
}
print("\nCalculating your house...")
print("Gryffindor points:", points_gryffindor)
print("Hufflepuff points:", points_hufflepuff)
print("Ravenclaw points:", points_ravenclaw)
print("Slytherin points:", points_slytherin)
highest_points = max(houses.values())
sorted_houses = sorted(houses.items(), key=lambda item: item[1], reverse=True)
if sorted_houses[0][1] == sorted_houses[1][1]:
    print("It's a tie between", sorted_houses[0][0], "and", sorted_houses[1][0] + "!")
else:    print("You belong to", sorted_houses[0][0] + "!")