from math import pi
from random import choice as ch 

planets = [
'Mercury',
'Venus',
'Earth',
'Mars',
'Saturn']

def random_planet():
    return ch(planets)

planet = random_planet()
if planet == 'Earth':
    r = 6371
elif planet == 'Mars':
    r = 3390
elif planet == 'Mercury':
    r = 2440
elif planet == 'Venus':
    r = 6052
elif planet == 'Saturn':
    r = 58232
else:
    print("Oops! An error occurred.")

area = 4 * pi * r**2

print(f"The surface area of {planet} is approximately {area:.2f} square kilometers.")