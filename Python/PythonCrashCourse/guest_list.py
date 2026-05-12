# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
dinner_guests = ['Beverly', 'Bailey', 'Bridgit', 'Araki Hirohiko']
print(dinner_guests[0] + ", I would like to invite you to dinner.")
print(dinner_guests[1] + ", I would like to invite you to dinner.")
print(dinner_guests[2] + ", I would like to invite you to dinner.")
print(dinner_guests[3] + ", I would like to invite you to dinner.")
print("Unfortunately, " + dinner_guests[3] + " can't make it to dinner.")
#3-5. Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
dinner_guests[3] = 'Hideo Kojima'
print(dinner_guests[0] + ", I would like to invite you to dinner.")
print(dinner_guests[1] + ", I would like to invite you to dinner.")
print(dinner_guests[2] + ", I would like to invite you to dinner.")
print(dinner_guests[3] + ", I would like to invite you to dinner.")
new_table = "I just found a bigger dinner table, so now more guests can come to dinner!"
print(new_table)
#3-6. More Guests: Use insert() to add one new guest to the beginning of your list, insert() to add one new guest to the middle of your list, and append() to add one new guest to the end of your list. Then print a new set of invitations
dinner_guests.insert((0), 'MeatCanyon')
dinner_guests.insert((2), "Wendigoon")
dinner_guests.insert((-1), "Jotaro Kujo")
print(dinner_guests[0] + ", I would like to invite you to dinner.")
print(dinner_guests[1] + ", I would like to invite you to dinner.")
print(dinner_guests[2] + ", I would like to invite you to dinner.")
print(dinner_guests[3] + ", I would like to invite you to dinner.")
print(dinner_guests[4] + ", I would like to invite you to dinner.")
print(dinner_guests[5] + ", I would like to invite you to dinner.")
print(dinner_guests[6] + ", I would like to invite you to dinner.")