class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name = "Bob's Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

Beeboops = Restaurant()
Beeboops.name = "Galactic Fye"
Beeboops.category = "Intergalactic Cuisine"
Beeboops.rating = 4.9
Beeboops.delivery = True

CustyDavers = Restaurant()
CustyDavers.name = "Custy Davers"
CustyDavers.category = "Dwarven Delights"
CustyDavers.rating = 4.5
CustyDavers.delivery = False

print(vars(bobs_burgers))
print(vars(Beeboops))
print(vars(CustyDavers))