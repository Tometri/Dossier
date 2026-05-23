earth_weight = float(input('Enter your weight: '))
planet = int(input('Enter the planet number: '))
if planet == 1:
  destination_weight = earth_weight * 0.38
  print(destination_weight)

elif planet == 2:
  destination_weight = earth_weight * 0.91
  print(destination_weight)

elif planet == 3:
  destination_weight = earth_weight * 0.38
  print(destination_weight)

elif planet == 4:
  destination_weight = earth_weight * 2.53
  print(destination_weight)

elif planet == 5:
    destination_weight = earth_weight * 1.07
    print(destination_weight)

elif planet == 6:
    destination_weight = earth_weight * 0.89
    print(destination_weight)  

elif planet == 7:
    destination_weight = earth_weight * 1.14
    print(destination_weight)

else:
    print("Invalid planet number. Please enter a number between 1 and 7.")
    